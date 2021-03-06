import folium, streamlit_folium
import streamlit as st
from streamlit_folium import folium_static
import json, csv, requests, datetime, time
from cp_dict import cp_dict

# ------------------ set time and connect api ------------------ #

# set to system current datetime and remove microsecond
now_dt = datetime.datetime.today().replace(microsecond=0)
now_str = str(now_dt)
# include T in current datetime as a required api query parameter
now_T = now_str.replace(' ', 'T')
# add 8 hours for streamlit server due to timezone difference
now_plus8 = str(now_dt + datetime.timedelta(hours=8))
# api url
endpoint = "https://api.data.gov.sg/v1/transport/carpark-availability"
# query parameter
query_params = {'date_time': now_T}
# get data and convert to json
data = requests.get(endpoint, params=query_params).json()

# ------------------ data processing ------------------ #
cp_code = []
total_lots = []
avail_lots = []

for item in data["items"]:
    for detail in item["carpark_data"]:
        #print(detail)
        cp_code.append(detail['carpark_number'])
        total_lots.append(detail["carpark_info"][0]["total_lots"])
        avail_lots.append(detail["carpark_info"][0]["lots_available"])

total_lots = total_lots[1:]
avail_lots = avail_lots[1:]

complete_list = []
for index in range(len(cp_code) - 1):
    if cp_code[index] in cp_dict:
        complete_list.append([index,
                              cp_code[index],
                              cp_dict[cp_code[index]][0],
                              cp_dict[cp_code[index]][1],
                              cp_dict[cp_code[index]][2],
                              cp_dict[cp_code[index]][3],
                              cp_dict[cp_code[index]][4],
                              total_lots[index],
                              avail_lots[index]])


# ------------------ folium and streamlit ------------------ #
st.set_page_config(layout="wide")
st.title(f"Real Time HDB Car Park Availability (version 1.0)")
st.header(now_plus8)
st.subheader("Programmed by Andy Oh")
m = folium.Map(location=[1.3521, 103.8198], tiles="CartoDB positron",
               name="Light Map", zoom_start=11, attr="My Data")


for index, coord in enumerate(complete_list):

    custom_icon = folium.CustomIcon(
        icon_image='carpark_logo.jpg', icon_size=(20, 20))
    #iframe = folium.IFrame(
    #    f"Total Lots: {coord[7]} <br> Available Lots: {coord[8]} <br> Type of Carpark: {coord[5]} <br> Short Term Parking: {coord[6]}")
    poopup = folium.Popup(
        f"Total Lots: {coord[7]} <br> Available Lots: {coord[8]} <br> Type of Carpark: {coord[5]} <br> Short Term Parking: {coord[6]}", min_width=300, max_width=300)
    folium.Marker(location=[coord[3], coord[4]],
                popup=poopup,
                tooltip=coord[2],
                icon=custom_icon).add_to(m)
  
folium_static(m, width=950, height=560)

##data = pd.DataFrame({
##    'awesome cities': ['Chicago', 'Minneapolis', 'Louisville', 'Topeka'],
##    'lat': [41.868171, 44.979840,  38.257972, 39.030575],
##    'lon': [-87.667458, -93.272474, -85.765187,  -95.702548]
##})
#

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
