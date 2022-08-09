import network
import urequests
from machine import Pin
import dht

lamp=Pin(2,Pin.OUT)
fan1=Pin(4,Pin.OUT)
fan2=Pin(15,Pin.OUT)
pump1=Pin(16,Pin.OUT)
pump2=Pin(17,Pin.OUT)
dht_sensor=dht.DHT11(Pin(33))
temp=0
hum=0
fan2.value(False)
pump2.value(False)
wifi=network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect("poyi recharge cheyyada","12345654321")
while not wifi.isconnected():
    print("connecting...")

def put_data(id,name,t):
    data={"name":name,"value":t}
    resp=urequests.put(f'https://paulkvarkey.pythonanywhere.com/api/sensor-write/{id}/',json=data).json()

def sense_data():
    try:
        dht_sensor.measure()
        temp=dht_sensor.temperature()
        hum=dht_sensor.humidity()
        print("Temperature: ",temp)
        print("Humidity: ",hum)
    except:
        temp=0
        hum=0
    finally:    
        put_data(2,"temperature",temp) #2 is the field id of temperature
        put_data(3,"humidity",hum) #3 is the field is of humidity
    
    
    

if wifi.isconnected():
    print("connected")
    print(wifi.ifconfig())
    while True:
        #block for controlling appliances
        resp=urequests.get('https://paulkvarkey.pythonanywhere.com/api/read-data/').json()
        for i in resp:
            if i['name']=="lamp":
                lamp.value(i['status'])
            if i['name']=="fan":
                fan1.value(i['status'])
            if i['name']=="pump":
                pump1.value(i['status'])
        
        #function for sense data
        sense_data()        
                
    

