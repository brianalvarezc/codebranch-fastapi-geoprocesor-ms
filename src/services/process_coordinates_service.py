from typing import List
from fastapi import HTTPException

from src.application.use_cases.process_coordinates_use_case import ProcessCoordinatesUseCase
from src.services.schemas.points_schema import PointSchema, PointsInputSchema
from src.services.schemas.processed_coordinates_schema import ProcessedCoordinatesOut
from src.domain.interfaces.coordinates_processor_interface import ICoordinatesProcessorGateway
from src.application.use_cases.process_coordinates_use_case import ProcessCoordinatesUseCase
from src.services.mappers.processed_coordinates_mapper import ProcessedCoordinatesMapper
from src.domain.entities.point import Point

class ProcessCoordinatesService(ICoordinatesProcessorGateway):
    def __init__(self):
        self.use_case = ProcessCoordinatesUseCase()

    def process_coordinates(self, payload: PointsInputSchema) -> ProcessedCoordinatesOut:
        points_data: List[PointSchema] = getattr(payload, 'points', [])

        if len(points_data) == 0:
            raise HTTPException(status_code=400, detail="Point list cannot be empty.")

        points = []
        for p in points_data:

            try:
                lat = float(p.lat)
                lng = float(p.lng)
            except (TypeError, ValueError):
                raise HTTPException(status_code=400, detail="Latitude and longitude must be numeric values.")

            points.append(Point(lat=lat, lng=lng))

        processed = self.use_case.execute(points)
            
        return ProcessedCoordinatesMapper.to_schema(processed)
