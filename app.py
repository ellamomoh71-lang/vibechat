import streamlit as st

st.set_page_config(
    page_title="VibeChat",
    page_icon="💬"
)

st.title("💬 VibeChat")
st.caption("Connect. Chat. Share.")

if "messages" not in st.session_state:
    st.session_state.messages = []

if "username" not in st.session_state:
    st.session_state.username = ""

if not st.session_state.username:
    st.subheader("Welcome to VibeChat!")

    name = st.text_input("What should we call you?")

    if st.button("Enter Chat"):
        if name.strip():
            st.session_state.username = name.strip()
            st.rerun()
        else:
            st.warning("Please enter your name.")

else:
    st.sidebar.title("Your Profile")
    st.sidebar.write(
        "👤 " + st.session_state.username
    )

    if st.sidebar.button("Logout"):
        st.session_state.username = ""
        st.rerun()

    st.subheader("💬 Your Chat Room")

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    new_message = st.chat_input("Type a message...")

    if new_message:
        st.session_state.messages.append({
            "role": "user",
            "content": new_message
        })
        st.rerun
