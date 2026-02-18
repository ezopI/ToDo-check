from flask import Flask, render_template, request, redirect, url_for, jsonify
import sqlite3

app = Flask(__name__)
DB_NAME = 'todo.db'

def get_db():
    # Conectar ao banco de dados
    conn = sqlite3.connect(DB_NAME)
    # row_factory permite acesso por nome de coluna
    conn.row_factory = sqlite3.Row  
    return conn

def init_db():
    # Criar a tabela de tarefas se não existir
    conn = get_db()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS todos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            completed BOOLEAN NOT NULL DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    # Exibir a lista de tarefas
    conn = get_db()
    todos = conn.execute('SELECT * FROM todos ORDER BY id DESC').fetchall()
    conn.close()
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add():
    # Adicionar uma nova tarefa
    title = request.form.get('title', '').strip()
    print(f"TITULO RECEBIDO: {title}")
    if title:
        conn = get_db()
        conn.execute("INSERT INTO todos (title, completed) VALUES (?, 0)", (title,))
        conn.commit()
        conn.close()
        print(f"Tarefa '{title}' adicionada com sucesso.")
    return redirect(url_for('index'))

@app.route('/toggle/<int:task_id>', methods=['POST'])
def toggle(task_id):
    # Alternar o status de conclusão de uma tarefa
    conn = get_db()
    conn.execute('UPDATE todos SET completed = CASE completed WHEN 0 THEN 1 ELSE 0 END WHERE id = ?', (task_id,))
    conn.commit()

    # Retornar o status atualizado da tarefa
    updated = conn.execute('SELECT * FROM todos WHERE id = ?', (task_id,)).fetchone()
    conn.close()
    return jsonify({"id": updated["id"], "completed": updated["completed"]})

@app.route("/delete/<int:task_id>", methods=["POST"])
def delete(task_id):
    # Excluir uma tarefa
    conn = get_db()
    conn.execute("DELETE FROM todos WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()
    return redirect(url_for("index"))

if __name__ == '__main__':
    init_db()
    app.run()
