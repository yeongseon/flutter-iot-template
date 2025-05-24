import requests
import time

while True:
    try:
        res = requests.post("http://backend:8000/data", json={"temperature": 23.5})
        print("Sent data:", res.status_code)
    except Exception as e:
        print("Error sending data:", e)
    time.sleep(5)
