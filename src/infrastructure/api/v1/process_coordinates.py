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
    ]
)

@router.post("/process", response_model=ProcessedCoordinatesOut, status_code=status.HTTP_200_OK)
def process_coordinates(payload: PointsInputSchema, service:ProcessCoordinatesService = Depends(get_process_coordinates_service)):
    return service.process_coordinates(payload)
