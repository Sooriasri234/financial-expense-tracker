import streamlit as st
from streamlit_oauth import OAuth2Component
import jwt

CLIENT_ID = st.secrets["GOOGLE_CLIENT_ID"]
CLIENT_SECRET = st.secrets["GOOGLE_CLIENT_SECRET"]

AUTHORIZE_URL = "https://accounts.google.com/o/oauth2/auth"
TOKEN_URL = "https://oauth2.googleapis.com/token"
REFRESH_TOKEN_URL = "https://oauth2.googleapis.com/token"
REVOKE_TOKEN_URL = "https://oauth2.googleapis.com/revoke"

oauth2 = OAuth2Component(
    CLIENT_ID,
    CLIENT_SECRET,
    AUTHORIZE_URL,
    TOKEN_URL,
    REFRESH_TOKEN_URL,
    REVOKE_TOKEN_URL,
)

def google_login():

    result = oauth2.authorize_button(
        name="Continue with Google",
        redirect_uri="https://financial-expense-tracker-5twxsfnmjp5trvrtoy5tdt.streamlit.app/",
        scope="openid email profile",
        key="google",
    )

    if result and "token" in result:

        token = result["token"]

        user_info = jwt.decode(
            token["id_token"],
            options={"verify_signature": False}
        )

        st.session_state["logged_in"] = True
        st.session_state["username"] = user_info["name"]
        st.session_state["email"] = user_info["email"]

        st.success("Google Login Successful ✅")

        st.write(f"Welcome {user_info['name']}")
        st.write(f"Email: {user_info['email']}")

        st.image(user_info['picture'], width=120)