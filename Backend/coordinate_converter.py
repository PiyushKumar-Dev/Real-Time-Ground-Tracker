class CoordinateConverter:

    @staticmethod
    def convert_latitude(lat):

        value = lat[:-1]
        direction = lat[-1]

        degree = int(value[:2])
        minute = float(value[2:]) / 1000

        decimal = degree + minute / 60

        if direction == "S":
            decimal *= -1

        return round(decimal, 6)


    @staticmethod
    def convert_longitude(lon):

        value = lon[:-1]
        direction = lon[-1]

        degree = int(value[:3])
        minute = float(value[3:]) / 1000

        decimal = degree + minute / 60

        if direction == "W":
            decimal *= -1

        return round(decimal, 6)