#!/usr/bin/env python3
from api_key import Api_Key
import requests as r 
import re 
import psutil 
from psutil._common import bytes2human
import os
import datetime
import speedtest 


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


def Get_Network(Up = False):
    servers = []
    threads = 1
    s = speedtest.Speedtest()
    s.get_best_server()
    Download = s.download(threads=threads)
    Upload = s.upload(threads=threads)
    download_mbs = round(Download / (10**6), 2)
    upload_mbs = round(Upload / (10**6), 2)
    if(Up == True):
        return (f'Dow : {download_mbs}Mbits/ Up : {upload_mbs}Mbits')
    else: 
        return (f'Dow : {download_mbs}Mbits')


def Get_Time_Date():
    Date_Time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M') 
    return (Date_Time)
#print(Get_Disk())