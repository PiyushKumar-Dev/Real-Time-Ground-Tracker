from telemetry_simulator import TelemetrySimulator
from packet_cleaner import PacketCleaner
import time

simulator = TelemetrySimulator()
cleaner = PacketCleaner()

while True:

    raw_packet = simulator.get_next_packet()

    print("\nRAW PACKET")
    print(raw_packet)

    clean_packet = cleaner.clean_packet(raw_packet)

    print("\nCLEAN PACKET")
    print(clean_packet)

    print("=" * 80)

    time.sleep(10)