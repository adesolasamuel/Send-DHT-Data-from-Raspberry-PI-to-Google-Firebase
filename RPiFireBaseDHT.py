# 2022 Adesola Samuel

import time
import board
import adafruit_dht
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



# Initial the dht device, with data pin connected to:
dhtDevice = adafruit_dht.DHT11(board.D4)

# you can pass DHT22 use_pulseio=False if you wouldn't like to use pulseio.
# This may be necessary on a Linux single board computer like the Raspberry Pi,
# but it will not work in CircuitPython.
dhtDevice = adafruit_dht.DHT11(board.D4, use_pulseio=False)

while True:
    try:
        # Print the values to the serial port
        temperature_c = dhtDevice.temperature
        temperature_f = temperature_c * (9 / 5) + 32
        humidity = dhtDevice.humidity
        print(
            "Temp: {:.1f} F / {:.1f} C    Humidity: {}% ".format(
                temperature_f, temperature_c, humidity
            )
        )
        data = {
        "Temperature" : temperature_c,
        "Humidity" : humidity
        }
        db.child("Status").push(data)

        db.update(data)
        print("Sent to Firebase")

    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error

    time.sleep(2.0)

