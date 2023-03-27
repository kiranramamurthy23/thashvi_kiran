import streamlit as st
def activity():
    display_text = "Model is ready for deployment"

    st.markdown("<body style='font-size:40px;text-align:center;font-weight:bold;'>" + display_text + "</body>",
                unsafe_allow_html=True)
    
    st.write("")
    
    st.markdown("""<a href="https://www.google.com/">Click here...</a>""",unsafe_allow_html=True)