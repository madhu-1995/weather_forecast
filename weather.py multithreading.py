import sys
from concurrent.futures import ThreadPoolExecutor
import json
import time
import requests
from country_list2 import my_list
import random
start=time.time()
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
def main():
    global name,code
    if len(sys.argv)>1:
        for _ in sys.argv[1: ]:
            name=_
            code=" "
            command_line_inputs(name,code)
    elif len(sys.argv)==1:
        name=input("City_name: ")
        code=input("Country_code: ")
        if not name:
            i=0
            while i<5:
                global key1,value1
                key1,value1=random.choice(list(my_list.items()))
                print(value1)
                any_city(key1,value1)
                i+=1
        else:
            coordinates(name,code)
def converter(n):
    C=n-273.15
    return C
def coordinates(name,code):
            def get_temp(numbers):
                num=Coordinates(numbers[0],numbers[1])
                ans=num.lat_lon()
            def get_latlon():
                global numbers
                parallels1=Coordinates(name,code)
                numbers=parallels1.calc()
                get_temp(list(numbers))
            def thread():
                 with ThreadPoolExecutor() as executor:
                      future=executor.submit(get_latlon)
                      future1=executor.submit(get_temp)
            thread()


def any_city(key1,value1):
    def get_latlon():
         global ans
         key_value=Coordinates(key1,value1)
         ans=key_value.calc()
         return list(ans)
    def get_temp():
         get_latlon()
         temp=Coordinates(ans[0],ans[1])
         temp.lat_lon()
    def thread():
            with ThreadPoolExecutor() as executor:
                future=executor.submit(get_latlon)
                future1=executor.submit(get_temp)
    thread()


def command_line_inputs(name,code):
        def get_detail():
            global ans2
            comm_name=Coordinates(name,code)
            ans2=comm_name.calc()
            return ans2
        def get_temp():
             get_detail()
             ans3=Coordinates(ans2[0],ans2[1])
             ans3.lat_lon()
        def thread():
             with ThreadPoolExecutor() as executor:
                  future=executor.submit(get_detail)
                  future1=executor.submit(get_temp)
        thread()















main()
end=time.time()
print(end-start)