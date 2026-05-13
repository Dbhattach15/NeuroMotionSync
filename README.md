# NeuroMotionSync

## Overview

NeuroMotionSync is a cross-platform neuroscience middleware framework designed to synchronize and compare real-world finger tracking data with virtual reality hand-tracking data in real time.

This project was developed to explore sensorimotor adaptation and multimodal motion synchronization by connecting systems that were not originally designed to communicate with one another.

The framework uses:

- Python
- UDP networking
- JSON packet streaming
- SQLite databases
- Real-time plotting and visualization

The system integrates:
- Windows-based Polhemus Liberty finger tracking
- Ubuntu-based VR hand tracking
- A laptop acting as the synchronization and database server

---

# Project Architecture

```text
Windows / Polhemus  ──UDP JSON──▶ Laptop Middleware Server
Ubuntu / VR         ──UDP JSON──▶ Laptop Middleware Server

Laptop:
- Receives both streams
- Applies synchronized timestamps
- Stores data in SQLite
- Plots real vs virtual motion
