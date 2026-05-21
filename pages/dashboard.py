import streamlit as st
import pandas as pd
import plotly.express as px

from database.db import create_connection

def dashboard():

    st.title("Financial Analytics Dashboard")

    conn = create_connection()
    

    query = """
    SELECT category, amount, type, transaction_date
    FROM transactions
    """

    df = pd.read_sql(query, conn)

    if df.empty:
        st.warning("No Transactions Found")
        return

    # Metrics
    total_income = df[df['type'] == 'Income']['amount'].sum()

    total_expense = df[df['type'] == 'Expense']['amount'].sum()

    savings = total_income - total_expense

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(f"""
        <div class="metric-card">
        <h3>Total Income</h3>
        <h2>₹ {total_income:.2f}</h2>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="metric-card">
        <h3>Total Expense</h3>
        <h2>₹ {total_expense:.2f}</h2>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div class="metric-card">
        <h3>Savings</h3>
        <h2>₹ {savings:.2f}</h2>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # Pie Chart
    expense_df = df[df['type'] == 'Expense']

    pie_chart = px.pie(
        expense_df,
        names='category',
        values='amount',
        title='Category Wise Expenses'
    )

    st.plotly_chart(pie_chart, use_container_width=True)

    # Monthly Expense Trend
    df['transaction_date'] = pd.to_datetime(df['transaction_date'])

    df['Month'] = df['transaction_date'].dt.strftime('%B')

    monthly = df.groupby('Month')['amount'].sum().reset_index()

    line_chart = px.line(
        monthly,
        x='Month',
        y='amount',
        title='Monthly Spending Trend',
        markers=True
    )

    st.plotly_chart(line_chart, use_container_width=True)