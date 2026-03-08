from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from database import engine, SessionLocal
import models
import crud

app = FastAPI()

# create tables
models.Base.metadata.create_all(bind=engine)

# CORS settings
origins = [
    "http://localhost:5173",
    "https://ai-expense-tracker-beta-eight.vercel.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# context memory
last_expense = None


@app.get("/")
def home():
    return {"message": "AI Expense Tracker Backend Running"}


# -------------------------
# GET ALL EXPENSES
# -------------------------
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


# -------------------------
# CHATBOT API
# -------------------------
@app.post("/chat")
def chat(data: dict):

    global last_expense

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

            last_expense = amount

            return {
                "response": f"Added expense: {amount} for {category}"
            }

        except:
            return {"response": "Could not understand the expense."}

    # SHOW EXPENSES
    elif "show" in words:

        expenses = crud.get_expenses(db)

        result = ""

        for e in expenses:
            result += f"{e.category}: {e.amount}\n"

        return {
            "response": result if result else "No expenses found"
        }

    # UPDATE LAST EXPENSE
    elif "update" in words:

        try:

            new_amount = float(words[-1])

            updated = crud.update_last_expense(db, new_amount)

            if updated:
                return {
                    "response": f"Updated last expense to {new_amount}"
                }

            return {"response": "No expense to update"}

        except:
            return {"response": "Invalid update amount"}

    # DELETE LAST EXPENSE
    elif "delete" in words:

        deleted = crud.delete_last_expense(db)

        if deleted:
            return {
                "response": f"Deleted expense: {deleted.category} {deleted.amount}"
            }

        return {"response": "No expense to delete"}

    # CONTEXT AWARENESS
    elif "make that" in message:

        try:

            new_amount = float(words[-1])

            updated = crud.update_last_expense(db, new_amount)

            return {
                "response": f"Updated last expense to {new_amount}"
            }

        except:
            return {"response": "Context update failed"}

    # INSIGHTS
    elif "insight" in message or "analysis" in message:

        expenses = crud.get_expenses(db)

        total = sum([e.amount for e in expenses])

        category_totals = {}

        for e in expenses:

            if e.category in category_totals:
                category_totals[e.category] += e.amount
            else:
                category_totals[e.category] = e.amount

        if category_totals:

            highest = max(category_totals, key=category_totals.get)

            return {
                "response":
                f"Total spent {total}. Highest spending category: {highest}"
            }

        return {"response": "No spending data yet"}

    # FOOD QUERY
    elif "food" in message and "spend" in message:

        expenses = crud.get_expenses(db)

        total = sum([e.amount for e in expenses if e.category == "food"])

        return {
            "response": f"You spent {total} on food"
        }

    # DEFAULT RESPONSE
    else:

        return {
            "response": f"You said: {message}"
        }