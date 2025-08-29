from pydantic import BaseModel

class BoundsSchema(BaseModel):
    north: float
    south: float
    east: float
    west: float

class CentroidSchema(BaseModel):
    lat: float
    lng: float

class ProcessedCoordinatesOut(BaseModel):
    centroid: CentroidSchema
    bounds: BoundsSchema
