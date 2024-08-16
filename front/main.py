import streamlit as st
from streamlit_option_menu import option_menu
import json, requests, os

import home_page, statistics_page, settings_page, upload_page

page_icon = "/mnt/hdd/@home/Link to archy/Desktop/caiag.kg/pets/ses_statistics_web/logo/logo_CAIAG_RU.jpg"

st.set_page_config(
    page_title="SES",
    page_icon=page_icon,
    layout="wide",  
    initial_sidebar_state="collapsed",  
    menu_items={}
)


col1, col2 = st.columns([9, 1])
    

with col1:
    st.header(
        ":blue-background[SES]", 
        divider=True,
        anchor=False,
        help='''***":blue[S]eysmikalık okuyalar jonundo :blue[E]skertuu :blue[S]isteması"*** - Система раннего оповещания
        \nо произошедшем землетрясении (__на Кыргызском языке__*).'''
        )
    

if "theme" not in st.session_state:
    st.session_state["theme"] = "light"

with col2:
    if st.button("",key="theme_switcher"):
        if st.session_state["theme"] == "light":
            st.session_state["theme"] = "dark"
            st._config.set_option("theme.base", "dark")
            st._config.set_option("theme.backgroundColor", "#333333")
            st._config.set_option("theme.primaryColor", "#4A90E2")
            st._config.set_option("theme.secondaryBackgroundColor", "#4A4A4A")
            st._config.set_option("theme.textColor", "#F5F7FA")
        else:
            st.session_state["theme"] = "light"
            st._config.set_option("theme.base", "light")
            st._config.set_option("theme.backgroundColor", "#F5F7FA")
            st._config.set_option("theme.primaryColor", "#4A90E2")
            st._config.set_option("theme.secondaryBackgroundColor", "#D9E2EF")
            st._config.set_option("theme.textColor", "#333333")

        st.rerun()

    st.markdown(
        """
        <style>
        .stButton button {
            background-color: orange;
            border: none;
            padding: 0;
            margin: 0;
            width: 40px;  
            height: 40px; 
            background-image: url('https://img.icons8.com/ios-filled/50/000000/light-on.png');
            background-size: 30px 30px;
            background-position: center;
            background-repeat: no-repeat;
            cursor: pointer;
            border-radius: 8px;  
            transition: background-color 0.2s;
        }
        .stButton button:active {
            background-color: green;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

page = option_menu(None, ["Home", "Upload", "Statistics", 'Settings'],
        icons=['house', 'cloud-upload', "list-task", 'gear'],
        menu_icon="cast", default_index=0, orientation="horizontal")



match page:
    case "Home":
        home_page.home()
    
    case "Upload":
        upload_page.upload()
        
    case "Statistics":
        statistics_page.statistics()
        
    case "Settings":
        settings_page.settings()
    


from PIL import Image

icon_path = "/mnt/hdd/@home/Link to archy/Desktop/caiag.kg/pets/ses_statistics_web/logo/logo_CAIAG_RU.jpg"


info_text = st.columns(1)

icon = Image.open(icon_path)
info_text[0].image(icon, width=46)