import streamlit as st
def activity():
    c1,c2 = st.columns(2, gap="small")
    with c1:
        st.info("Sleeping")
    with c2:
        st.success("Drinking Milk")
    
    c1,c2 = st.columns(2, gap="small")
    with c1:
        st.success("Crying")
    with c2:
        st.info("Smiling")
        
    c1,c2 = st.columns(2, gap="small")
    with c1:
        st.info("Crawling")
    with c2:
        st.success("Spitting")
    st.warning("**Loading More. . .**")