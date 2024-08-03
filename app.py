import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

# Configure the Generative AI model
api_key = os.getenv("GOOGLE_API_KEY")
if api_key:
    genai.configure(api_key=api_key)
else:
    st.error("API key not found. Please set the GOOGLE_API_KEY in the .env file.")

# Define the function to get the Gemini response
def get_gemini_response(question):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(question)
    return response.text

# Streamlit app configuration
st.set_page_config(page_title="Q&A Demo", page_icon="🧠", layout="wide")
st.title("🌟 Gemini LLM Q&A Application")
st.markdown("""
    <style>
    .stApp {
        background-color: black;
    }
    .stButton button {
        background-color: #4CAF50;
        color: white;
        border: none;
        padding: 10px 24px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        transition-duration: 0.4s;
        cursor: pointer;
        border-radius: 12px;
    }
    .stButton button:hover {
        background-color: white;
        color: black;
        border: 2px solid #4CAF50;
    }
    .header {
        text-align: center;
        padding: 50px;
        font-family: Arial, sans-serif;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='header'><h1>Welcome to the Gemini Q&A Demo</h1><p>Ask anything and get responses from the advanced Gemini language model!</p></div>", unsafe_allow_html=True)

# Input and submit button
input_text = st.text_input("Type your question here:", key="input")
submit = st.button("Ask the Question")

# Display the response if the button is clicked
if submit and input_text:
    response = get_gemini_response(input_text)
    st.subheader("The Response is")
    st.write(response)
else:
    st.write("Please enter a question and click the button to get a response.")

