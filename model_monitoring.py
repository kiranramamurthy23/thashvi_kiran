import streamlit as st

def model_monitoring(usecase):
    if usecase == 'Mortgage Loan':
        display_text = "After model deployment, the reports are displayed below"
    
        st.markdown("<body style='font-size:40px;text-align:center;font-weight:bold;'>"+display_text+"</body>", unsafe_allow_html=True)