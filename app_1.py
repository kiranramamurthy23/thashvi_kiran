import streamlit as st
st.set_page_config(layout='wide')
# Using object notation
from utilities import *

################# HIDING STREAMLIT FOOTER LOGO ############################

hide_streamlit_style = """
<style>
#MainMenu {visibility: show;}
footer {visibility: hidden;}
</style>

"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Radio Button Style
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
st.markdown("""<style>div[class*="stRadio"] > label > div[data-testid="stMarkdownContainer"] > p {
font-size: 24px;font-weight: 600;}</style>""", unsafe_allow_html=True)
#############################################

################### USAA LOGO ###########################

st.markdown(f"""<div class='logo-begining'></div>""", unsafe_allow_html=True)
add_logo("usaa_logo.png")
with open("style_test.css") as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

##############################################


with st.sidebar:
    st.markdown("<h1 style='font-size:40px;text-align:center;font-weight:bold;'>USAA</h1>", unsafe_allow_html=True)



    st.markdown("<h2>Choose Use Case: </h2>", unsafe_allow_html=True)
    use_case_select_box = st.sidebar.selectbox(
        "choose the use-case",
        use_cases_,
        label_visibility='hidden'
    )

    #st.markdown("<h2>Choose the Phase: </h2>", unsafe_allow_html=True)
    #model_phase_select_box = st.sidebar.selectbox(
    #    "choose the model phase",
    #    model_stages_,
    #    label_visibility='hidden'
    #)


 
if use_case_select_box != "<Please Choose>":
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(model_stages_[1:])
    with tab1:
        model_phases_dict["Model Registration"](use_case_select_box)

    with tab2:
        model_phases_dict["Model Details"](use_case_select_box)

    with tab3:
        model_phases_dict["Model Development Phase"](use_case_select_box)

    with tab4:
        model_phases_dict["Model Approval For Deployment"](use_case_select_box)

    with tab5:
        model_phases_dict["Model Deployment"](use_case_select_box)

    with tab6:
        model_phases_dict["Model Monitoring"](use_case_select_box)
else:
    col1,col2 = st.columns((1.3,0.7))
    with col1:
        st.header("Welcome")
        model_phases_dict["Welcome tab"]()






