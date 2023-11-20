
import folium
import pandas as pd
import os
andong = folium.Map(location=[37.55, 126.98], zoom_start=12)
andong.save(r"C:/data/andong.html")



data =pd.read_csv(r"C:\Users\1\.conda\envs\Bigdata\data\seoul-metro-2021.logs.csv")
station_info = pd.read_csv(r"C:\Users\1\.conda\envs\Bigdata\data\seoul-metro-station-info.csv")
station_sum = data.groupby("station_code").sum()
station_sum = station_sum[['people_in', 'people_out']]
output_file_path = (r"C:\Users\1\.conda\envs\Bigdata\data\seoul-metro-station_code.csv")
station_sum.to_csv(output_file_path)

station_info = station_info[['station.code', 'geo.latitude', 'geo.longitude']]
station_info = station_info.set_index('station.code')
joined_data = station_sum.join(station_info)
seoul_in = folium.Map(location=[37.55, 126.98], zoom_start = 12)
from folium.plugins import HeatMap
HeatMap(data = joined_data[['geo.latitude', 'geo.longitude','people_in']]).add_to(seoul_in)
seoul_in.save(r"C:\Users\1\.conda\envs\Bigdata\data/seoul_in.html")
seoul_out = folium.Map(location=[37.55, 126.98], zoom_start=12)
HeatMap(data = joined_data[['geo.latitude', 'geo.longitude','people_out']]).add_to(seoul_out)
seoul_out.save(r"C:\Users\1\.conda\envs\Bigdata\data/seoul_out.html")
morning_data =data[pd.to_datetime(data.timestamp).dt.hour< 9]
evening_data = data[pd.to_datetime(data.timestamp).dt.hour > 17]
noon_data = data[(pd.to_datetime(data.timestamp).dt.hour > 11) & (pd.to_datetime(data.timestamp).dt.hour < 14)]


morning_station_sum = morning_data.groupby("station_code").sum()
evening_station_sum = evening_data.groupby("station_code").sum()
noon_station_sum = noon_data.groupby("station_code").sum()

morning_joined_data = morning_station_sum.join(station_info)
evening_joined_data = evening_station_sum.join(station_info)
noon_joined_data = noon_station_sum.join(station_info)

morning_seoul_in = folium.Map(location=[37.55, 126.98], zoom_start=12)
HeatMap(data=morning_joined_data[['geo.latitude', 'geo.longitude','people_in']]).add_to(morning_seoul_in)
morning_seoul_in.save(r"C:\Users\1\.conda\envs\Bigdata\data\morning_seoul_in.html")

morning_seoul_out = folium.Map(location=[37.55, 126.98], zoom_start=12)
HeatMap(data=morning_joined_data[['geo.latitude', 'geo.longitude','people_out']]).add_to(morning_seoul_out)
morning_seoul_out.save(r"C:\Users\1\.conda\envs\Bigdata\data\morning_seoul_out.html")

evening_seoul_in = folium.Map(location=[37.55, 126.98], zoom_start=12)
HeatMap(data=evening_joined_data[['geo.latitude', 'geo.longitude','people_in']]).add_to(evening_seoul_in)
evening_seoul_in.save(r"C:\Users\1\.conda\envs\Bigdata\data\evening_seoul_in.html")

evening_seoul_out = folium.Map(location=[37.55, 126.98], zoom_start=12)
HeatMap(data=evening_joined_data[['geo.latitude', 'geo.longitude','people_out']]).add_to(evening_seoul_out)
evening_seoul_out.save(r"C:\Users\1\.conda\envs\Bigdata\data\evening_seoul_out.html")

noon_seoul_in = folium.Map(location=[37.55, 126.98], zoom_start=12)
HeatMap(data=noon_joined_data[['geo.latitude', 'geo.longitude','people_out']]).add_to(noon_seoul_in)
noon_seoul_in.save(r"C:\Users\1\.conda\envs\Bigdata\data\noon_seoul_in.html")

noon_seoul_out = folium.Map(location=[37.55, 126.98], zoom_start=12)
HeatMap(data=noon_joined_data[['geo.latitude', 'geo.longitude','people_out']]).add_to(noon_seoul_out)
noon_seoul_out.save(r"C:\Users\1\.conda\envs\Bigdata\data\noon_seoul_out.html")





