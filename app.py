import os
from flask import Flask, render_template, request, redirect, url_for, jsonify, flash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user, UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from models import Base, engine, SessionLocal, Todo, User

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev_secret_key")

login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.init_app(app)

def init_db():
    Base.metadata.create_all(bind=engine)

class LoginUser(UserMixin):
    def __init__(self, db_user: User):
        self.id = db_user.id
        self.email = db_user.email
        self.username = db_user.username

@login_manager.user_loader
def load_user(user_id: str):
    db = SessionLocal()
    u = db.get(User, int(user_id))
    db.close()
    if not u:
        return None
    return LoginUser(u)

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username", "").strip().lower()
        email = request.form.get("email", "").strip().lower()
        password_hash = request.form.get("password", "")

        if not username or not email or not password_hash:
            flash("Fill email and password.")
            return redirect(url_for("register"))
        
        db = SessionLocal()
        exists = db.query(User).filter(User.email == email).first()
        if exists:
            db.close()
            flash("Email already registered.")
            return redirect(url_for("register"))
        
        u = User(email=email, password_hash=generate_password_hash(password_hash))
        db.add(u)
        db.commit()
        db.refresh(u)  # Para obter o ID gerado

        # login automático após registro
        login_user(LoginUser(u), remember=True)
        db.close()
        return redirect(url_for("index"))
    
    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")

        db = SessionLocal()
        u = db.query(User).filter(User.email == email).first()
        if not u or not check_password_hash(u.password_hash, password):
            db.close()
            flash("Invalid email or password.")
            return redirect(url_for("login"))
        
        db.close()
        login_user(LoginUser(u), remember=True)
        return redirect(url_for("index"))
    
    return render_template("login.html")

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))

@app.route('/')
@login_required
def index():
    db = SessionLocal()
    todos = (db.query(Todo).filter(Todo.user_id == int(current_user.id)).order_by(Todo.id.desc()).all())
    db.close()
    return render_template("index.html", todos=todos, user_email=getattr(current_user, "email", ""))

@app.route("/add", methods=["POST"])
@login_required
def add():
    # Adicionar uma nova tarefa
    title = request.form.get("title", "").strip()
    if title:
        db = SessionLocal()
        db.add(Todo(title=title, completed=False, user_id=int(current_user.id)))
        db.commit()
        db.close()
    return redirect(url_for("index"))

@app.route('/toggle/<int:todo_id>', methods=['POST'])
@login_required
def toggle(todo_id):
    db = SessionLocal()
    t = (
        db.query(Todo)
        .filter(Todo.id == todo_id, Todo.user_id == int(current_user.id))
        .first()
    )
    if not t:
        db.close()
        return jsonify({"error": "Not found"}), 404
    
    t.completed = not t.completed
    db.commit()
    new_value = t.completed
    db.close()
    return jsonify({"id": todo_id, "completed": 1 if new_value else 0})

@app.route("/delete/<int:todo_id>", methods=["POST"])
@login_required
def delete(todo_id):
    # Excluir uma tarefa
    db = SessionLocal()
    t = (
        db.query(Todo)
        .filter(Todo.id == todo_id, Todo.user_id == int(current_user.id))
        .first()
    )
    if t:
        db.delete(t)
        db.commit()
    db.close()
    return redirect(url_for("index"))

if __name__ == '__main__':
    init_db()
    app.run()
