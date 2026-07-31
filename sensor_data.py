import csv
import os
import random
from datetime import datetime

filename = "sensor_data.csv"

sensor_data = {
    "temperature": round(random.uniform(25.0, 35.0), 1),
    "humidity": random.randint(40, 80),
    "pressure": random.randint(1000, 1025),
    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
}

file_exists = os.path.isfile(filename)

with open(filename, "a", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=sensor_data.keys())

    if not file_exists:
        writer.writeheader()

    writer.writerow(sensor_data)

print("Sensor data uploaded to sensor_data.csv successfully!")