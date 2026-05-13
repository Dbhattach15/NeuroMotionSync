import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import time

plt.ion()

while True:
    conn = sqlite3.connect("../data/motion_data.db")
    df = pd.read_sql_query("SELECT * FROM motion_data", conn)
    conn.close()

    if len(df) > 0:
        plt.clf()

        polhemus = df[df["source"] == "polhemus"]
        vr = df[df["source"] == "vr"]

        if len(polhemus) > 0:
            plt.plot(
                polhemus["laptop_timestamp"],
                polhemus["x"],
                label="Windows / Polhemus X"
            )

        if len(vr) > 0:
            plt.plot(
                vr["laptop_timestamp"],
                vr["x"],
                label="Ubuntu / VR X"
            )

        plt.xlabel("Laptop Timestamp")
        plt.ylabel("Finger X Position")
        plt.title("Live Real vs Virtual Finger Tracking")
        plt.legend()
        plt.pause(0.5)

    time.sleep(0.5)
