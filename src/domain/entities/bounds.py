class Bounds:
    def __init__(self, north: float, south: float, east: float, west: float):
        self.north = north
        self.south = south
        self.east = east
        self.west = west

    def __repr__(self):
        return f"Bounds(north={self.north}, south={self.south}, east={self.east}, west={self.west})"
