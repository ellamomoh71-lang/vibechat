
import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="VibeChat",
    page_icon="💬",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.title("💬 VibeChat")
st.caption("Connect. Chat. Share.")

if "messages" not in st.session_state:
    st.session_state.messages = []

if "username" not in st.session_state:
    st.session_state.username = ""

if "profile_pic" not in st.session_state:
    st.session_state.profile_pic = None

if not st.session_state.username:
    st.subheader("Welcome to VibeChat!")

    name = st.text_input("Choose your username")

    picture = st.file_uploader(
        "Upload your profile picture",
        type=["png", "jpg", "jpeg"]
    )

    if st.button("Enter Chat"):
        if name.strip():
            st.session_state.username = name.strip()
            st.session_state.profile_pic = picture
            st.rerun()
        else:
            st.warning("Please enter your username.")

else:
    st.sidebar.title("Your Profile")
    st.sidebar.write(st.session_state.username)

    if st.session_state.profile_pic:
        st.sidebar.image(
            st.session_state.profile_pic,
            width=120
        )
    else:
        st.sidebar.write("👤 No profile picture")

    if st.sidebar.button("Logout"):
        st.session_state.username = ""
        st.session_state.profile_pic = None
        st.rerun()

    st.subheader("💬 Chat Room")

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])
            st.caption(message["time"])

    new_message = st.chat_input("Type a message...")

    if new_message:
        current_time = datetime.now().strftime("%I:%M %p")

        st.session_state.messages.append({
            "role": "user",
            "content": new_message,
            "time": current_time
        })

        st.rerun()

