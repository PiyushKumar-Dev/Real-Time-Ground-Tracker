import random
import time
from datetime import datetime, timedelta


class TelemetrySimulator:

    def __init__(self):

        # Start Time
        self.time = datetime.strptime("11:15:12", "%H:%M:%S")

        # Starting Coordinates (inside your map)
        self.lat = 1258013
        self.lon = 7742017
        self.altitude = 909

        # Movement Direction
        self.lat_direction = 1
        self.lon_direction = 1

        # Vehicle stop counter
        self.stop_counter = 0

    def move_vehicle(self):

        # Vehicle is stopped
        if self.stop_counter > 0:
            self.stop_counter -= 1
            return

        # Random stop (about once every 50 packets)
        if random.randint(1, 50) == 1:
            self.stop_counter = random.randint(2, 5)
            return

        # Occasionally change direction
        if random.randint(1, 20) == 1:
            self.lat_direction *= random.choice([-1, 1])
            self.lon_direction *= random.choice([-1, 1])

        # Small movement
        self.lat += self.lat_direction * random.randint(0, 2)
        self.lon += self.lon_direction * random.randint(0, 3)

        # Keep inside map limits
        self.lat = max(1257000, min(1261000, self.lat))
        self.lon = max(7740000, min(7745000, self.lon))

        # Small altitude variation
        self.altitude += random.randint(-1, 1)

    def get_next_packet(self):

        # Move vehicle
        self.move_vehicle()

        latitude = f"{self.lat:07d}N"
        longitude = f"{self.lon:08d}E"

        header = (
            f"1:Fm VU3TJD To VU2URC "
            f"<UI R Pid=F0 Len=28> "
            f"[{self.time.strftime('%H:%M:%S')}R]"
        )

        payload = (
            f"${self.time.strftime('%H%M%S')}"
            f"{latitude}"
            f"{longitude}"
            f"{self.altitude:03d}."
        )

        self.time += timedelta(seconds=10)

        return header + "\n" + payload


if __name__ == "__main__":

    simulator = TelemetrySimulator()

    while True:

        packet = simulator.get_next_packet()

        print(packet)
        print("-" * 70)

        time.sleep(10)