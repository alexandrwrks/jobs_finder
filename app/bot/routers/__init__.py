from .query import router as query_router
from .start import router as start_router
from .grades import router as grades_router

routers = [
    start_router,
    query_router,
    grades_router,
]