import csv
import random
import time
from datetime import datetime

FILE_PATH = "data/sensor_data.csv"

# Write header once
with open(FILE_PATH, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Timestamp", "Temperature", "Pressure"])

print("Simulating sensor data... Press Ctrl+C to stop.")

try:
    while True:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        temperature = round(random.uniform(60, 120), 2)
        pressure = round(random.uniform(900, 1100), 2)

        with open(FILE_PATH, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([timestamp, temperature, pressure])

        time.sleep(1)
except KeyboardInterrupt:
    print("Data generation stopped.")
