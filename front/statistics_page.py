import pandas as pd 
import numpy as np 

import streamlit as st
from streamlit_lightweight_charts import renderLightweightCharts
import streamlit_lightweight_charts.dataSamples as data
import plotly.express as px


def first():
    priceVolumeChartOptions = {
        "height": 400,
        "rightPriceScale": {
            "scaleMargins": {
                "top": 0.2,
                "bottom": 0.25,
            },
            "borderVisible": False,
        },
        "overlayPriceScales": {
            "scaleMargins": {
                "top": 0.7,
                "bottom": 0,
            }
        },
        "layout": {
            "background": {
                "type": 'solid',
                "color": '#131722'
            },
            "textColor": '#d1d4dc',
        },
        "grid": {
            "vertLines": {
                "color": 'rgba(42, 46, 57, 0)',
            },
            "horzLines": {
                "color": 'rgba(42, 46, 57, 0.6)',
            }
        }
    }

    priceVolumeSeries = [
        {
            "type": 'Area',
            "data": data.priceVolumeSeriesArea,
            "options": {
                "topColor": 'rgba(38,198,218, 0.56)',
                "bottomColor": 'rgba(38,198,218, 0.04)',
                "lineColor": 'rgba(38,198,218, 1)',
                "lineWidth": 2,
            }
        },
        {
            "type": 'Histogram',
            "data": data.priceVolumeSeriesHistogram,
            "options": {
                "color": '#26a69a',
                "priceFormat": {
                    "type": 'volume',
                },
                "priceScaleId": "" # set as an overlay setting,
            },
            "priceScale": {
                "scaleMargins": {
                    "top": 0.7,
                    "bottom": 0,
                }
            }
        }
    ]
    st.subheader("Price and Volume Series Chart")

    renderLightweightCharts([
        {
            "chart": priceVolumeChartOptions,
            "series": priceVolumeSeries
        }
    ], 'priceAndVolume')
    

    
    chartOptions = {
    "layout": {
        "textColor": 'black',
        "background": {
            "type": 'solid',
            "color": 'white'
            }
        }
    }


    seriesBaselineChart = [{
        "type": 'Baseline',
        "data": [
            { "value": 1, "time": 1642425322 },
            { "value": 8, "time": 1642511722 },
            { "value": 10, "time": 1642598122 },
            { "value": 20, "time": 1642684522 },
            { "value": 3, "time": 1642770922 },
            { "value": 43, "time": 1642857322 },
            { "value": 41, "time": 1642943722 },
            { "value": 43, "time": 1643030122 },
            { "value": 56, "time": 1643116522 },
            { "value": 46, "time": 1643202922 }
        ],
        "options": {
            "baseValue": { "type": "price", "price": 25 },
            "topLineColor": 'rgba( 38, 166, 154, 1)',
            "topFillColor1": 'rgba( 38, 166, 154, 0.28)',
            "topFillColor2": 'rgba( 38, 166, 154, 0.05)',
            "bottomLineColor": 'rgba( 239, 83, 80, 1)',
            "bottomFillColor1": 'rgba( 239, 83, 80, 0.05)',
            "bottomFillColor2": 'rgba( 239, 83, 80, 0.28)'
        }
    }]

    st.subheader("Baseline Chart with Watermark")

    renderLightweightCharts([
        {
            "chart": chartOptions,
            "series": seriesBaselineChart
        }
    ], 'baseline')
    

def __gutenberg_richter(form: st, data: pd.DataFrame = None):
    chart_data = data.groupby('magnitude').size().reset_index(name='Count')
    chart_data = chart_data.sort_values(by='magnitude', ascending=False)
    chart_data['Cumulative_Count'] = chart_data['Count'].cumsum()
    chart_data['Log_Cumulative_Count'] = np.log10(chart_data['Cumulative_Count'])
    
    chart_data.rename(columns={'magnitude': 'Magnitude'}, inplace=True)   
    
    fig = px.line(chart_data, x="Magnitude", y="Count")
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)
    

def statistics(form: st, data: pd.DataFrame):
    charts = {
        "Gutenberg-Richter magnitude": __gutenberg_richter,
        
    }
    
    std_chart = form.selectbox(
        "Select chart type:",
        ("Not selected", "Gutenberg-Richter magnitude", "Quadrangle"),
    )
    
    if std_chart in charts.keys():
        charts[std_chart](form=form, data=data)

