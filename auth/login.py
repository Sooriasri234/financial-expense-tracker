import streamlit as st
import bcrypt

from database.db import create_connection
from auth.jwt_handler import generate_token

def login_user():

    st.subheader("Login")

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):

        conn = create_connection()
        cursor = conn.cursor()

        query = "SELECT * FROM users WHERE email=%s"

        cursor.execute(query, (email,))

        user = cursor.fetchone()

        if user:

            stored_password = user[3]

            if bcrypt.checkpw(
                password.encode('utf-8'),
                stored_password.encode('utf-8')
            ):

                token = generate_token(email)

                st.session_state.token = token
                st.session_state.user_id = user[0]

                st.success("Login Successful")

            else:
                st.error("Invalid Password")

        else:
            st.error("User Not Found")