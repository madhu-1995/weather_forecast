import sys
from Coordinate_class import Coordinates
import threading
import time
from country_list2 import my_list
import random
start=time.time()
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
            def get_latlon(buffer):
                cc=Coordinates(buffer[0][0],buffer[0][1])
                latitude_longitude=cc.calc()
                buffer.append(latitude_longitude)
            def get_temp(buffer):
                num=Coordinates(buffer[0][1],buffer[0][1])
                num.calc()
            buffer=[]
            producer=threading.Thread(target=get_latlon,args=(buffer,))
            producer.start()
            producer.join()
            consumer=threading.Thread(target=get_temp,args=(buffer,))
            consumer.start()
            consumer.join()


def any_city(key1,value1):
    def get_latlon(buffer):
         random_key_value=Coordinates(key1,value1)
         latitude_longitude=random_key_value.calc()
         buffer.append(latitude_longitude)
    def get_temp(buffer):
         temp=Coordinates(buffer[0][0],buffer[0][1])
         temp.lat_lon()
    buffer=[]
    producer=threading.Thread(target=get_latlon,args=(buffer,))
    producer.start()
    producer.join()
    consumer=threading.Thread(target=get_temp,args=(buffer,))
    consumer.start()
    consumer.join()


def command_line_inputs(name,code):
        def get_detail(buffer):
            commandprompt_name=Coordinates(name,code)
            latitude_longitude=commandprompt_name.calc()
            buffer.append(latitude_longitude)
        def get_temp(buffer):
             temp=Coordinates(buffer[0][0],buffer[0][1])
             temp.lat_lon()
        buffer=[]
        producer=threading.Thread(target=get_detail,args=(buffer,))
        producer.start()
        producer.join()
        consumer=threading.Thread(target=get_temp,args=(buffer,))
        consumer.start()
        consumer.join()
















main()
end=time.time()
print(end-start)