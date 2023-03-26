import streamlit as st
def model_registration(usecase):
    if usecase == 'Mortgage Loan':
        st.markdown("#### Model ID: 1001")
        st.write("----------------")
        st.markdown("#### Purpose Of The Model:")
    
        display_text = """UCAA specialises in lending various types of loans to urban customers. 
        When the company receives a loan application, 
        the company has to make a decision for loan approval based on the applicant’s profile. 
        Two types of risks are associated with the bank’s decision:<br>
        1. If the applicant is likely to repay the loan, 
        then not approving the loan results in a loss of business to the company<br>
        2. If the applicant is not likely to repay the loan, i.e. he/she is likely to default, 
        then approving the loan may lead to a financial loss for the company<br><br>
        The aim is to identify patterns which indicate if a person is likely to default, 
        which may be used for takin actions such as denying the loan, reducing the amount of loan, 
        lending (to risky applicants) at a higher interest rate, etc."""
    
        st.markdown("<body style='font-size:40px;text-align:center;font-weight:bold;'>" + display_text + "</body>",
                    unsafe_allow_html=True)
        

        st.write("---------")
        # st.markdown("#### Availability of internal solution:")
        st.radio("Availability of internal solution:",['Yes',"No"],label_visibility="visible",index=1)
        st.markdown("""<style>div[class*="stRadio"] > label > div[data-testid="stMarkdownContainer"] > p {
    font-size: 24px;font-weight: 600;}</style>""", unsafe_allow_html=True)
        
        
    elif usecase == "Insurance Cross-sell":
        st.markdown("### Purpose Of The Model:")
    
        display_text = "UCAA an Insurance company that has provided Health Insurance to its customers now they need your help in building a model to predict whether the policyholders (customers) from past year will also be interested in Vehicle Insurance provided by the company."
    
        st.markdown("<body style='font-size:40px;text-align:center;font-weight:bold;'>" + display_text + "</body>",
                    unsafe_allow_html=True)