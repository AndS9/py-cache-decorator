from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_results = {}

    def inner(*args) -> Any:
        if args in cache_results:
            print("Getting from cache")
            return cache_results[args]

        result = func(*args)
        cache_results[args] = result
        print("Calculating new result")
        return result
    return inner
