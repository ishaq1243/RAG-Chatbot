import streamlit as st
import os
import shutil
import pandas as pd
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama_index.core.settings import Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.gemini import Gemini
import google.generativeai as genai
from dotenv import load_dotenv

# Loading API key from .env 
load_dotenv()
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

UPLOAD_DIR = "uploaded_files"

# Creating upload dir if it doesn't exist
os.makedirs(UPLOAD_DIR, exist_ok=True)

def delete_all_files():
    if os.path.exists(UPLOAD_DIR):
        shutil.rmtree(UPLOAD_DIR)
        os.makedirs(UPLOAD_DIR)
    for key in ["uploaded_files", "query_engine", "embedded_index", "llm"]:
        st.session_state.pop(key, None)
    st.success("All uploaded files and session data cleared.")

def upload_page():
    st.title("📤 Upload Files")
    st.markdown("Upload PDF, DOCX, CSV, XLSX, or XML files. You can query these in the Chat Page.")

    uploaded_files = st.file_uploader(
        "Choose your file(s):", 
        type=["pdf", "docx", "csv", "xlsx", "xml"], 
        accept_multiple_files=True
    )

    if uploaded_files:
        st.session_state.uploaded_files = []
        for file in uploaded_files:
            file_path = os.path.join(UPLOAD_DIR, file.name)
            with open(file_path, "wb") as f:
                f.write(file.getbuffer())
            st.session_state.uploaded_files.append(file_path)

        st.success("Files uploaded successfully!")

        # Loading embedding and Gemini LLM
        embed_model = HuggingFaceEmbedding(model_name="sentence-transformers/all-MiniLM-L6-v2")

        llm = Gemini(
            model="models/gemini-2.0-flash",  
            temperature=0.3,
            max_tokens=512
        )

        # Registering models globally
        Settings.llm = llm
        Settings.embed_model = embed_model

        # Processing documents
        docs = SimpleDirectoryReader(UPLOAD_DIR).load_data()
        index = VectorStoreIndex.from_documents(docs)
        query_engine = index.as_query_engine()

        st.session_state.query_engine = query_engine
        st.session_state.embedded_index = index
        st.session_state.llm = llm

        st.info("Embedding and indexing complete. Head to the Chat Page to ask questions!")

    if st.button("🗑️ Delete All Uploaded Files"):
        delete_all_files()

    if "uploaded_files" in st.session_state:
        st.markdown("### Uploaded Files")
        for f in st.session_state.uploaded_files:
            st.write(f)
