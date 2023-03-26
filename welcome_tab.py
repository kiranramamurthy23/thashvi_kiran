import streamlit as st
def welcome_tab():

    display_text = "Please choose the use case from the list present in the sidebar menu"

    st.markdown("<body style='font-size:40px;text-align:center;font-weight:bold;'>" + display_text + "</body>",
                unsafe_allow_html=True)