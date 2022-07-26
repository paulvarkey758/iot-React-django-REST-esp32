import network
import urequests
from machine import Pin
led1=Pin(2,Pin.OUT)
led2=Pin(4,Pin.OUT)
led3=Pin(15,Pin.OUT)
wifi=network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect("poyi recharge cheyyada","12345654321")
while not wifi.isconnected():
    print("connecting...")
    
if wifi.isconnected():
    print("connected")
    print(wifi.ifconfig())
    
    while True:
        url="https://paulkv.pythonanywhere.com/api/read-data/"
        data=urequests.get(url).json()
        print(data)
        for i in data:
            if i['name']=="led1":
                led1.value(i['status'])
            if i['name']=="led2":
                led2.value(i['status'])
            if i['name']=="led3":
                led3.value(i['status'])

