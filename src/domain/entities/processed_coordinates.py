from src.domain.entities.centroid import Centroid
from src.domain.entities.bounds import Bounds

class ProcessedCoordinates:
    def __init__(self, centroid: Centroid, bounds: Bounds):
        self.centroid = centroid
        self.bounds = bounds

    def __repr__(self):
        return f"CoordinatesResult(centroid={self.centroid}, bounds={self.bounds})"
