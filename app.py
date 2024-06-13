# chatbot_streamlit.py

import streamlit as st
from bot import get_response

def main():
    st.title("Nutrition Bot")

    # Streamlit UI
    prompt = st.text_input("You: ")

    if st.button("Send"):
        response = get_response(prompt)
        st.write("Chatbot:", response)

if __name__ == "__main__":
    main()
