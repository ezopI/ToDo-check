# ToDo Check 📝

🇧🇷[Portugês](README-ptbr.md)

🌟 Full-stack ToDo web application with authentication, Flask, SQLAlchemy, Bootstrap, and PostgreSQL (production-ready).

👉 Live Demo: https://todo-flask-0b1d.onrender.com/

---

## About

This project is a ToDo list application featuring:

✅ User registration  
✅ Login and logout  
✅ User-specific task isolation (each user sees only their own tasks)  
✅ Mark tasks as completed  
✅ Delete tasks  
✅ Python (Flask) backend  
✅ SQLAlchemy ORM  
✅ PostgreSQL database (production)  
✅ Bootstrap frontend with Jinja2 templates  
✅ Production deployment on Render via `render.yaml`

---

## Technologies Used

| Layer | Technology |
|-------|------------|
| Backend | Python 3.12 + Flask |
| Authentication | Flask-Login |
| ORM | SQLAlchemy |
| Database | PostgreSQL (production) / SQLite (local development) |
| Frontend | HTML, CSS, JavaScript, Bootstrap |
| Deployment | Render |

---

## Features

✔️ User account creation  
✔️ Login and logout  
✔️ Add new tasks  
✔️ Mark tasks as completed  
✔️ Delete tasks  
✔️ Multi-user architecture (task isolation per user)

---

## Running Locally

### 1- Clone the repository
```bash
git clone https://github.com/ezopI/ToDo-check.git
cd ToDo-check
```

### 2- Create and active virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate    # Linux/Mac
# .venv\Scripts\activate     # Windows
```

### 3- Install dependecies
```bash
uv pip install -r requirements.txt
```

### 4- Run

#### Option A (Simplest): Run without Docker (Automatic SQLite)

> If you do not have Docker or PostgreSQL installed, the project automatically uses SQLite.

```bash
export SECRET_KEY="dev-secret"
uv run --active app.py
```

A local SQLite database file (```local.db```) will be created automatically.

Open in your browser:
```bash
http://127.0.0.1:5000
```

#### Option B (Production-like): Run with PostgreSQL (Docker)

##### 1- Start PostgreSQL locally
```bash
docker run --name todo_pg \
  -e POSTGRES_USER=todo \
  -e POSTGRES_PASSWORD=todo123 \
  -e POSTGRES_DB=todo_db \
  -p 5432:5432 \
  -d postgres:16
```

##### 2- Configure environment variables
```bash
export DATABASE_URL="postgresql+psycopg://todo:todo123@localhost:5432/todo_db"
export SECRET_KEY="dev-secret"
```

##### 3- Start the application
```bash
uv run --active app.py
```

Access:
```bash
http://127.0.0.1:5000
```

## Deployment (Render)

This project includes a render.yaml file, enabling easy deployment via Blueprint.

Steps:

- Connect your GitHub repository to Render
- Deploy using the Blueprint configuration
- Add the ```SECRET_KEY``` variable under <em>Environment Variables</em>
- Render automatically provisions PostgreSQL and injects ```DATABASE_URL```

## Preview

![ToDo Check Demo](images/toDoCheckFinal.gif)
---
![Register Page](images/registro.png)

- Username
- Email
- Senha

---

This project was built to simplify everyday task management, designed for both desktop and mobile use.