import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect("../data/motion_data.db")

df = pd.read_sql_query(
    "SELECT * FROM motion_data",
    conn
)

conn.close()

polhemus = df[df["source"]=="polhemus"]
vr = df[df["source"]=="vr"]

plt.figure(figsize=(10,6))

plt.plot(
    polhemus["laptop_timestamp"],
    polhemus["x"],
    label="Polhemus"
)

plt.plot(
    vr["laptop_timestamp"],
    vr["x"],
    label="VR"
)

plt.xlabel("Time")
plt.ylabel("Thumb X Position")

plt.title("Real vs Virtual Finger Tracking")

plt.legend()

plt.savefig("../plots/finger_tracking.png")

plt.show()

