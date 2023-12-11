import streamlit as st
import os
import requests
from streamlit_lottie import st_lottie

st.set_page_config(page_title="AWS Demo", page_icon=":tada:", layout="wide")

st.image('./logo.png', width=80)
st.title("This the site for AWS Demo")


hide = """
    <style>
        .css-1jc7ptx, .e1ewe7hr3, .viewerBadge_container__1QSob,
        .styles_viewerBadge__1yB5_, .viewerBadge_link__1S137,
        .viewerBadge_text__1JaDK {
        display: none;
        }
        # footer { visibility: hidden; } 
        header { visibility: hidden; }
        #MainMenu {visibility: visible;}
        footer {visibility: hidden;}
    </style>
    """
st.markdown(hide, unsafe_allow_html=True)

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
lottie_coding = load_lottieurl("https://lottie.host/f1767470-c8ea-4e48-b3bb-8e5ed9c44431/tfW1qxCrWa.json") 

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Please clik thye below button to access the control panel for Vison system")

        st.button("Control System")
        st.write("")
        st.write("[MSISLAB Inc.  >](https://www.msislab.co.kr/)")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")


