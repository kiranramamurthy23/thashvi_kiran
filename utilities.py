import base64
import streamlit as st
from details_tab import *
from photo_library import *
from travel_plans import *
from social_activity import *
from activity import *
from welcome_tab import *
from PIL import Image

model_phases_dict = {
    "Welcome tab": welcome_tab,
    "Details": details_tab,
    "Photo": photo_library,
    "Travel": travel_plans,
    "Social": social_activity,
    "Activity": activity
}

model_stages_ = ["Welcome",
                 "✍️ Details", "📁 Photo Library",
                 "🌴 Travel Plans", "👩‍👩‍👧‍👧 Social",
                 "♻️ Activities"]




@st.cache_data
def add_logo_gif(image_path):
    """### gif from local file"""
    file_ = open(image_path, "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()
    
    st.markdown(
        f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
        unsafe_allow_html=True,
    )


    
