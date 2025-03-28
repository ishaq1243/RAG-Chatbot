import streamlit as st
from upload import upload_page
from chat import chat_page
from feedback import feedback_page

st.set_page_config(page_title="RAG Chatbot", layout="wide")

# Sidebar for navigation
PAGES = {
    "Upload Page": upload_page,
    "Chat Page": chat_page,
    "Feedback Page": feedback_page
}

st.sidebar.title("🔍 Navigation")
selected_page = st.sidebar.radio("Go to", list(PAGES.keys()))

# Page rendering
PAGES[selected_page]()
