import streamlit as st

def social_activity():
    # st.markdown("#### Availability of data:")
    st.radio("Availability of data:",['Yes',"No"],label_visibility="visible",index=0)
    
    st.write("---------")
