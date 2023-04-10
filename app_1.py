import streamlit as st
st.set_page_config(layout='wide')
# Using object notation
from utilities import *
from PIL import Image

################# HIDING STREAMLIT FOOTER LOGO ############################

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>

"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Remove whitespace from the top of the page and sidebar
st.markdown("""
        <style>
               .block-container {
                    padding-top: 1rem;
                    padding-bottom: 0rem;
                    padding-left: 1rem;
                    padding-right: 1rem;
                }
        </style>
        """, unsafe_allow_html=True)

# Radio Button Style
# st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
# st.markdown("""<style>div[class*="stRadio"] > label > div[data-testid="stMarkdownContainer"] > p {
# font-size: 24px;font-weight: 600;}</style>""", unsafe_allow_html=True)
#############################################

################### LOGO ###########################
st.image(Image.open('logo.PNG'))

##############################################

tabs_font_css = """
<style>
button[data-baseweb="tab"] > div[data-testid="stMarkdownContainer"] > p {
font-size: 22px;
}
</style>
"""
st.write(tabs_font_css, unsafe_allow_html=True)

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(model_stages_)
with tab1:
    model_phases_dict["Welcome tab"]()
    st.success("## Welcome to my little world")
    st.image(Image.open('apr10.png'))
    # add_logo_gif("Thashu_V1.gif")
with tab2:
    model_phases_dict["Details"]()
    add_logo_gif("birthday.gif")    
with tab3:
    model_phases_dict["Photo"]()

with tab4:
    model_phases_dict["Travel"]()

with tab5:
    model_phases_dict["Social"]()

with tab6:
    model_phases_dict["Activity"]()






