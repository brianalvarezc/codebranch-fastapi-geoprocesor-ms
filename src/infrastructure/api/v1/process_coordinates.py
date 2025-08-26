from fastapi import APIRouter, status, Depends

from src.infrastructure.api.v1.auth import get_current_user
from src.services.schemas.points_schema import PointsInputSchema
from src.services.schemas.processed_coordinates_schema import ProcessedCoordinatesOut
from src.services.process_coordinates_service import ProcessCoordinatesService

def get_process_coordinates_service() -> ProcessCoordinatesService:
    return ProcessCoordinatesService()

router = APIRouter(
    dependencies=[
        # se descomenta si se va a usar autenticación siempre
        # Depends(get_current_user)
    ],
    tags=["Coordinates"]
)

@router.post(
    "/process",
    response_model=ProcessedCoordinatesOut,
    status_code=status.HTTP_200_OK,
    summary="Process geographic coordinates",
    description="Receives a list of points (latitude and longitude) and returns the centroid and geographic bounds (north, south, east, west)."
)
def process_coordinates(
    payload: PointsInputSchema,
    service: ProcessCoordinatesService = Depends(get_process_coordinates_service)
):
    """
    Process a list of geographic points and return centroid and bounds.

    - **Request body:** PointsInputSchema with a list of points (lat, lng).
    - **Returns:** ProcessedCoordinatesOut with centroid and bounds.
    - **Errors:**
        - 400: Invalid or empty points list.
        - 422: Validation error (missing lat/lng).
    """
    return service.process_coordinates(payload)
