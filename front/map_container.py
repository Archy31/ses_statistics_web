from streamlit_plotly_mapbox_events import plotly_mapbox_events
import plotly.express as px
from streamlit_extras.stylable_container import stylable_container
import streamlit as st

import pandas as pd


LAYERS = {
    'terrain': 'http://mt0.google.com/vt/lyrs=p&hl=en&x={x}&y={y}&z={z}',
    'hybrid': 'http://mt0.google.com/vt/lyrs=y&hl=en&x={x}&y={y}&z={z}',
    'satellite': 'http://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}'
}

def __get_map_url(form: st, layers: dict) -> str:
    with form.container(border=True):
        st.markdown(
            """
            <style>
            .stContainer > div {
                width: 20%;
                margin: auto;
                height: 10%;
                padding-top: 20px; 
                padding-bottom: 20px;
            }
            </style>
            """,
            unsafe_allow_html=True
        )
        col1, col2 = form.columns([5, 4])
        col1.write("**Select map type:**")


        if 'map_label' not in form.session_state:
            form.session_state['map_label'] = 'hybrid'

        with stylable_container(
                key="map_selector",
                css_styles="""
                    button {
                        background-color: #ECDFCC;
                        color: yellow;
                        border-radius: 10px;
                        width: 80px;    
                        height: 20px;    
                        padding: 10px 20px; 
                        font-size: 10px;
                    }
                    """
        ):
            with col2.popover(form.session_state['map_label'], use_container_width=True):
                layer_type = st.radio(
                    "Select map type:",
                    (
                        "hybrid",
                        "terrain",
                        "satellite"
                    )
                )
                form.session_state['map_label'] = layer_type

                return layers[layer_type]



def data_mapping(data: pd.DataFrame):
    with st.container(border=True):
        layer = __get_map_url(form=st, layers=LAYERS)

        mapbox = px.scatter_mapbox(
            data_frame=data,
            lat="lat", lon="lon",
            hover_name="hover",
            zoom=8,
            height=646,
        )

        mapbox.update_layout(
            mapbox_style="white-bg",
            mapbox_layers=[
                    {
                        "below": 'traces',
                        "sourcetype": "raster",
                        # "sourceattribution": "Kyrgyzstan. Bishkek. CAIAG",
                        "source": [layer]
                    }
                ],
            margin={"r": 0, "t": 0, "l": 0, "b": 0},
            showlegend=False,
            )
        mapbox.update_traces(text=None)

        mapbox_events = plotly_mapbox_events(
            mapbox,
            click_event=True,
            select_event=True,
            hover_event=True,
            override_height=646
        )

    # Clicked point: mapbox_events[0]
    # "<a href='https://caiag.kg/en/' target='_blank'>Kyrgyzstan. Bishkek. CAIAG</a>"


