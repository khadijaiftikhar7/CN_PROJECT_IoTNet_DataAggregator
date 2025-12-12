import paho.mqtt.client as mqtt
import json
import random
import time
from datetime import datetime

# MQTT broker settings
broker = "localhost"
port = 1883

# Connect to broker
client = mqtt.Client()
client.connect(broker, port)

# Locations and sensors
locations = {
    "CR-24": ["temp", "humidity", "occupancy", "noise", "light"],
    "CR-25": ["temp", "humidity", "occupancy", "noise", "light"],
    "CR-26": ["temp", "humidity", "occupancy", "noise", "light"],
    "CR-27": ["temp", "humidity", "occupancy", "noise", "light"],
    "CR-28": ["temp", "humidity", "occupancy", "noise", "light"],
    "Lab-10": ["temp", "humidity", "co2", "occupancy", "status"],
    "Lab-11": ["temp", "humidity", "co2", "occupancy", "status"],
    "Lab-12": ["temp", "humidity", "co2", "occupancy", "status"]
}

# Function to generate random sensor values
def generate_value(sensor):
    if sensor == "temp":
        return round(random.uniform(20, 30), 2)
    elif sensor == "humidity":
        return round(random.uniform(40, 70), 2)
    elif sensor == "co2":
        return round(random.uniform(300, 1000), 2)
    elif sensor == "occupancy":
        return random.randint(0, 30)
    elif sensor == "noise":
        return round(random.uniform(30, 80), 2)
    elif sensor == "light":
        return round(random.uniform(100, 1000), 2)
    elif sensor == "status":
        return random.choice(["ok", "warning", "error"])
    else:
        return None

# Simulation loop
try:
    while True:
        for room, sensors in locations.items():
            # Combine all sensor readings for this room into one message
            message = {"room": room, "timestamp": datetime.now().isoformat()}
            for sensor in sensors:
                message[sensor] = generate_value(sensor)
            
            topic = f"campus/{room}/all_sensors"
            client.publish(topic, json.dumps(message))
            print(f"Sent: {message} to topic {topic}")
        
        time.sleep(5)  # send every 5 seconds
except KeyboardInterrupt:
    print("Simulation stopped.")
