import socket
import json
import time
import random

LAPTOP_IP = "174.220.59.176"
PORT = 5055

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:

    packet = {
        "source":"polhemus",
        "trial":1,
        "condition":"baseline",
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

