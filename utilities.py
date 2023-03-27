import base64
import streamlit as st
from details_tab import *
from photo_library import *
from travel_plans import *
from social_activity import *
from activity import *
from welcome_tab import *

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
                 "🛠️ Travel Plans", "✔️ Social",
                 "♻️ Activities"]




def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

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

    
def add_logo(image_path):
    logo_image = add_background_image \
            (
            class_id="logo-begining",
            image_path=image_path
        )
    st.markdown(logo_image, unsafe_allow_html=True)

def add_background_image(
        class_id,
        image_path
):
    b64_image = get_base64(image_path)
    return """
            <style>
            div.%s 
            {

            background-image: url("data:image/png;base64,%s");
            background-repeat: no-repeat;

            }
            </style>
            """ % (
        class_id,
        b64_image
    )
