import folium, streamlit_folium
import streamlit as st
from streamlit_folium import folium_static
import numpy as np
import pandas
#st.set_page_config(layout="wide")
#print(streamlit-folium.__version__)

m = folium.Map(location=[23.47, 77.94], tiles="CartoDB positron", name = "Light Map", zoom_start=5, attr="My Data")

folium_static(m, width=950, height=560)

# title
#st.title("Hello World!")
#st.header("This is a header")
#st.subheader("This is a subheader")
#st.text("Hello Andy!")
#
#age = st.selectbox("Choose your age:", np.arange(18,66,1) )
#age = st.slider("Choose your age: ", min_value=16, max_value=66, value=35, step=1)
#artists = st.multiselect("Who are your favorite artists?",
#                         ["Michael Jackson", "Elvis Presley",
#                          "Eminem", "Billy Joel", "Madonna"])

#actions = {"A": st.write, "B": st.write, "C": st.write}
#choice = st.selectbox("Choose one:", ["_", "A", "B", "C"])
#if choice != "_":
#    result = actions[choice](f"You chose {choice}")
