import time
from datetime import datetime, timedelta


class TelemetrySimulator:

    def __init__(self):
        # Fixed starting values
        self.time = datetime.strptime("11:15:12", "%H:%M:%S")
        self.latitude = "1258013N"
        self.longitude = "07742017E"
        self.altitude = 909

    def get_next_packet(self):

        # Header
        header = (
            f"1:Fm VU3TJD To VU2URC "
            f"<UI R Pid=F0 Len=28> "
            f"[{self.time.strftime('%H:%M:%S')}R]"
        )

        # Telemetry Payload
        payload = (
            f"${self.time.strftime('%H%M%S')}"
            f"{self.latitude}"
            f"{self.longitude}"
            f"{self.altitude}."
        )

        # Increase time by 10 seconds for next packet
        self.time += timedelta(seconds=10)

        return header + "\n" + payload


if __name__ == "__main__":

    simulator = TelemetrySimulator()

    while True:
        print(simulator.get_next_packet())
        print("-" * 70)

        # Wait 10 seconds
        time.sleep(10)