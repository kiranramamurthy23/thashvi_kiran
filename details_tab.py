import streamlit as st
def details_tab():
    c1,c2 = st.columns(2, gap="small")
    with c1:
        st.info("I was born in Mysore")
    with c2:
        st.success("But going to live in Bangalore")
    
    c1,c2 = st.columns(2, gap="small")
    with c1:
        st.success("I like mummy")
    with c2:
        st.info("But I'm dad's little princess")