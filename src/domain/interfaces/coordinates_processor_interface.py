from abc import ABC, abstractmethod
from typing import Any, List

class ICoordinatesProcessorGateway(ABC):
    @abstractmethod
    def process_coordinates(self, points: List[Any]) -> Any:
        pass
