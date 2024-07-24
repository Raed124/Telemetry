#!/usr/bin/env python3
from api_key import Api_Key
import requests as r 
import re 
import psutil 
from psutil._common import bytes2human
import os
import datetime
import speedtest 
import typer


import pyfiglet
from colorama import Fore , Style
T  = "TELEMETRY"
ASCII_art_1 = pyfiglet.figlet_format(T,font='doom')
print(Fore.GREEN + Style.DIM + ASCII_art_1)

app = typer.Typer()


@app.command()
def Weather():
    ip = Get_IP()
    example_url ="http://api.weatherapi.com/v1/current.json?key="+Api_Key+"&q=" + ip
    Ans = r.get(example_url)
    Temperature = Ans.json()['current']['temp_c']
    Condition = Ans.json()['current']['condition']['text']
    print (Temperature,Condition)

def Get_IP():
    Address = r.get('http://checkip.dyndns.com/')
    return re.compile(r'Address: (\d+\.\d+\.\d+\.\d+)').search(Address.text).group(1)

@app.command()
def Memory():
    mem = psutil.virtual_memory()
    Percent = mem[2]
    print (f"Memory Usage : {Percent} %")

@app.command()
def Disk():
    Disk = psutil.disk_usage('/') 
    Usage = int(Disk.percent)
    print (f"Disk Usage : {Usage} %") 

@app.command()
def Network_Speed(Up : bool = False):
    servers = []
    threads = 1
    s = speedtest.Speedtest()
    s.get_best_server()
    Download = s.download(threads=threads)
    Upload = s.upload(threads=threads)
    download_mbs = round(Download / (10**6), 2)
    upload_mbs = round(Upload / (10**6), 2)
    if(Up == True):
        print (f'Dow : {download_mbs}Mbits/ Up : {upload_mbs}Mbits')
    else: 
        print (f'Dow : {download_mbs}Mbits')

@app.command()
def Time_Date():
    Date_Time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M') 
    print (Date_Time)

if __name__ == "__main__":
    app()
