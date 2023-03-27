import streamlit as st
import streamlit.components.v1 as components

def travel_plans():
    display_text = "Chat with my baby..."

    
    col0, col1 = st.columns([1, 0.05])
    # with col0:
    #     st.markdown("<body style='font-size:40px;text-align:center;font-weight:bold;'>" + display_text + "</body>",
    #                 unsafe_allow_html=True)
    with col0:
        st.markdown("<body style='font-size:40px;text-align:center;font-weight:bold;'>" + display_text + "</body>",
                    unsafe_allow_html=True)
        
        components.html(r"""
        <script src="https://www.gstatic.com/dialogflow-console/fast/messenger-cx/bootstrap.js?v=1"></script><df-messenger
        df-cx='true'
        location='asia-south1'
        chat-title='CompanyPolicyBot'
        agent-id="a729922e-4110-46ef-a5dc-23e95f82b05e"
        language-code="en"><style>
        .container {
        max-height: 300px;
        height: 50%;
        }</style></df-messenger>

        """,
                        height=300, width=500)

