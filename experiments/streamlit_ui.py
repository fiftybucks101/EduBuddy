import streamlit as st

# Sidebar navigation
page = st.sidebar.radio("Navigate", ["Login", "Signup"])

if page == "Login":
    st.title("Login")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        # Add your login logic here
        st.success("Logged in successfully!")  # Placeholder

elif page == "Signup":
    st.title("Signup")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    role = st.selectbox("Role", ["student", "teacher"])
    if st.button("Signup"):
        # Add your signup logic here
        st.success("Signed up successfully!")  # Placeholder