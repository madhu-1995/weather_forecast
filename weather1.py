import requests
import sys
import json
#Function to convert Kelvin to Celsius
def converter(n):
    C=n-273.15
    return C
#API Key
key="3d2b0de8eeecb965115c17dfe3543321"
city_name=input("City Name: ")
#Country code according to ISO for India is IND
country_code=input("ISO Country code: ")
link="http://api.openweathermap.org/geo/1.0/direct?q="
actual_link=link+city_name+","+country_code+"&limit=10"+"&appid="+key
response=requests.get(actual_link)
o=response.json()
for lat1 in o:
    latitude=str(lat1['lat'])
    longitude=str(lat1['lon'])
link2="https://api.openweathermap.org/data/2.5/weather?lat="
actual_link2=link2+latitude+"&lon="+longitude+"&appid="+key
response2=requests.get(actual_link2)
f=response2.json()
converting=f["main"]["temp"]
min_temp=f["main"]["temp_min"]
max_temp=f["main"]["temp_max"]
print(f'Current Temperature:{converter(converting)}°c')
print(f'Minimum Temperature:{converter(min_temp)}°c')
print(f'Maximum Temperature:{converter(max_temp)}°c')

