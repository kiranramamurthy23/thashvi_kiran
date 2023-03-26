import base64
import streamlit as st
from model_details import *
from model_approval_deployment import *
from model_deployment import *
from model_approval_deployment import *
from model_registration import *
from model_monitoring import *
from model_development_phase import *
from welcome_tab import *

model_phases_dict = {
    "Welcome tab": welcome_tab,
    "Model Registration": model_registration,
    "Model Details": model_details,
    "Model Development Phase": model_development_phase,
    "Model Approval For Deployment": model_approval_deployment,
    "Model Deployment": model_deployment,
    "Model Monitoring": model_monitoring
}

use_cases_ = ["Choose Menu", "Details", "Photo Gallery","Travel List"]

model_stages_ = ["",
                 "✍️ First Year", "📁 Second Year",
                 "🛠️ Third Year", "✔️ Fourth Year",
                 "♻️ Fifth Year", "👓 Sixth"]




def get_image_base64(image_path):
    with open(image_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


def add_background_image(
        class_id,
        image_path
):
    b64_image = get_image_base64(image_path)
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


def add_logo(image_path):
    logo_image = add_background_image \
            (
            class_id="logo-begining",
            image_path=image_path
        )
    st.markdown(logo_image, unsafe_allow_html=True)

