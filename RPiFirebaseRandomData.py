import pyrebase
import random

config = {
  "apiKey": "WEB API KEY",
  "authDomain": "project-id.firebaseapp.com",
  "databaseURL": "RealtimeDatabase URL",
  "storageBucket": "project-id.appspot.com"
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
