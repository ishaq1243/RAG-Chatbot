# Welcome to the RAG-based Question Answering System

An AI-powered question-answering chatbot built using Retrieval-Augmented Generation (RAG) with Google Generative AI Gemini Model and Streamlit. This application allows users to upload documents in multiple formats and get precise answers to their queries using AI.

## Features

### Document-Powered Chatbot:
- Provides accurate answers strictly based on the content of uploaded documents.
- Supports document formats including PDF, DOCX, CSV, XLSX, and XML.
- Uses RAG to retrieve relevant information and generate context-aware responses.

### Secure File Management:
- Files are stored temporarily during the session.
- Option to delete uploaded files to ensure privacy.

### Easy File Upload:
- Simple drag-and-drop file upload system.
- Displays uploaded files for verification.

### Intuitive Chat Interface:
- Streamlit-powered responsive design.
- Real-time interaction with AI responses.
- Provides system messages for clarification when queries are vague.

### User Feedback Collection:
- Built-in feedback form powered by Google Forms.
- Allows users to rate their experience and suggest improvements.

## Tech Stack
- **Frontend:** Streamlit
- **AI Model:** Google Generative AI Gemini Model
- **Embedding Model:** Sentence-Transformers (all-MiniLM-L6-v2)
- **Document Parsing:** PyMuPDF, python-docx, pandas, lxml
- **RAG Framework:** LlamaIndex

## Supported File Types
- PDF (.pdf)
- Word Document (.docx)
- Excel (.xlsx)
- CSV (.csv)
- XML (.xml)

## How to Use
1. **Upload Files:** Go to the **Upload Page** and upload documents.
2. **Chat with AI:** Navigate to the **Chat Page** and ask questions based on the uploaded documents.
3. **Provide Feedback:** After using the chatbot, go to the **Feedback Page** and submit your experience.

## Disclaimer
- The chatbot only provides responses based on the uploaded files.
- It is not designed to provide general knowledge or information beyond the uploaded content.
- Ensure sensitive data is handled responsibly, as the application does not store files permanently.
