# app.py
import streamlit as st
from auth import authenticate_user, authenticate_admin
from user_dashboard import display_user_dashboard
from admin_dashboard import display_admin_dashboard

def main():
    st.title("GrowthGen App")

    # Sidebar with login forms
    st.sidebar.header("Login")

    login_option = st.sidebar.radio("Select login type:", ["User", "Admin"])

    if login_option == "User":
        username = st.sidebar.text_input("Username")
        password = st.sidebar.text_input("Password", type="password")

        if st.sidebar.button("Login"):
            if authenticate_user(username, password):
                st.sidebar.success("Login successful as User!")
                display_user_dashboard()
            else:
                st.error("Invalid credentials!")

    elif login_option == "Admin":
        username = st.sidebar.text_input("Username")
        password = st.sidebar.text_input("Password", type="password")

        if st.sidebar.button("Login"):
            if authenticate_admin(username, password):
                st.sidebar.success("Login successful as UserAdmin!")
                display_admin_dashboard()
            else:
                st.error("Invalid credentials!")

if __name__ == "__main__":
    main()
