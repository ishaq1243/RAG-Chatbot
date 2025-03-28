import streamlit as st

def feedback_page():
    st.title("📨 Feedback Page")
    st.markdown("""
    We value your feedback! Please take a moment to fill out the feedback form below:

    <iframe src="https://docs.google.com/forms/d/e/1FAIpQLSd84Lhz58W2kr1w9FQ6qMQ6zLLHHbKs0__xlGLrvfIQJ-wVNw/viewform?usp=dialog" width="100%" height="700" style="border:none;">Loading…</iframe>
    
    """, unsafe_allow_html=True)
