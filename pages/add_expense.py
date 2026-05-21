import streamlit as st
from database.db import create_connection
from alerts.smtp_mail import send_budget_alert
from datetime import datetime, date


def add_expense():

    st.title("Add Transaction")

    # ---------------- FORM ---------------- #

    amount = st.number_input(
        "Amount",
        min_value=0.0,
        step=100.0
    )

    category = st.selectbox(
        "Category",
        [
            "Food & Drink",
            "Utilities",
            "Rent",
            "Investment",
            "Shopping",
            "Entertainment",
            "Health & Fitness",
            "Salary",
            "Travel",
            "Other"
        ]
    )

    transaction_type = st.selectbox(
        "Transaction Type",
        ["Expense", "Income"]
    )

    description = st.text_area(
        "Transaction Description"
    )

    transaction_date = st.date_input(
        "Transaction Date",
        date.today()
    )

    # ---------------- ADD BUTTON ---------------- #

    if st.button("Add Transaction"):

        try:

            conn = create_connection()
            cursor = conn.cursor(buffered=True)

            # ---------------- INSERT TRANSACTION ---------------- #

            insert_query = """
            INSERT INTO transactions
            (
                user_id,
                transaction_date,
                description,
                category,
                amount,
                type
            )
            VALUES (%s, %s, %s, %s, %s, %s)
            """

            values = (
                st.session_state.user_id,
                transaction_date,
                description,
                category,
                amount,
                transaction_type
            )

            cursor.execute(insert_query, values)

            conn.commit()

            st.success("Transaction Added Successfully")

            # ---------------- BUDGET ALERT LOGIC ---------------- #

            current_month = datetime.now().strftime("%B")
            current_year = datetime.now().year

            # Get monthly budget

            budget_query = """
            SELECT monthly_budget
            FROM budgets
            WHERE user_id = %s
            AND month = %s
            AND year = %s
            """

            cursor.execute(
                budget_query,
                (
                    st.session_state.user_id,
                    current_month,
                    current_year
                )
            )

            budget_result = cursor.fetchone()

            # If budget exists

            if budget_result:

                monthly_budget = budget_result[0]

                # Calculate total expenses

                expense_query = """
                SELECT SUM(amount)
                FROM transactions
                WHERE user_id = %s
                AND type = 'Expense'
                """

                cursor.execute(
                    expense_query,
                    (st.session_state.user_id,)
                )

                total_expense = cursor.fetchone()[0]

                if total_expense is None:
                    total_expense = 0

                # Calculate percentage used

                budget_usage = (
                    total_expense / monthly_budget
                ) * 100

                # Get user email

                email_query = """
                SELECT email
                FROM users
                WHERE id = %s
                """

                cursor.execute(
                    email_query,
                    (st.session_state.user_id,)
                )

                user_email = cursor.fetchone()[0]

                # ---------------- WARNING ALERT ---------------- #

                if budget_usage >= 80 and budget_usage < 100:

                    subject = "Budget Warning Alert"

                    body = f"""
Hello User,

You have used {budget_usage:.2f}% of your monthly budget.

Monthly Budget : ₹{monthly_budget}
Current Expense: ₹{total_expense}

Please monitor your spending carefully.

Thank You,
AI Financial Expense Tracker
"""

                    send_budget_alert(
                        user_email,
                        subject,
                        body
                    )

                    st.warning(
                        "Warning: Budget usage exceeded 80%"
                    )

                # ---------------- EXCEEDED ALERT ---------------- #

                elif budget_usage >= 100:

                    subject = "Budget Exceeded Alert"

                    body = f"""
Hello User,

Your monthly budget has been exceeded.

Monthly Budget : ₹{monthly_budget}
Current Expense: ₹{total_expense}

Please reduce unnecessary spending.

Thank You,
AI Financial Expense Tracker
"""

                    send_budget_alert(
                        user_email,
                        subject,
                        body
                    )

                    st.error(
                        "Budget Exceeded!"
                    )

        except Exception as e:

            st.error(f"Error: {e}")