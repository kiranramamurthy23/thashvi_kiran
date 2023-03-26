import streamlit as st

def model_development_phase(usecase):
    if usecase == 'Mortgage Loan':
        # st.markdown("#### Availability of data:")
        st.radio("Availability of data:",['Yes',"No"],label_visibility="visible",index=0)
        st.markdown("""<style>div[class*="stRadio"] > label > div[data-testid="stMarkdownContainer"] > p {
    font-size: 24px;font-weight: 600;}</style>""", unsafe_allow_html=True)
        
        st.write("---------")
        
        st.markdown("#### EDA and Charts:")
        if st.button("Fetch Details"):
            st.write("Details are displayed below")
            
        # display_text = "Model Training Details"
    
        # st.markdown("<body style='font-size:40px;text-align:center;font-weight:bold;'>" + display_text + "</body>",
        #             unsafe_allow_html=True)
        
        # st.write("")
        
        # st.markdown("""<a href="https://www.google.com/">Click here...</a>""",unsafe_allow_html=True)