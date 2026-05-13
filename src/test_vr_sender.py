import socket
import json
import time
import random

LAPTOP_IP = "192.168.1.5"
PORT = 5055

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:

    packet = {
        "source":"vr",
        "trial":1,
        "condition":"temporal_lag",
        "sensor":"thumb",
        "x":random.uniform(0,1),
        "y":random.uniform(0,1),
        "z":random.uniform(0,1)
    }

    sock.sendto(
        json.dumps(packet).encode(),
        (LAPTOP_IP, PORT)
    )

    time.sleep(0.02)
