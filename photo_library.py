import streamlit as st
def photo_library():   
    txt="First Month:"    
    htmlstr1=f"""<p style='background-color:blue;
                                      color:white;
                                      font-size:28px;
                                      border-radius:3px;
                                      line-height:60px;
                                      padding-left:17px;
                                      opacity:0.6'>
                                      {txt}</style>
                                      <br></p>""" 
    st.markdown(htmlstr1,unsafe_allow_html=True) 
           
    st.markdown("""<a href="https://www.google.com/">Click here...</a>""",unsafe_allow_html=True)
