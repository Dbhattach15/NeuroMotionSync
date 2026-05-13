import socket
import json
import sqlite3
import time

UDP_IP = "0.0.0.0"
UDP_PORT = 5055

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind((UDP_IP, UDP_PORT))

print("Listening for incoming data...")

def save_packet(packet):

    conn = sqlite3.connect("../data/motion_data.db")

    cursor = conn.cursor()

    laptop_timestamp = time.time()

    cursor.execute("""
    INSERT INTO motion_data
    (laptop_timestamp, source, trial, condition, sensor, x, y, z)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        laptop_timestamp,
        packet["source"],
        packet["trial"],
        packet["condition"],
        packet["sensor"],
        packet["x"],
        packet["y"],
        packet["z"]
    ))

    conn.commit()
    conn.close()

while True:

    data, addr = sock.recvfrom(4096)

    packet = json.loads(data.decode())

    print(packet)

    save_packet(packet)
