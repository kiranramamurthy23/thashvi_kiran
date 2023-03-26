import streamlit as st
def welcome_tab():

    display_text = "Welcome to the world of my little princess. Click the menu from side bar"

    st.markdown("<body style='font-size:40px;text-align:center;font-weight:bold;'>" + display_text + "</body>",
                unsafe_allow_html=True)
