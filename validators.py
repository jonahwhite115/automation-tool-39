import functools
from typing import Any, Callable

# Cache for input validation results to reduce overhead in game loops
_validation_cache = {}

@functools.lru_cache(maxsize=128)
def validate_input_sequence(sequence_id: int, input_data: tuple) -> bool:
    """Validates player input sequences using lru_cache for performance."""
    if not input_data:
        return False
    return len(input_data) > 0 and all(isinstance(i, (int, float)) for i in input_data)

def memoized_validator(func: Callable) -> Callable:
    """Decorator for caching repetitive game state validations."""
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = (args, frozenset(kwargs.items()))
        if key not in _validation_cache:
            _validation_cache[key] = func(*args, **kwargs)
        return _validation_cache[key]
    return wrapper

@memoized_validator
def check_resource_bounds(resource_key: str, value: int, min_val: int, max_val: int) -> bool:
    """Checks if resource levels are within safe operating bounds."""
    return min_val <= value <= max_val

def clear_validator_cache() -> None:
    """Clears global caches to prevent memory leaks during sessions."""
    _validation_cache.clear()
    validate_input_sequence.cache_clear()