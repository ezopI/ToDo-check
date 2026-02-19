# ToDo-Check 📝

🌟 Full-stack ToDo Web App com autenticação, PostgreSQL, Flask, SQLAlchemy e Bootstrap.

👉 Live Demo: https://todo-flask-0b1d.onrender.com/

---

## Sobre

Este projeto é uma aplicação de lista de tarefas (ToDo) com:

✅ Cadastro de usuário  
✅ Login e logout  
✅ Associação de tarefas por usuário  
✅ Marcar tarefas como concluídas  
✅ Deletar tarefas  
✅ Backend em Python + Flask  
✅ Banco de dados PostgreSQL  
✅ ORM SQLAlchemy  
✅ Frontend com Bootstrap + templates Jinja2  
✅ Deploy em produção (Render)

---

## Tecnologias utilizadas

| Camada | Tecnologia |
|--------|------------|
| Backend | Python 3.12 + Flask |
| ORM | SQLAlchemy |
| Banco de Dados | PostgreSQL |
| Frontend | HTML, CSS, JS e Bootstrap |
| Deploy | Render |

---

## Funcionalidades

✔️ Criar conta de usuário  
✔️ Login e logout  
✔️ Adicionar tarefas  
✔️ Marcar como concluída  
✔️ Excluir tarefas  
✔️ Usuário vê apenas suas próprias tarefas

---

## Como rodar localmente

### 1- Clone o repositório

```bash
git clone https://github.com/ezopI/ToDo-check.git
cd ToDo-check
```

### 2- Crie e ative um ambiente virtual
```bash
python3 -m venv .venv
source .venv/bin/activate    # Linux/Mac
# .venv\Scripts\activate     # Windows
```

### 3- Instale as dependências

```bash
uv pip install -r requirements.txt
```

### 4 Rodar

#### Opção A (mais simples): rodar sem Docker(SQLite automático)

> Caso você não tenha Docker e/ou PostgreSQL isntalado, o projeto usa automaticamente o SQLite

```bash
export SECRET_KEY="dev-key"
uv run --active app.py
```
O banco será criado localmente como ```local.db```

Acesse
```bash
http://127.0.0.1:5000
```

---

#### Opção B (produção): rodar com PostgreSQL (Docker)

##### 1- Rode o PostgreSQL
```bash
docker run --name todo_pg \
  -e POSTGRES_USER=todo \
  -e POSTGRES_PASSWORD=todo123 \
  -e POSTGRES_DB=todo_db \
  -p 5432:5432 \
  -d postgres:16
```

##### 2- Configurar variáveis de ambiente
```bash
export DATABASE_URL="postgresql+psycopg://todo:todo123@localhost:5432/todo_db"
export SECRET_KEY="dev-key"
```

##### 3- Iniciar a aplicação
```bash
uv run --active app.py
```

Abra no navegador
```bash
http://127.0.0.1:5000
```
---

## Deploy render

Neste projeto temos o render.yaml, facilitando um deploy a partir do Blueprint.

- Conecte o GitHub no Render
- Faça o deploy via Blueprint
- Adicione a variável ```SECRET_KEY``` em <em>Environment Variables</em>
- O Render provisiona o PostgreSQL e injeta ```DATABASE_URL``` automaticamente

## Preview

![Funcionamento do app Demo](images/toDoCheckFinal.gif)
---
![Página de Registro](images/registro.png)

- Username (seu nome)
- Email
- Senha

---

Desenvolvi esse projeto com o intuito de facilitar as atividades do dia a dia, utilizando pelo PC e também mobile.