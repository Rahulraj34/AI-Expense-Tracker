from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from database import engine, SessionLocal
import models
import crud

app = FastAPI()

# create database tables
models.Base.metadata.create_all(bind=engine)

# ---------------------------
# CORS CONFIGURATION
# ---------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # allow all domains (for deployment)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# handle browser preflight
@app.options("/{rest_of_path:path}")
async def preflight_handler(rest_of_path: str):
    return JSONResponse(content={"message": "OK"})


# ---------------------------
# HOME API
# ---------------------------

@app.get("/")
def home():
    return {"message": "AI Expense Tracker Backend Running"}


# ---------------------------
# GET ALL EXPENSES
# ---------------------------

@app.get("/expenses")
def get_expenses():

    db: Session = SessionLocal()

    expenses = crud.get_expenses(db)

    result = []

    for e in expenses:
        result.append({
            "category": e.category,
            "amount": e.amount
        })

    return result


# ---------------------------
# CHATBOT API
# ---------------------------

@app.post("/chat")
def chat(data: dict):

    db: Session = SessionLocal()

    message = data.get("message").lower()

    words = message.split()

    # ADD EXPENSE
    if "spent" in words or "cost" in words or "paid" in words:

        try:

            amount = float([w for w in words if w.isdigit()][0])
            category = words[-1]

            crud.create_expense(
                db,
                amount,
                category,
                "chat expense",
                "today"
            )

            return {
                "response": f"Added expense: {amount} for {category}"
            }

        except:
            return {"response": "Could not understand expense"}

    # SHOW EXPENSES
    elif "show" in words:

        expenses = crud.get_expenses(db)

        result = ""

        for e in expenses:
            result += f"{e.category}: {e.amount}\n"

        return {"response": result if result else "No expenses found"}

    # UPDATE LAST EXPENSE
    elif "update" in words:

        try:

            new_amount = float(words[-1])

            updated = crud.update_last_expense(db, new_amount)

            if updated:
                return {"response": f"Updated last expense to {new_amount}"}

            return {"response": "No expense found to update"}

        except:
            return {"response": "Invalid update amount"}

    # DELETE EXPENSE
    elif "delete" in words:

        deleted = crud.delete_last_expense(db)

        if deleted:
            return {
                "response": f"Deleted expense: {deleted.category} {deleted.amount}"
            }

        return {"response": "No expense to delete"}

    # AI INSIGHTS
    elif "insight" in message or "analysis" in message:

        expenses = crud.get_expenses(db)

        total = sum([e.amount for e in expenses])

        categories = {}

        for e in expenses:
            if e.category in categories:
                categories[e.category] += e.amount
            else:
                categories[e.category] = e.amount

        if categories:

            highest = max(categories, key=categories.get)

            return {
                "response":
                f"Total spent {total}. Highest spending category: {highest}"
            }

        return {"response": "No expense data available"}

    # DEFAULT RESPONSE
    else:

        return {
            "response": f"You said: {message}"
        }