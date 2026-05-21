import streamlit as st
import bcrypt
from database.db import create_connection

def register_user():

    st.subheader("Register")

    username = st.text_input("Username")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Register"):

        hashed_password = bcrypt.hashpw(
            password.encode('utf-8'),
            bcrypt.gensalt()
        )

        conn = create_connection()
        cursor = conn.cursor(buffered=True)

        query = """
        INSERT INTO users(username, email, password)
        VALUES(%s, %s, %s)
        """

        values = (
            username,
            email,
            hashed_password.decode('utf-8')
        )

        cursor.execute(query, values)

        conn.commit()

        st.success("Registration Successful")