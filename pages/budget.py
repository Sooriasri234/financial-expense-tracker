import streamlit as st
from database.db import create_connection
from datetime import datetime

def set_budget():

    st.subheader("Set Monthly Budget")

    budget = st.number_input(
        "Enter Monthly Budget",
        min_value=0.0
    )

    current_month = datetime.now().strftime("%B")
    current_year = datetime.now().year

    if st.button("Save Budget"):

        conn = create_connection()
        cursor = conn.cursor(buffered=True)

        query = """
        INSERT INTO budgets
        (
            user_id,
            monthly_budget,
            month,
            year
        )
        VALUES (%s, %s, %s, %s)
        """

        values = (
            st.session_state.user_id,
            budget,
            current_month,
            current_year
        )

        cursor.execute(query, values)

        conn.commit()

        st.success("Budget Saved Successfully")