import streamlit as st
def activity():
    c1,c2 = st.columns(2, gap="small")
    with c1:
        st.info("Sleeping when others are awake 😴")
    with c2:
        st.info("Drinking milk on demand 🍼")
    
    c1,c2 = st.columns(2, gap="small")
    with c1:
        st.success("Crying for no reasons 😭")
    with c2:
        st.success("Smile when I'm happy 😃")
        
    c1,c2 = st.columns(2, gap="small")
    with c1:
        st.info("Crawling to fidget something 🤾‍♀️")
    with c2:
        st.info("Spitting on everyone 🤤")
        
    c1,c2 = st.columns(2, gap="small")
    with c1:
        st.success("Seeking attention always 🤸‍♀️")
    with c2:
        st.success("Playing with everything except toys 🎮")
    st.warning("**Loading More. . .**")
