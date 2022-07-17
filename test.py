import folium, streamlit_folium
import streamlit as st
from streamlit_folium import folium_static
import numpy as np
import pandas as pd
st.set_page_config(layout="wide")
#print(streamlit-folium.__version__)

#https://deckgl.readthedocs.io/en/latest/

st.title("HDB Car Park Availability in Real Time")

m = folium.Map(location=[1.3521, 103.8198], tiles="CartoDB positron",
               name="Light Map", zoom_start=11, attr="My Data")

custom_icon = folium.CustomIcon(icon_image='home_icon.png', icon_size=(20, 20))
folium.Marker([1.3633000666013873, 103.82944513883707],
                popup="<h2>Our Home</h2><img src='home.jpg', width=200px><p>18 Jalan Gendang</p>",
                tooltip="Home",
                icon=custom_icon).add_to(m)

folium_static(m, width=950, height=560)

#data = pd.DataFrame({
#    'awesome cities': ['Chicago', 'Minneapolis', 'Louisville', 'Topeka'],
#    'lat': [41.868171, 44.979840,  38.257972, 39.030575],
#    'lon': [-87.667458, -93.272474, -85.765187,  -95.702548]
#})


#st.map(data)
# Adding code so we can have map default to the center of the data
#midpoint = (np.average(data['lat']), np.average(data['lon']))



# -------------- basic map ----------------#
# https://www.youtube.com/watch?v=AHiWIOohYa8

#m = folium.Map(location=[1.3521, 103.8198], tiles="CartoDB positron",
#               name="Light Map", zoom_start=11, attr="My Data")
#
#folium_static(m, width=950, height=560)

# title

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
