import streamlit as st

def render_history_download():
    if st.session_state.get("message"):
        chat_text="\n\n".join([f"{message['role'].upper()}: {message['content']}" for message in st.session_state.messages])
        st.download_button("Download Chat History", chat_text, file_name="chat_history.txt", mime="text/plain")