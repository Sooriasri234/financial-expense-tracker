import streamlit as st

from auth.google_auth import google_login
from auth.register import register_user
from auth.login import login_user

from pages.add_expense import add_expense
from pages.dashboard import dashboard
from pages.budget import set_budget
from pages.prediction import prediction_page
from pages.financial_insights import financial_insights


# ---------------- LOAD CSS ---------------- #

def load_css():

    with open("assets/style.css") as f:

        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )


load_css()


# ---------------- PAGE TITLE ---------------- #

st.title("AI Financial Expense Tracker")


# ---------------- SESSION STATE ---------------- #

if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False


# ---------------- MENU ---------------- #

menu = [
    "Login",
    "Register",
    "Google Login",
    "Dashboard",
    "Add Expense",
    "Set Budget",
    "AI Prediction",
    "Financial Insights"
]

choice = st.sidebar.selectbox("Menu", menu)


# ---------------- LOGIN ---------------- #

if choice == "Login":

    login_user()


# ---------------- REGISTER ---------------- #

elif choice == "Register":

    register_user()


# ---------------- GOOGLE LOGIN ---------------- #

elif choice == "Google Login":

    google_login()


# ---------------- DASHBOARD ---------------- #

elif choice == "Dashboard":

    if st.session_state.get("logged_in"):

        dashboard()

    else:

        st.warning("Please Login First")


# ---------------- ADD EXPENSE ---------------- #

elif choice == "Add Expense":

    if st.session_state.get("logged_in"):

        add_expense()

    else:

        st.warning("Please Login First")


# ---------------- SET BUDGET ---------------- #

elif choice == "Set Budget":

    if st.session_state.get("logged_in"):

        set_budget()

    else:

        st.warning("Please Login First")


# ---------------- AI PREDICTION ---------------- #

elif choice == "AI Prediction":

    if st.session_state.get("logged_in"):

        prediction_page()

    else:

        st.warning("Please Login First")


# ---------------- FINANCIAL INSIGHTS ---------------- #

elif choice == "Financial Insights":

    if st.session_state.get("logged_in"):

        financial_insights()

    else:

        st.warning("Please Login First")