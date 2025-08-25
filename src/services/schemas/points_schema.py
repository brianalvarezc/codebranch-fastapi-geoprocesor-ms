from pydantic import BaseModel
from typing import List

class PointSchema(BaseModel):
    lat: float
    lng: float

class PointsInputSchema(BaseModel):
    points: List[PointSchema]
