from src.domain.entities.processed_coordinates import ProcessedCoordinates
from src.services.schemas.processed_coordinates_schema import ProcessedCoordinatesOut, CentroidSchema, BoundsSchema

class ProcessedCoordinatesMapper:
	@staticmethod
	def to_schema(entity: ProcessedCoordinates) -> ProcessedCoordinatesOut:
		centroid = CentroidSchema(lat=entity.centroid.lat, lng=entity.centroid.lng)
		bounds = BoundsSchema(
			north=entity.bounds.north,
			south=entity.bounds.south,
			east=entity.bounds.east,
			west=entity.bounds.west
		)
		return ProcessedCoordinatesOut(centroid=centroid, bounds=bounds)
