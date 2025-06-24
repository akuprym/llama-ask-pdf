# Introduction

A Python application that lets you get insights from a PDF document using Llama 3.2, running locally with Ollama. You can ask questions about your PDF, and the application will provide relevant responses based on the content of the document. This app utilizes a language model to generate accurate answers to your queries. 

## Features
- Upload PDF documents
- Chat interface for asking questions about the PDF content
- Local processing with Ollama (requires local Ollama server)
- Persistent chat history during session

## Prerequisites
- Python 3.8+
- Ollama installed and running locally (with Llama 3.2 model downloaded)

## Installation
1. Clone this repository
2. Install the requirements:
   ```
   pip install -r requirements.txt
   ```
3. Make sure Ollama is running:
   ```
    ollama serve
   ```
# Usage
1. Run the application:
   ```
    streamlit run app.py
   ```
2. Upload a PDF file through the sidebar.
3. Click "Add to Knowledge Base" to process the PDF:
<img width="1440" alt="Screenshot 2024-10-08 at 03 21 11" src="https://github.com/user-attachments/assets/2d3a6d63-e9e0-4c6a-84f8-79b3d0de45f7">

4. Start asking questions in the chat interface:
<img width="1440" alt="Screenshot 2024-10-08 at 03 37 30" src="https://github.com/user-attachments/assets/2201a307-b934-43c2-a500-06a76ee2ac39">

# Important Notes
Before running the app, make sure you have Ollama installed and running locally with:
   ```
    ollama serve
   ```
You'll need to pull the Llama 3.2 model:
   ```
    ollama pull llama3.2
   ```
The app assumes Ollama is running at http://localhost:11434 (default port)
## To run the application:
1. Save your code as app.py
2. Install dependencies with pip install -r requirements.txt
3. Run with streamlit run app.py

The application will create temporary directories for the ChromaDB vector storage during each session, and will clean them up automatically when the session ends.
