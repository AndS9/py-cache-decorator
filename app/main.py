from typing import Callable, Any
# from functools import wraps


def cache(func: Callable) -> Callable:
    # @wraps(func)
    cache_results = {}

    def inner(*args, **kwargs) -> Any:
        if kwargs:
            print("This function can't operate with keyword arguments")
            return None

        if args in cache_results.keys():
            print("Getting from cache")
            return cache_results[args]

        result = func(*args, **kwargs)
        cache_results[args] = result
        print("Calculating new result")
        return result
    return inner
