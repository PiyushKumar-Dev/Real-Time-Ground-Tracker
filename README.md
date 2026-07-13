# 🚗 Real-Time Ground Tracker

An offline ground vehicle tracking system that visualizes real-time vehicle telemetry on OpenStreetMap using locally stored MBTiles. The application is designed to operate without an internet connection by serving map tiles through a Flask backend and rendering them with Leaflet.js.

## ✨ Features

- 🗺️ Offline map rendering using MBTiles
- 🔍 Interactive zoom and pan
- ⚡ Flask-based tile server
- 🗄️ SQLite (MBTiles) integration
- 🌍 OpenStreetMap support
- 📍 Vehicle marker visualization
- 📡 Real-time telemetry integration (In Progress)
- 🛣️ Vehicle path visualization (In Progress)

## 🛠️ Tech Stack

- Python
- Flask
- SQLite (MBTiles)
- Leaflet.js
- HTML5
- CSS3
- JavaScript
- OpenStreetMap
- MOBAC (Mobile Atlas Creator)

## 📂 Project Structure

```
Real-Time-Ground-Tracker/
│
├── Backend/
│   └── app.py
│
├── Frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── MapData/
│   └── VehicleTracker.mbtiles
│
└── README.md
```

## 🚀 Current Progress

- ✅ Downloaded offline OpenStreetMap tiles
- ✅ Generated MBTiles database
- ✅ Implemented Flask backend
- ✅ Read MBTiles using SQLite
- ✅ Built tile-serving API
- ✅ Integrated Leaflet frontend
- ✅ Offline map rendering
- ✅ Zoom and pan support

## 📋 Upcoming Features

- [ ] Real-time vehicle marker
- [ ] Telemetry packet parser
- [ ] Live GPS tracking
- [ ] Vehicle path visualization
- [ ] TCP socket integration
- [ ] Multiple vehicle support

## 📸 Demo

*Screenshots and demo GIF will be added after completing the tracking module.*

## 📄 License

This project is developed for educational and research purposes.