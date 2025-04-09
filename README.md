
# Django Q&A App

A simple Quora-like Question and Answer web application built using Django and Bootstrap. Users can register, log in, ask questions, and answer others.

---

## Features

- User registration and login  
- Ask questions (only when logged in)  
- View all questions and answers  
- Post answers to questions  
- Like/unlike answers  
- Responsive UI using Bootstrap  
- Simple user access control (only logged-in users can post questions or answers)  

---

## Tech Stack

- **Backend**: Django (Python)  
- **Frontend**: HTML, Bootstrap  
- **Database**: SQLite3 (default in Django)  

---

## Getting Started

### 1. Clone the repository

git clone https://github.com/arjun915/website.git  
cd website

---

### 2. Ensure Django and Python are installed on the system

### 3. Run the project

python manage.py runserver  

Visit the app in your browser at:  
http://127.0.0.1:8000

---

### Working

- Register a new account via the Register page  
- Log in with your credentials  
- Ask a new question using the Ask a Question button (only for logged-in users)  
- Answer any existing questions (only for logged-in users)  
- Like or unlike answers (only for logged-in users)  
- Logout  

---

### Notes

- No password validation rules are enforced  
- Uses Django’s built-in SQLite3 database  

---

### Future Enhancements

- Add password validation  
- Allow editing or deleting answers  
