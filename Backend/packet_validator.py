class PacketValidator:

    @staticmethod
    def validate(packet):

        if packet is None:
            return {"valid": False, "reason": "Packet Missing"}

        if len(packet["time"]) != 6:
            return {"valid": False, "reason": "Invalid Time"}

        if not packet["latitude"].endswith(("N", "S")):
            return {"valid": False, "reason": "Invalid Latitude"}

        if not packet["longitude"].endswith(("E", "W")):
            return {"valid": False, "reason": "Invalid Longitude"}

        return {
            "valid": True,
            "reason": "Packet Valid"
        }