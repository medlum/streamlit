import folium
import streamlit_folium
import streamlit as st
from streamlit_folium import folium_static, st_folium

# ------------------ folium and streamlit ------------------ #
st.set_page_config(layout="wide")

#@st.cache(suppress_st_warning=False)
def map_stream_func(complete_list):
    
    # set page

    #st.title(f"Real Time HDB Car Park Availability (version 1.0)")
    #st.header(now_plus8)
    #st.subheader("Programmed by Andy Oh")
    
    # set singapore map with folium module
    m = folium.Map(location=[1.3521, 103.8198], tiles="CartoDB positron",
                name="Light Map", zoom_start=11, attr="My Data")


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

    # use streamlit function 
    folium_static(m, width=950, height=560)
    


