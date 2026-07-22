import time

from telemetry_simulator import TelemetrySimulator
from packet_cleaner import PacketCleaner
from packet_validator import PacketValidator
from coordinate_converter import CoordinateConverter

simulator = TelemetrySimulator()
cleaner = PacketCleaner()
validator = PacketValidator()

while True:

    raw_packet = simulator.get_next_packet()

    print("\nRaw Packet")
    print(raw_packet)

    cleaned = cleaner.clean_packet(raw_packet)

    print("\nCleaned")
    print(cleaned)

    result = validator.validate(cleaned)

    print("\nValidation")
    print(result)

    if result["valid"]:

        cleaned["latitude"] = CoordinateConverter.convert_latitude(
            cleaned["latitude"]
        )

        cleaned["longitude"] = CoordinateConverter.convert_longitude(
            cleaned["longitude"]
        )

        print("\nConverted Coordinates")
        print(cleaned)

    # Wait 10 seconds before generating the next packet
    time.sleep(10)