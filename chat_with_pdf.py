import os
import tempfile
import streamlit as st
from embedchain import App
import base64
from streamlit_chat import message

st.title("Chat with PDF using Llama 3.2")
st.caption("This app allows you to chat with a PDF using Llama 3.2 running locally with Ollama!")
