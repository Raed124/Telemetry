from api_key import Api_Key
import requests as r 
import re 
import psutil 
from psutil._common import bytes2human
import os

def Get_Weather():
    ip = Get_IP()
    example_url ="http://api.weatherapi.com/v1/current.json?key="+Api_Key+"&q=" + ip
    Ans = r.get(example_url)
    Temperature = Ans.json()['current']['temp_c']
    Condition = Ans.json()['current']['condition']['text']
    return (Temperature,Condition)

def Get_IP():
    Address = r.get('http://checkip.dyndns.com/')
    return re.compile(r'Address: (\d+\.\d+\.\d+\.\d+)').search(Address.text).group(1)


def Get_Mem():
    mem = psutil.virtual_memory()
    Percent = mem[2]
    return (f"Memoru Usage : {Percent} %")

def Get_Disk():
    Disk = psutil.disk_usage('/') 
    Usage = int(Disk.percent)
    return (f"Disk Usage : {Usage} %") 


print(Get_Disk())