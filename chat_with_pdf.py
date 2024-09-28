import os
import tempfile
import streamlit as st
from embedchain import App
import base64
from streamlit_chat import message

st.title("Chat with PDF using Llama 3.2")
st.caption("This app allows you to chat with a PDF using Llama 3.2 running locally with Ollama!")

def embedchain_bot(dn_path):
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
