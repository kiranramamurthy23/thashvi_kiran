import streamlit as st
def photo_library():   
    with st.expander("**First Month**"):
        st.image(Image.open('one.png'))
        st.markdown("""<a href="https://drive.google.com/drive/folders/1-DMzhVju9hWX-mTmg1psMwJyaSZl54Xd">Click here...</a>""",unsafe_allow_html=True)
    with st.expander("**Second Month**"):
        st.image(Image.open('two.png'))
        st.markdown("""<a href="https://drive.google.com/drive/folders/1-DMzhVju9hWX-mTmg1psMwJyaSZl54Xd">Click here...</a>""",unsafe_allow_html=True)
    with st.expander("**Third Month**"):
        st.image(Image.open('three.png'))
        st.markdown("""<a href="https://drive.google.com/drive/folders/1-DMzhVju9hWX-mTmg1psMwJyaSZl54Xd">Click here...</a>""",unsafe_allow_html=True)
    with st.expander("**Fourth Month**"):
        st.image(Image.open('four.png'))
        st.markdown("""<a href="https://drive.google.com/drive/folders/1-DMzhVju9hWX-mTmg1psMwJyaSZl54Xd">Click here...</a>""",unsafe_allow_html=True)
    with st.expander("**Fifth Month**"):
        st.image(Image.open('five.png'))
        st.markdown("""<a href="https://drive.google.com/drive/folders/1-DMzhVju9hWX-mTmg1psMwJyaSZl54Xd">Click here...</a>""",unsafe_allow_html=True)
    st.info("Coming Soon. .  .")
