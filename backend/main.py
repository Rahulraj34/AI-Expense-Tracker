from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from database import engine, SessionLocal
import models
import crud

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

origins = ["http://localhost:5173"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

last_expense_context = None


@app.get("/")
def home():
    return {"message": "AI Expense Tracker Running"}


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


@app.post("/chat")
def chat(data: dict):

    global last_expense_context

    db: Session = SessionLocal()

    message = data.get("message").lower()

    words = message.split()

    # ADD EXPENSE

    if "spent" in words or "cost" in words or "paid" in words:

        try:

            amount = float([w for w in words if w.isdigit()][0])
            category = words[-1]

            crud.create_expense(db, amount, category, "chat", "today")

            last_expense_context = {"amount": amount, "category": category}

            return {"response": f"Added expense: {amount} for {category}"}

        except:
            return {"response": "Could not understand expense"}

    # SHOW EXPENSES

    elif "show" in words:

        expenses = crud.get_expenses(db)

        result = ""

        for e in expenses:
            result += f"{e.category}: {e.amount}\n"

        return {"response": result}

    # DELETE

    elif "delete" in words:

        deleted = crud.delete_last_expense(db)

        if deleted:
            return {"response": f"Deleted {deleted.category} {deleted.amount}"}

        return {"response": "Nothing to delete"}

    # UPDATE

    elif "update" in words:

        try:

            amount = float(words[-1])

            updated = crud.update_last_expense(db, amount)

            return {"response": f"Updated expense to {amount}"}

        except:

            return {"response": "Update failed"}

    # CONTEXT AWARENESS

    elif "make that" in message:

        if last_expense_context:

            try:

                amount = float(words[-1])

                crud.update_last_expense(db, amount)

                return {"response": f"Updated last expense to {amount}"}

            except:
                pass

    # BUDGET

    elif "budget" in words:

        try:

            amount = float([w for w in words if w.isdigit()][0])
            category = words[-1]

            crud.set_budget(db, category, amount)

            return {"response": f"Budget set: {category} = {amount}"}

        except:
            return {"response": "Budget command failed"}

    # INSIGHTS

    elif "insight" in message or "analysis" in message:

        expenses = crud.get_expenses(db)

        total = sum([e.amount for e in expenses])

        categories = {}

        for e in expenses:

            categories[e.category] = categories.get(e.category, 0) + e.amount

        highest = max(categories, key=categories.get)

        return {
            "response":
            f"Total spent {total}. Highest category: {highest}"
        }

    # FOOD QUERY

    elif "food" in message and "spend" in message:

        expenses = crud.get_expenses(db)

        total = sum([e.amount for e in expenses if e.category == "food"])

        return {"response": f"You spent {total} on food"}

    return {"response": "I didn't understand that"}