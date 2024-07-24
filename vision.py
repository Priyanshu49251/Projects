from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env.
import streamlit as st
import os
from PIL import Image
import google.generativeai as genai
def app():
    st.title("Gemini Vision Analysis")

    # Load API key from environment variable
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

    def get_gemini_response(input, image):
        model = genai.GenerativeModel('gemini-pro-vision')
        try:
            if input:
                response = model.generate_content([input, image])
            else:
                response = model.generate_content(image)
            # Check if response has valid content
            if hasattr(response, 'text'):
                return response.text
            else:
                return "No valid response received. Please check the input and try again."
        except ValueError as e:
            # Handle any value errors that occur
            return f"An error occurred: {str(e)}"

    st.header("Gemini Vision Analysis Application")
    input = st.text_input("Input Prompt: ", key="input")
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    image = None
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image.", use_column_width=True)
    else:
        st.write("Please give an input image.")

    submit = st.button("Tell me about the image")

    if submit:
        if image is not None:
            response = get_gemini_response(input, image)
            st.subheader("The Response is")
            st.write(response)
        else:
            st.write("Please upload an image to get a response.")

