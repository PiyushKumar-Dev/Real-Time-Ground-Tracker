from flask import Flask, send_file, jsonify, send_from_directory
import sqlite3
import io

from telemetry_simulator import TelemetrySimulator
from packet_cleaner import PacketCleaner
from packet_validator import PacketValidator
from coordinate_converter import CoordinateConverter

app = Flask(__name__)

DATABASE = "../MapData/VehicleTracker.mbtiles"

# -----------------------------
# Create Objects
# -----------------------------
simulator = TelemetrySimulator()
cleaner = PacketCleaner()
validator = PacketValidator()


# -----------------------------
# Home Route
# -----------------------------
@app.route("/")
def home():
    return send_from_directory("../Frontend", "index.html")


@app.route("/script.js")
def script():
    return send_from_directory("../Frontend", "script.js")


@app.route("/style.css")
def style():
    return send_from_directory("../Frontend", "style.css")

@app.route("/leaflet/dist/<path:filename>")
def leaflet(filename):
    return send_from_directory("../Frontend/leaflet/dist", filename)


# -----------------------------
# Tile Route
# -----------------------------
@app.route("/tile/<int:z>/<int:x>/<int:y>")
def get_tile(z, x, y):

    # Convert XYZ -> TMS
    tms_y = (2 ** z - 1) - y

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT tile_data
        FROM tiles
        WHERE zoom_level=?
        AND tile_column=?
        AND tile_row=?
    """, (z, x, tms_y))

    row = cursor.fetchone()

    conn.close()

    if row is None:
        return "Tile Not Found", 404

    return send_file(
        io.BytesIO(row[0]),
        mimetype="image/png"
    )


# -----------------------------
# Telemetry Route
# -----------------------------
@app.route("/telemetry")
def telemetry():

    # Get next telemetry packet
    raw_packet = simulator.get_next_packet()

    # Clean packet
    cleaned_packet = cleaner.clean_packet(raw_packet)

    # Validate packet
    validation = validator.validate(cleaned_packet)

    if not validation["valid"]:
        return jsonify(validation), 400

    # Convert Coordinates
    cleaned_packet["latitude"] = CoordinateConverter.convert_latitude(
        cleaned_packet["latitude"]
    )

    cleaned_packet["longitude"] = CoordinateConverter.convert_longitude(
        cleaned_packet["longitude"]
    )

    return jsonify(cleaned_packet)


# -----------------------------
# Run Flask
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)