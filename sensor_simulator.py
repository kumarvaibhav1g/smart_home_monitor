import requests
import random
import time

while True:
    temp = round(random.uniform(20, 30), 2)
    humidity = round(random.uniform(40, 70), 2)
    data = {"temperature": temp, "humidity": humidity}

    try:
        response = requests.post("http://127.0.0.1:5000/sensor", json=data)
        print(f"Sent: {data}, Status: {response.status_code}")
    except Exception as e:
        print(f"Failed to send: {e}")

    time.sleep(2)