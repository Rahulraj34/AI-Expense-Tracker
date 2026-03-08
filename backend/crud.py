from sqlalchemy.orm import Session
import models


# --------------------------
# EXPENSE FUNCTIONS
# --------------------------

def create_expense(db: Session, amount, category, description, date):

    expense = models.Expense(
        amount=amount,
        category=category,
        description=description,
        date=date
    )

    db.add(expense)
    db.commit()
    db.refresh(expense)

    return expense


def get_expenses(db: Session):

    return db.query(models.Expense).all()


def update_last_expense(db: Session, new_amount):

    expense = db.query(models.Expense).order_by(models.Expense.id.desc()).first()

    if expense:

        expense.amount = new_amount

        db.commit()

        return expense

    return None


def delete_last_expense(db: Session):

    expense = db.query(models.Expense).order_by(models.Expense.id.desc()).first()

    if expense:

        db.delete(expense)

        db.commit()

        return expense

    return None


# --------------------------
# BUDGET FUNCTIONS
# --------------------------

def set_budget(db: Session, category, limit):

    budget = models.Budget(
        category=category,
        limit=limit
    )

    db.add(budget)

    db.commit()

    db.refresh(budget)

    return budget


def get_budgets(db: Session):

    return db.query(models.Budget).all()


# --------------------------
# ANALYTICS FUNCTIONS
# --------------------------

def get_total_spending(db: Session):

    expenses = db.query(models.Expense).all()

    total = sum([e.amount for e in expenses])

    return total


def get_category_spending(db: Session):

    expenses = db.query(models.Expense).all()

    category_totals = {}

    for e in expenses:

        if e.category in category_totals:

            category_totals[e.category] += e.amount

        else:

            category_totals[e.category] = e.amount

    return category_totals