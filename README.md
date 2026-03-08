# AI Expense Tracker

AI-powered expense tracking web application where users can manage expenses using a natural language chatbot.

This project allows users to add, update, delete, and analyze expenses through conversational interaction with an AI assistant.

Live Demo:
https://ai-expense-tracker-beta-eight.vercel.app

Demo Login:
Username: rahul
Password: 1234
---

# Features

### User Authentication
- Signup and Login system
- Secure login before accessing the dashboard

### AI Chatbot
Users can manage expenses using natural language.

Example:

I spent 200 on food  
Uber ride cost 150  
I paid electricity bill 1200  

The chatbot extracts:
- Amount
- Category
- Context

and stores it in the database.

---

### Expense CRUD Operations

Create expense  
Read expenses  
Update expense  
Delete expense  

Example chatbot commands:

I spent 200 on food  
show expenses  
update last expense to 300  
delete expense  

---

### Dashboard Analytics

Dashboard shows:

- Total spending
- Category breakdown
- Pie chart visualization
- Spending insights

---

### Expense History

Table listing all transactions:

- Category
- Amount

---

### Budget Management

Users can set budgets.

Example:

set food budget 500

---

### AI Insights

Example command:

give me spending insights

Example response:

Total spent ₹1550. Highest category: bills

---

# Tech Stack

Frontend  
React + Vite

Backend  
FastAPI (Python)

Database  
SQLite

AI Integration  
Google Gemini API

Charts  
Chart.js

---

# Project Structure
AI-Expense-Tracker
│
├── backend
│ ├── main.py
│ ├── models.py
│ ├── crud.py
│ ├── database.py
│ ├── ai_parser.py
│
├── frontend
│ ├── src
│ │ ├── App.jsx
│ │ ├── Dashboard.jsx
│ │ ├── Chatbot.jsx
│ │ ├── ExpenseHistory.jsx
│ │ ├── Login.jsx
│ │ └── style.css
│
└── README.md

---

# Login Credentials (Demo)

Use the following credentials to log in:

Username: rahul  
Password: 1234

---

# Running the Project Locally

## Run Backend

Open terminal and run:
cd backend
python -m venv venv
venv\Scripts\activate
pip install fastapi uvicorn sqlalchemy google-generativeai
uvicorn main:app --reload

Backend runs on:
http://127.0.0.1:8000

---

## Run Frontend

Open another terminal and run:
cd frontend
npm install
npm run dev

Frontend runs on:
http://localhost:5173

---

# Example Chatbot Commands
I spent 200 on food
Uber ride cost 150
I paid electricity bill 1200
show expenses
update last expense to 300
delete expense
give me spending insights

# Author

Rahul R  
Computer Science Engineering Student
