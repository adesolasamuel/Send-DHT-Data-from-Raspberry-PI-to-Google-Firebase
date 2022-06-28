import pyrebase
import random

config = {
  "apiKey": "AIzaSyDoIQUbG8K0dZJWwYiXG4yrFD0at68HKbo",
  "authDomain": "rpi-dht-monitor.firebaseapp.com",
  "databaseURL": "https://rpi-dht-monitor-default-rtdb.firebaseio.com",
  "storageBucket": "rpi-dht-monitor.appspot.com"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

while True:
    data = {
    "Temp" : random.randrange(1, 10),
    "Hum" : random.randrange(10, 50)
    }

    db.child("Status").push(data)

    db.update(data)