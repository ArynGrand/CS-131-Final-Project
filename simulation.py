import random
import requests
import time
import json

IP = "http://10.13.226.50:5000/SensorData" #"http://10.13.2.166:5000/SensorData" #"http://192.168.1.11:5000/SensorData" <- my laptop IP change depending on where it is sending

def SimulateSensor(): #function simulates random data for each category
    t =  round(random.uniform(20, 30), 2) #3rd number is how far it rounds we can change for more/less precision
    h = round(random.uniform(40, 60), 2)
    m = round(random.uniform(200, 800), 2)
    l = round(random.uniform(100, 1000), 2)
    data = { "Temperature": t, "Humidity": h, "Moisture": m , "Lighting": l}
    return data

running = True

while running:
    sensorData = SimulateSensor() #simulate data
    try:
        response = requests.post(IP, json=sensorData) #sends data to flask (replace the IP with where you want the server to be created)
        print("Sent data:", sensorData, "Response:", response.status_code) 
        time.sleep(2)
    except Exception as e: #if error send exception
        print("Error:", e)
    userDecision = input("Enter n to quit or anything to continue outputting random data: ")
    if userDecision == 'n':
       running = False