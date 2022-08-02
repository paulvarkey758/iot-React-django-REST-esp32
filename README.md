# iot-React-django-REST-esp32
<p>An IoT system which built with React Js as front end for user interaction. an api with Python Django Rest framework used as the backend of the system. All the appliances controlled by the ESP32 NodeMcu which programmed with Arduino sketch.</p>

<u><h2>The system is divided into three</h2></u>
<ol>
<li>Frontend</li>
<li>Backend/API</li>
<li>Embedded system</li>
</ol>

<h2>Frontend</h2>
<p>Frontend is a developed by using <b>REACT JS</b> and it is a responsive webapp which have buttons to control the home appliances.This app fetch data from the backend and also update the data to the backend/api</p>
<p>Frontend is given as another repository  and find it in the given link</p>
https://github.com/paulvarkey758/IoT-React-Js-Frontend

<h2>Backend</h2>
<p>Backend is developed by using <b>Python Django Rest framework</b> and it developed as an api with end pionts to read and write data.</p>
<p>Backend is given as another repository  and find it in the given link</p>
https://github.com/paulvarkey758/iot-django-backend

<h2>Embedded systems</h2>
<p>Here the <b>ESP32 NodeMcu</b> using as the brain of the system in which has inbuilt <b>WiFi</b> connectivity. The esp module is programmed by using <b>Micropython</b>. The micropython program access the backend/Api and fetch the data. according to the data the program controls devices connected to the esp modules through gpio pins. Also there is temperature and humidity sensor to sense the data and it will be updated on api. user can integrate more sensors with the system </p>
