import logging
import time
from functools import wraps
from typing import Callable

logging.getLogger(__name__)

def timelog(func: Callable) -> Callable:

    @wraps(func)
    async def wrapper(*args, **kwargs):
        start = time.perf_counter()

        result = await func(*args, **kwargs)

        print(f"Время выполнения: {time.perf_counter() - start:.3f}")
        logging.info(f"Время выполнения: {time.perf_counter() - start:.3f}")

        return result

    return wrapper