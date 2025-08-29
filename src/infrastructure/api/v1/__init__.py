from .process_coordinates import router as coordinates_router
from .auth import router as auth_router

all_routers = [
    (auth_router, "/auth"),
    (coordinates_router, "/coordinates"),
]