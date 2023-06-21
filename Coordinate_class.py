import json
import requests
def converter(n):
    C=n-273.15
    return C
class Coordinates:
    def __init__(self,name,code):
        self.name=name
        self.code=code
    def __str__(self):
        return f"{self.name} {self.code}"
    def calc(self):
        global latitude,longitude,key
        key="3d2b0de8eeecb965115c17dfe3543321"
        link="http://api.openweathermap.org/geo/1.0/direct?q="
        actual_link=link+self.name+","+self.code+"&limit=10"+"&appid="+key
        response=requests.get(actual_link)
        city_coordinates=response.json()
        for lat1 in city_coordinates:
            latitude=str(lat1['lat'])
            longitude=str(lat1['lon'])
        return [latitude,longitude]
    def lat_lon(self):
        key="3d2b0de8eeecb965115c17dfe3543321"
        link2="https://api.openweathermap.org/data/2.5/weather?lat="
        actual_link2=link2+latitude+"&lon="+longitude+"&appid="+key
        response2=requests.get(actual_link2)
        city_api=response2.json()
        converting=city_api["main"]["temp"]
        min_temp=city_api["main"]["temp_min"]
        max_temp=city_api["main"]["temp_max"]
        print(f"Current_temperature:{converter(converting)}°c")
        print(f"Maximum_temperature:{converter(min_temp)}°c")
        print(f"Minimum_temperature:{converter(max_temp)}°c")