from dotenv import load_dotenv
load_dotenv()  # loading all the environment variables

import streamlit as st
import os
import google.generativeai as genai

# Configure the generative AI model
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

# Initialize the Gemini model
model = genai.GenerativeModel("gemini-pro")

def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text

def app():
    st.title("Gemini Q&A")

    st.header("Gemini Q&A Application")
    input = st.text_input("Input: ", key="input")

    submit = st.button("Ask Anything")

    # When the submit button is clicked
    if submit:
        response = get_gemini_response(input)
        st.subheader("The Response is: ")
        st.write(response)

