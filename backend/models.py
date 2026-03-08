from sqlalchemy import Column, Integer, String, Float
from database import Base


# Expense Table

class Expense(Base):

    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index=True)

    amount = Column(Float)

    category = Column(String)

    description = Column(String)

    date = Column(String)


# Budget Table

class Budget(Base):

    __tablename__ = "budgets"

    id = Column(Integer, primary_key=True, index=True)

    category = Column(String)

    limit = Column(Float)


# User Table (for login)

class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    username = Column(String, unique=True)

    password = Column(String)