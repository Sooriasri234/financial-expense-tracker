import streamlit as st
import joblib
import pandas as pd
import plotly.express as px

def prediction_page():

    st.title("AI Expense Prediction")

    model = joblib.load(
        "ml/expense_prediction_model.pkl"
    )

    month = st.slider(
        "Select Future Month",
        1,
        12,
        6
    )

    prediction = model.predict([[month]])

    st.success(
        f"Predicted Expense for Month {month}: ₹ {prediction[0]:.2f}"
    )

    # Prediction chart

    months = list(range(1, 13))

    predictions = model.predict(
        pd.DataFrame(months, columns=['Month'])
    )

    chart_df = pd.DataFrame({
        "Month": months,
        "Predicted Expense": predictions
    })

    fig = px.line(
        chart_df,
        x="Month",
        y="Predicted Expense",
        markers=True,
        title="Future Expense Forecast"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )