import streamlit as st
from st_aggrid import AgGrid, AgGridTheme
import pandas as pd



def data_table(data: pd.DataFrame):
    """Generating Data Table with sent DataFrame.

    Args:
        data (pd.DataFrame): DataTable
    """
    new_data = data[['reg_date', 'last_phase_time', 'magnitude', 'latitude', 'longitude']]
    new_data.rename(columns={'reg_date': 'Date'}, inplace=True)
    new_data.rename(columns={'last_phase_time': 'Time (UTC*)'}, inplace=True)
    new_data.rename(columns={'magnitude': 'Magnitude (ml)'}, inplace=True)   
    styled_df = new_data.style.set_properties(**{'text-align': 'center'})

    # Display the styled DataFrame in Streamlit
    st.dataframe(styled_df, height=600, use_container_width=True)
    # st.dataframe(data, use_container_width=True, height=600)
    # AgGrid(data, height=600, theme=AgGridTheme.ALPINE)