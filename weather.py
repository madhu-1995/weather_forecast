import sys
import requests
import json
import country_list1
import random
def main():
        city_name=input("City Name: ")
        country_code=input("ISO Country code: ")
        if len(city_name)==0:
             any_city()
        else:
             coordinates(city_name,country_code)
#Function to convert Kelvin to Celsius
def converter(n):
    C=n-273.15
    return C
#API Key
def coordinates(city_name,country_code):
    global latitude,longitude
    key="3d2b0de8eeecb965115c17dfe3543321"
    link="http://api.openweathermap.org/geo/1.0/direct?q="
    actual_link=link+city_name+","+country_code+"&limit=10"+"&appid="+key
    response=requests.get(actual_link)
    city_coordinates=response.json()
    for lat1 in city_coordinates:
        latitude=str(lat1['lat'])
        longitude=str(lat1['lon'])
    link2="https://api.openweathermap.org/data/2.5/weather?lat="
    actual_link2=link2+latitude+"&lon="+longitude+"&appid="+key
    response2=requests.get(actual_link2)
    city_api=response2.json()
    converting=city_api["main"]["temp"]
    min_temp=city_api["main"]["temp_min"]
    max_temp=city_api["main"]["temp_max"]
    print(f'Current Temperature:{converter(converting)}°c')
    print(f'Minimum Temperature:{converter(min_temp)}°c')
    print(f'Maximum Temperature:{converter(max_temp)}°c')
#function to generates random city names and country code
def any_city():
     i=0
     while i<6:
         key1,value1=random.choice(list(country_list1.my_list.items()))
         print(value1.upper())
         coordinates(value1,key1)
         i=i+1
def command_line_inputs():
     n=len(sys.argv)
     i=0
     while i<n:
          city_name=str(sys.argv[1: ])
          country_code=" "
          coordinates(city_name,country_code)
          i+=n
          

main()

