import streamlit as st
from matplotlib import image
import pandas as pd
import plotly.express as px
import os
import pandas as pd
import numpy as np


# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")


DATA_PATH = os.path.join(dir_of_interest, "data", "edu.csv")

st.title("Education")
df = pd.read_csv(DATA_PATH)
df=df.reset_index(drop=True)

df

st.bar_chart(df["Institute"])

DATA_PATH1 = os.path.join(dir_of_interest, "data", "exp.csv")

st.title("Experience")
df1 = pd.read_csv(DATA_PATH1)

df1

st.bar_chart(df1["Organization"])





