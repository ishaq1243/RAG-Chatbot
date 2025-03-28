import streamlit as st
from llama_index.core.llms import ChatMessage

def chat_page():
    st.title("💬 Chat Page")

    if "query_engine" not in st.session_state:
        st.warning("Please upload and process your files first in the Upload Page.")
        return

    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "Hi! Ask me anything based on your uploaded files."}
        ]

    # Clear Chat History 
    if st.button("🗑️ Clear Chat History"):
        st.session_state.messages = [
            {"role": "assistant", "content": "Hi! Ask me anything based on your uploaded files."}
        ]
        st.success("Chat history cleared!")

    def strict_response(prompt):
        if not st.session_state.uploaded_files:
            return "No files found. Please upload supported documents first."

        valid_exts = (".csv", ".xlsx", ".xml", ".pdf", ".docx")
        if not any(file.endswith(valid_exts) for file in st.session_state.uploaded_files):
            return "Unsupported file type."

        # Clarify question if vague
        vague_keywords = ["data", "table", "document", "file"]
        if any(k in prompt.lower() for k in vague_keywords):
            prompt += "\n[System note: Please specify if you're referring to a spreadsheet (csv/xlsx/xml) or a document (pdf/docx).]"

        try:
            response = st.session_state.query_engine.query(prompt)
        except Exception:
            response = "Sorry, I can only answer questions strictly based on your uploaded files."

        return str(response)

    prompt = st.chat_input("Ask your question...")

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = strict_response(prompt)
                st.markdown(response)
                st.session_state.messages.append({"role": "assistant", "content": response})
