# FastAPI-crud-api
Building APIs with CRUD operations using FastAPI 
👇

📌 FastAPI CRUD API with JWT Authentication
🚀 Project Overview
This project is a backend API built using FastAPI that supports:

CRUD Operations (Create, Read, Delete)

Database Integration (SQLite + SQLAlchemy)

User Authentication using JWT (JSON Web Tokens)

Protected Routes (only accessible to authenticated users)

🛠️ Tech Stack
FastAPI – Backend framework

SQLite – Database

SQLAlchemy – ORM

Pydantic – Data validation

JWT (python-jose) – Authentication

Passlib (bcrypt) – Password hashing

Uvicorn – ASGI server

📂 Project Structure
fastapi-crud-api/
│
├── main.py            # Main FastAPI app
├── models.py          # Database models
├── database.py        # Database connection
├── auth_utils.py      # JWT & password hashing
├── requirements.txt   # Dependencies
└── README.md
⚙️ Features
✅ CRUD Operations
Create post

Get all posts

Get single post

Delete post

🔐 Authentication
User Signup

User Login

JWT Token generation

Password hashing using bcrypt

🔒 Protected Routes
Only authenticated users can access certain endpoints

🧠 API Endpoints
🔹 Authentication
Method	Endpoint	Description
POST	/signup	Register new user
POST	/login	Login and get JWT token
🔹 Posts
Method	Endpoint	Description
POST	/posts	Create post (Protected)
GET	/posts	Get all posts
GET	/posts/{id}	Get single post
DELETE	/posts/{id}	Delete post
🔑 Authentication Usage
Login via /login

Copy the access_token

Click Authorize 🔒 in Swagger UI

Enter:

Bearer YOUR_TOKEN
🗄️ Database
SQLite database (test.db)

Tables:

users

posts

▶️ How to Run Locally
1️⃣ Clone the repository
git clone https://github.com/YOUR_USERNAME/fastapi-crud-api.git
cd fastapi-crud-api
2️⃣ Create virtual environment
python -m venv testenv
Activate:

testenv\Scripts\activate   # Windows
3️⃣ Install dependencies
pip install -r requirements.txt
4️⃣ Run server
python -m uvicorn main:app --reload
5️⃣ Open in browser
👉 Swagger UI:

http://127.0.0.1:8000/docs
⚠️ Important Notes
Do NOT upload:

testenv/
__pycache__/
*.db
Use .gitignore file

🎯 Learning Outcomes
From this project, I learned:

Building REST APIs with FastAPI

Connecting backend to database

Using SQLAlchemy ORM

Implementing JWT Authentication

Securing APIs with protected routes

Debugging real backend errors

🚀 Future Improvements
Update (PUT/PATCH) APIs

Role-based authentication (admin/user)

PostgreSQL integration

Deployment (Render / Railway)

Better project structure (routers, services)

👩‍💻 Author
Aditi Shete


