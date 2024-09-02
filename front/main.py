import streamlit as st
from streamlit import config as st_config
from streamlit_option_menu import option_menu
from streamlit_extras.stylable_container import stylable_container

import home_page, statistics_page, settings_page, upload_page


page_icon = "/mnt/hdd/@home/Link to archy/Desktop/caiag.kg/pets/ses_statistics_web/logo/logo_CAIAG_RU.jpg"

def __set_page_configs():
    st.set_page_config(
        page_title="SES",
        page_icon=page_icon,
        layout="wide",
        initial_sidebar_state="collapsed",
        menu_items={}
    )

    hide_st_style = """
                    <style>
                    #MainMenu {visibility: hidden;}
                    footer {visibility: hidden;}
                    header {visibility: hidden;}
                    
                    .block-container {
                        padding-top: 1rem;
                        padding-bottom: 0rem;
                        padding-left: 5rem;
                        padding-right: 5rem;
                    }
                    </style>
                    """
    st.markdown(hide_st_style, unsafe_allow_html=True)


def __theme_switcher():
    if 'theme_label' not in st.session_state:
        st.session_state['theme_label'] = '☀️'
        st.session_state['backgroundColor'] = '#3C7EC9'

    with stylable_container(
        key="theme_switcher",
        css_styles=f"""
            button {{
                background-color: {st.session_state['backgroundColor']};
                color: yellow;
                border-radius: 10px;
                width: 80px;    
                height: 20px;    
                padding: 10px 20px; 
                font-size: 10px;
            }}
            """
        ):
        if st.button(st.session_state['theme_label'], key="theme_switcher", help="Theme switcher"):
            if st.session_state["theme"] == "light":        # DARK THEME
                st.session_state["theme"] = "dark"
                st.session_state['theme_label'] = '☀️'
                st.session_state['backgroundColor'] = '#3C7EC9'
                st_config.set_option("theme.base", "dark")
                st_config.set_option("theme.backgroundColor", "#697565")
                st_config.set_option("theme.primaryColor", "#3C3D37")
                st_config.set_option("theme.secondaryBackgroundColor", "#ECDFCC")
                st_config.set_option("theme.textColor", "#1E201E")
            else:                                           # LIGHT THEME
                st.session_state["theme"] = "light"
                st.session_state['theme_label'] = '🌕️'
                st.session_state['backgroundColor'] = '#191970'
                st_config.set_option("theme.base", "light")
                st_config.set_option("theme.backgroundColor", "#FEFAE0")
                st_config.set_option("theme.primaryColor", "#A6B37D")
                st_config.set_option("theme.secondaryBackgroundColor", "#E0E5B6")
                st_config.set_option("theme.textColor", "#333333")

            st.rerun()

    # st.markdown(
    #     """
    #     <style>
    #     .stButton button {
    #         background-color: #ECDFCC;
    #         border: none;
    #         padding: 0;
    #         margin: 0;
    #         width: 40px;
    #         height: 40px;
    #         background-image: url('https://img.icons8.com/ios-filled/50/000000/light-on.png');
    #         background-size: 30px 30px;
    #         background-position: center;
    #         background-repeat: no-repeat;
    #         cursor: pointer;
    #         border-radius: 8px;
    #         transition: background-color 0.2s;
    #     }
    #     .stButton button:active {
    #         background-color: #FF8343;
    #     }
    #     </style>
    #     """,
    #     unsafe_allow_html=True
    # )


def __language_switcher():
    langs = {
        'KG': "Russian",
        'RU': "Russian",
        'EN': "Russian",
    }

    if 'lang_label' not in st.session_state:
        st.session_state['lang_label'] = 'RU'

    with stylable_container(
        key="lang_switcher",
        css_styles="""
            button {
                background-color: #697565;
                color: #ECDFCC;
                border-radius: 10px;
                width: 80px;    
                height: 20px;    
                padding: 10px 20px; 
                font-size: 10px;
            }
            """
        ):
        with st.popover(st.session_state['lang_label'], help="Language switcher"):
            chd_lang = st.radio(
                "Select language:",
                ['***KG***', '***RU***', '***EN***']
            )

            st.session_state['lang_label'] = chd_lang

            # st.rerun()



    # if st.button(st.session_state['lang_label'], key="language_switcher", help="Language switcher"):
    #     if st.session_state['lang_label']

def __set_head():
    head = st.container(border=True)
    col1, col2 = head.columns([9, 1])

    with col1:
        col1.header(
            """
            :red[SES]
            :red[S]eysmikalyk okuyalar jonundo erte :red[E]skertuu :red[S]istemasy
            """,
            # divider="red",
            anchor=False,
            help='''Система раннего оповещания о произошедшем землетрясении (__на Кыргызском языке__*).'''
        )


    if "theme" not in st.session_state:
        st.session_state["theme"] = "light"

    with col2:
        __theme_switcher()
        __language_switcher()


def main():
    __set_page_configs()
    __set_head()

    # page = option_menu(None, ["Home", "Upload", "Statistics", 'Settings'],
    #                    icons=['house', 'cloud-upload', "list-task", 'gear'],
    #                    menu_icon="cast", default_index=0, orientation="horizontal")

    page = option_menu(None, ["Home", "Statistics"],
                       icons=['house', "list-task"],
                       menu_icon="cast", default_index=0, orientation="horizontal")

    match page:
        case "Home":
            home_page.home()

        case "Statistics":
            statistics_page.statistics()

    # from PIL import Image
    #
    # icon_path = "/mnt/hdd/@home/Link to archy/Desktop/caiag.kg/pets/ses_statistics_web/logo/logo_CAIAG_RU.jpg"
    #
    #
    # info_text = st.columns(1)
    #
    # icon = Image.open(icon_path)
    # info_text[0].image(icon, width=46)

if __name__ == "__main__":
    main()