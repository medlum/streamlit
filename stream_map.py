import folium, datetime
import streamlit_folium
import streamlit as st
from streamlit_folium import folium_static, st_folium
from folium.plugins import MarkerCluster

# ------------------ folium and streamlit ------------------ #
st.set_page_config(layout="wide")

#@st.cache(suppress_st_warning=False)


def map_stream_func(now_modifed, complete_list):

    # set page
    st.title("Real Time HDB Car Park Availability")
    st.header(f"Current Date & Time")
    st.header(f"{now_modifed}")
    st.text("[V1.0] Andy Oh | School of Business & Acccountancy | Ngee Ann Polytechnic".upper())
   
    # set singapore map with folium module
    m = folium.Map(location=[1.3521, 103.8198], min_zoom =11, max_zoom = 15, max_bounds=True, tiles="CartoDB positron",
                name="Light Map", zoom_start=11)
    
    # MarkCluster plugin for faster mapping
    mc = MarkerCluster()

    # map lat and long data from complete list
    for coord in complete_list:
        # create custom icon with hdb logo
        custom_icon = folium.CustomIcon(
            icon_image='carpark_logo.jpg', icon_size=(20, 20))
        #iframe = folium.IFrame(
        #    f"Total Lots: {coord[7]} <br> Available Lots: {coord[8]} <br> Type of Carpark: {coord[5]} <br> Short Term Parking: {coord[6]}")
        
        # put carpark details with api data as pop-up
        poopup = folium.Popup(
            f"Total Lots: {coord[7]} <br> Available Lots: {coord[8]} <br> Type of Carpark: {coord[5]} <br> Short Term Parking: {coord[6]}", min_width=300, max_width=300)
        folium.Marker(location=[coord[3], coord[4]],
                    popup=poopup,
                    tooltip=coord[2],
                    icon=custom_icon).add_to(m)

    mc.add_to(m)
    # use streamlit function 
    folium_static(m, width=1000, height=560)
    


