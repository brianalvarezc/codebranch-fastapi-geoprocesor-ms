from typing import Any

class Point:
    def __init__(self, lat: float, lng: float):
        self.lat = lat
        self.lng = lng

    def __repr__(self):
        return f"Point(lat={self.lat}, lng={self.lng})"
