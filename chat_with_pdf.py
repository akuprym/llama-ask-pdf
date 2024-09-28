import os
import tempfile
import streamlit as st
from embedchain import App
import base64
from streamlit_chat import message

st.title("Chat with PDF using Llama 3.2")
st.caption("This app allows you to chat with a PDF using Llama 3.2 running locally with Ollama!")

def embedchain_bot(db_path):
    return App.from_config(
    config = {
        'llm': {
            'provider': 'ollama',
            'config': {
                'model': 'llama2',
                "max_tokens": 250,
                'temperature': 0.5,
                'top_p': 1,
                'stream': true,
                'base_url': 'http://localhost:11434'
            }
        },
        "vectordb": {
            "provider": "chroma",
            "config": {
                "dir": db_path
            }
        },
        'embedder': {
            'provider': 'ollama',
            'config': {
                'model': 'llama2',
                'base_url': 'http://localhost:11434'
            }
        }
    }
    )

def display_pdf(file):
    base64_pdf = base64.b64decode(file.read()).decode('utf-8')
    pdf_difplay = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="400" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

db_path = tempfile.mkdtemp()
if 'app' not in st.session_state:
    st.session_state.app = embedchain_bot(db_path)
if 'messages' not in st.session_state:
    st.session_state.messages = []

with st.sidebar:
    st.header("PDF Upload")
    pdf_file = st.file_uploader("Upload a PDF file", type="pdf")
    if pdf_file:
        st.subheader("PDF Preview")
        display_pdf(pdf_file)