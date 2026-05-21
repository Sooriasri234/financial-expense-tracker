import streamlit as st

from auth.register import register_user
from auth.login import login_user
from pages.add_expense import add_expense
from pages.dashboard import dashboard
from pages.budget import set_budget
from pages.prediction import prediction_page
from pages.financial_insights import financial_insights
def load_css():

    with open("assets/style.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()

st.title("AI Financial Expense Tracker")

menu = [
    "Login",
    "Register",
    "Dashboard",
    "Add Expense",
    "Set Budget",
    "AI Prediction",
    "Financial Insights"
]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Login":
    login_user()

elif choice == "Register":
    register_user()

elif choice == "Add Expense":

    if "token" in st.session_state:
        add_expense()
    else:
        st.warning("Please Login First")

elif choice == "Dashboard":

    if "token" in st.session_state:
        dashboard()
    else:
        st.warning("Please Login First")

elif choice == "Set Budget":

    if "token" in st.session_state:
        set_budget()
    else:
        st.warning("Please Login First")

elif choice == "AI Prediction":

    if "token" in st.session_state:
        prediction_page()
    else:
        st.warning("Please Login First")

elif choice == "Financial Insights":

    if "token" in st.session_state:
        financial_insights()
    else:
        st.warning("Please Login First")