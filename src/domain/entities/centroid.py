class Centroid:
    def __init__(self, lat: float, lng: float):
        self.lat = lat
        self.lng = lng

    def __repr__(self):
        return f"Centroid(lat={self.lat}, lng={self.lng})"
