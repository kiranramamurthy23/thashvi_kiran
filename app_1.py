import streamlit as st
st.set_page_config(layout='wide')
# Using object notation
from utilities import *

################# HIDING STREAMLIT FOOTER LOGO ############################

hide_streamlit_style = """
<style>
#MainMenu {visibility: show;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>

"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Radio Button Style
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
st.markdown("""<style>div[class*="stRadio"] > label > div[data-testid="stMarkdownContainer"] > p {
font-size: 24px;font-weight: 600;}</style>""", unsafe_allow_html=True)
#############################################
# set_png_as_page_bg('bgm.png')

################### USAA LOGO ###########################

st.markdown(f"""<div class='logo-begining'></div>""", unsafe_allow_html=True)
add_logo_img("logo.png")
# add_logo_gif("Thashu_V1.gif")
with open("style_test.css") as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

##############################################


tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(model_stages_)
with tab1:
    model_phases_dict["Welcome tab"]()
    add_logo_gif("Thashu_V1.gif")
with tab2:
    model_phases_dict["Details"]()

with tab3:
    model_phases_dict["Photo"]()

with tab4:
    model_phases_dict["Travel"]()

with tab5:
    model_phases_dict["Social"]()

with tab6:
    model_phases_dict["Activity"]()






