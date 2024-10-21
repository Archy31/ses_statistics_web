import streamlit as st
from st_aggrid import AgGrid, AgGridTheme
import pandas as pd



def data_table(data: pd.DataFrame):
    """Generating Data Table with sent DataFrame.

    Args:
        data (pd.DataFrame): DataTable
    """
    styled_df = data.style.set_properties(**{'text-align': 'center'})

    # Display the styled DataFrame in Streamlit
    st.dataframe(styled_df, height=600, width=490)
    # st.dataframe(data, use_container_width=True, height=600)
    # AgGrid(data, height=600, theme=AgGridTheme.ALPINE)