import requests
import random
import time
import os

TARGET_URL = os.getenv("TARGET_URL", "http://127.0.0.1:5000/sensor")

while True:
    temp = round(random.uniform(20, 30), 2)
    humidity = round(random.uniform(40, 70), 2)
    data = {"temperature": temp, "humidity": humidity}

    try:
        response = requests.post(TARGET_URL, json=data)
        print(f"Sent: {data}, Status: {response.status_code}")
    except Exception as e:
        print(f"Failed to send: {e}")

    time.sleep(2)
