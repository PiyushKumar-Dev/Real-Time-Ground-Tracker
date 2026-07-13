from flask import Flask, send_file
import sqlite3
import io

app = Flask(__name__)

DATABASE = "../MapData/VehicleTracker.mbtiles"


@app.route("/")
def home():

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT zoom_level, tile_column, tile_row
        FROM tiles
        LIMIT 10
    """)

    rows = cursor.fetchall()

    conn.close()

    result = ""

    for zoom, col, row in rows:
        result += f"Zoom: {zoom}, X: {col}, Y: {row}<br>"

    return result

@app.route("/tile/<int:z>/<int:x>/<int:y>")
def get_tile(z, x, y):

    tms_y = (2 ** z - 1) - y

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT tile_data
        FROM tiles
        WHERE zoom_level=?
        AND tile_column=?
        AND tile_row=?
    """,(z,x,tms_y))

    row = cursor.fetchone()

    conn.close()

    if row is None:
        return "Tile Not Found",404

    return send_file(
        io.BytesIO(row[0]),
        mimetype="image/png"
    )


if __name__ == "__main__":
    app.run(debug=True)