import streamlit as st
# import streamlit.components.v1 as components
import pickle
import pandas as pd

def travel_plans():
    display_text = "Enter model description below. We shall serve you the best to answer about rules, regulations and risk of the model."

    
    col0, col1 = st.columns([1, 0.05])
    # with col0:
    #     st.markdown("<body style='font-size:40px;text-align:center;font-weight:bold;'>" + display_text + "</body>",
    #                 unsafe_allow_html=True)
    with col0:
        st.markdown("<body style='font-size:40px;text-align:center;font-weight:bold;'>" + display_text + "</body>",
                    unsafe_allow_html=True)
        
        txt = st.text_area('', '''Enter model description here''')
        if st.button("Submit"):
            st.write("Please find the results below:-")
            with st.container():
                path = "C:/Users/suneyna/Downloads/git_app/git_app/"
                with open(path+'ucaa_db.pkl', 'rb') as f:
                    dct = pickle.load(f)
                st.write(dct['model_details'])
                # st.write(pd.DataFrame(dct))
        # components.html(r"""
        # <script src="https://www.gstatic.com/dialogflow-console/fast/messenger-cx/bootstrap.js?v=1"></script><df-messenger
        # df-cx='true'
        # location='asia-south1'
        # chat-title='CompanyPolicyBot'
        # agent-id="a729922e-4110-46ef-a5dc-23e95f82b05e"
        # language-code="en"><style>
        # .container {
        # max-height: 300px;
        # height: 50%;
        # }</style></df-messenger>

        # """,
        #                 height=300, width=500)

