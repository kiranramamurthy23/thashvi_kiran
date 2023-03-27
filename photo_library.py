import streamlit as st
def photo_library():   
    txt="Checklist from Model Details Tab:"    
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
           
    
    # display_text = "Please verify the model documents and make your decision below"

    # st.markdown("<body style='font-size:40px;text-align:center;font-weight:bold;'>" + display_text + "</body>",
    #             unsafe_allow_html=True)
    st.write("")
    st.write("--------")
    st.radio("Approve model for deployment",['Approve',"Refer Back"],label_visibility="visible")