from collections.abc import Callable
import functools
import time
import tracemalloc
from typing import Any


def measure_performance(func: Callable[[Any], Any]) -> None:
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        tracemalloc.start()

        result = func(*args, **kwargs)

        end_time = time.perf_counter()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        ellapsed_time = (end_time - start_time) * 1000

        print(f"Function '{func.__name__}' Performance Metrics:")
        print(f"- execution time: {ellapsed_time:.3f} ms")
        print(f"- memory usage: {current / 1024:.2f} KB / peak: {peak / 1024:.2f} KB")

        return result

    return wrapper
