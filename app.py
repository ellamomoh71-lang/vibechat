import streamlit as st

st.set_page_config(
    page_title="VibeChat",
    page_icon="💬",
    layout="centered"
)

st.title("💬 VibeChat")
st.subheader("Connect. Chat. Share.")

st.write("Welcome to VibeChat!")

st.divider()

st.header("Get Started")

option = st.radio(
    "Choose an option:",
    ["Create Account", "Login"]
)

if option == "Create Account":
    st.subheader("Create your account")
    username = st.text_input("Choose a username")
    email = st.text_input("Enter your email")
    password = st.text_input("Create password", type="password")

    if st.button("Sign Up"):
        st.success("Welcome to VibeChat!")

elif option == "Login":
    st.subheader("Welcome back!")
    email = st.text_input("Your email")
    password = st.text_input("Your password", type="password")

    if st.button("Login"):
                st.success("Login button clicked!")￼Enter
