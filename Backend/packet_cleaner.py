class PacketCleaner:

    def clean_packet(self, raw_packet):

        lines = raw_packet.strip().split("\n")

        if len(lines) != 2:
            return None

        header = lines[0]
        payload = lines[1]

        payload = payload.strip("$.")
        
        source = header.split("Fm ")[1].split(" To")[0]
        destination = header.split("To ")[1].split(" <")[0]

        cleaned = {

            "source": source,

            "destination": destination,

            "time": payload[0:6],

            "latitude": payload[6:14],

            "longitude": payload[14:23],

            "altitude": int(payload[23:])

        }

        return cleaned