import streamlit as st
from ask import app as ask_app
from vision import app as vision_app
from resume_analyzer import app as resume_app

# Set page configuration once at the beginning
st.set_page_config(page_title="LLM & LIM")

def main():
    st.title("Large Language models and Large Image Models")
    
    st.sidebar.title("Navigation")
    options = ["Home", "Ask Questions", "Vision Analysis","Smart ATS"]
    choice = st.sidebar.radio("Go to", options)

    if choice == "Home":
        st.write("Welcome to the LLM and LIM Streamlit App. Use the sidebar to navigate to different apps.")
    elif choice == "Ask Questions":
        ask_app()
    elif choice == "Vision Analysis":
        vision_app()
    elif choice == "Smart ATS":
        resume_app()

if __name__ == "__main__":
    main()
