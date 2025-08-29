from typing import List

from src.domain.entities.point import Point
from src.domain.entities.centroid import Centroid
from src.domain.entities.bounds import Bounds
from src.domain.entities.processed_coordinates import ProcessedCoordinates

class ProcessCoordinatesUseCase:
	def execute(self, points: List[Point]) -> ProcessedCoordinates:
		if not points:
			raise ValueError("La lista de puntos no puede estar vacía.")
		
		lats = [p.lat for p in points]
		lngs = [p.lng for p in points]

		centroid = Centroid(lat=sum(lats)/len(lats), lng=sum(lngs)/len(lngs))
		bounds = Bounds(north=max(lats), south=min(lats), east=max(lngs), west=min(lngs))

		return ProcessedCoordinates(centroid=centroid, bounds=bounds)
