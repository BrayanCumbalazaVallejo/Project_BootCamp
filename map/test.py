import streamlit as st
import pandas as pd


data = pd.DataFrame({
    'lat': [6.2725062336625035],
    'lon': [-75.5934863]
})

st.header("test Medellín")
st.map(data, zoom=10)
