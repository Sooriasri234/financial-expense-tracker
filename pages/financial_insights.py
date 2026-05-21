import streamlit as st
import pandas as pd
from database.db import create_connection


def financial_insights():

    st.title("Smart Financial Insights")

    conn = create_connection()

    query = """
    SELECT
        category,
        amount,
        type,
        transaction_date
    FROM transactions
    """

    df = pd.read_sql(query, conn)

    if df.empty:

        st.warning("No transaction data found")
        return

    # Convert date

    df['transaction_date'] = pd.to_datetime(
        df['transaction_date']
    )

    # Extract month

    df['Month'] = df['transaction_date'].dt.month

    # Current and previous month

    current_month = df['Month'].max()

    previous_month = current_month - 1

    current_df = df[
        df['Month'] == current_month
    ]

    previous_df = df[
        df['Month'] == previous_month
    ]

    # Expenses only

    current_expense = current_df[
        current_df['type'] == 'Expense'
    ]

    previous_expense = previous_df[
        previous_df['type'] == 'Expense'
    ]

    st.subheader("Monthly Financial Analysis")

    categories = current_expense['category'].unique()

    for category in categories:

        current_total = current_expense[
            current_expense['category'] == category
        ]['amount'].sum()

        previous_total = previous_expense[
            previous_expense['category'] == category
        ]['amount'].sum()

        if previous_total > 0:

            percentage_change = (
                (
                    current_total - previous_total
                ) / previous_total
            ) * 100

            # Increased

            if percentage_change > 0:

                st.warning(
                    f"{category} expenses increased by "
                    f"{percentage_change:.2f}% "
                    f"compared to last month."
                )

            # Decreased

            elif percentage_change < 0:

                st.success(
                    f"{category} expenses decreased by "
                    f"{abs(percentage_change):.2f}% "
                    f"compared to last month."
                )

    # Highest spending category

    highest_category = current_expense.groupby(
        'category'
    )['amount'].sum().idxmax()

    highest_amount = current_expense.groupby(
        'category'
    )['amount'].sum().max()

    st.error(
        f"Highest spending category this month: "
        f"{highest_category} "
        f"(₹ {highest_amount:.2f})"
    )

    # Savings analysis

    current_income = current_df[
        current_df['type'] == 'Income'
    ]['amount'].sum()

    current_expense_total = current_expense[
        'amount'
    ].sum()

    savings = current_income - current_expense_total

    st.info(
        f"Estimated Savings This Month: "
        f"₹ {savings:.2f}"
    )

    # Financial recommendation

    if highest_amount > 10000:

        st.warning(
            f"Recommendation: Try reducing "
            f"{highest_category} expenses "
            f"to improve savings."
        )

    else:

        st.success(
            "Your financial management looks healthy."
        )