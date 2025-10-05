# 🚀 Flask REST API Starter Kit

This is a starter template for building REST APIs using Flask.  
It comes with user CRUD routes, a simple in-memory "database", and example tests.  

---

## 🔧 Setup
1. Clone or download this project.
2. Install dependencies:pip install -r requirments 
3. Run the server: python app.py
4. Test endpoints with curl, Postman, or your browser:
- GET users: `http://127.0.0.1:5000/users/`
- POST user: `http://127.0.0.1:5000/users/` (JSON body: `{ "name": "Alice" }`)
- PUT user: `http://127.0.0.1:5000/users/0`
- DELETE user: `http://127.0.0.1:5000/users/0`

## ✅ Features
- Flask project structure  
- CRUD endpoints for users  
- In-memory "database"  
- Basic tests with Pytest  
- Beginner-friendly comments  

## 🎯 Next Steps
- Replace the in-memory DB with SQLite or PostgreSQL  
- Add authentication routes  
- Expand the data model  

