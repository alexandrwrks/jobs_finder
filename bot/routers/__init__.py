from .request import router as query_router
from .start import router as start_router

routers = [
    start_router,
    query_router,
]