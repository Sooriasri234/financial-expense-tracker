from database.db import create_connection

conn = create_connection()

cursor = conn.cursor()

# USERS TABLE

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(100),
    email VARCHAR(100),
    password VARCHAR(300)
)
""")

# TRANSACTIONS TABLE

cursor.execute("""
CREATE TABLE IF NOT EXISTS transactions (
    transaction_id SERIAL PRIMARY KEY,
    user_id INTEGER,
    transaction_date DATE,
    description TEXT,
    category VARCHAR(100),
    amount FLOAT,
    type VARCHAR(20)
)
""")

# BUDGET TABLE

cursor.execute("""
CREATE TABLE IF NOT EXISTS budgets (
    budget_id SERIAL PRIMARY KEY,
    user_id INTEGER,
    monthly_budget FLOAT,
    month VARCHAR(30),
    year INTEGER
)
""")

conn.commit()

print("Tables Created Successfully")