import streamlit as st
import pydeck as pdk
import pandas as pd
from matplotlib import image
import os
import pandas as pd
import plotly.express as px


st.header("View My Location")
# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

DATA_PATH = os.path.join(dir_of_interest, "data", "sample.csv")


df = pd.read_csv(DATA_PATH)

layer = pdk.Layer(
        "ScatterplotLayer",
        df,
        pickable=True,
        opacity=0.8,
        filled=True,
        radius_scale=2,
        radius_min_pixels=10,
        radius_max_pixels=500,
        line_width_min_pixels=0.01,
        get_position='[Longitude, Latitude]',
        get_fill_color=[255, 0, 0],
        get_line_color=[0, 0, 0],
    )

    # Set the viewport location
view_state = pdk.ViewState(latitude=df['Latitude'].iloc[-1], longitude=df['Longitude'].iloc[-1], zoom=13, min_zoom= 10, max_zoom=30)

    # Render
r = pdk.Deck(layers=[layer], map_style='mapbox://styles/mapbox/satellite-v9',
                 initial_view_state=view_state, tooltip={"html": "<b>Point ID: </b> {PointID} <br /> "
                                                                 "<b>Longitude: </b> {Longitude} <br /> "
                                                                 "<b>Latitude: </b>{Latitude} <br /> "
                                                                 "<b> Value: </b>{Value} <br /> "
                                                                 "<b> City: </b> {City}"})
r

   