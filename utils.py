import random
import math


def roll_dice(sides=6, num_dice=1):
    """Roll num_dice dice with a given number of sides."""
    return [random.randint(1, sides) for _ in range(num_dice)]


def calculate_distance(point_a, point_b):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((point_a[0] - point_b[0]) ** 2 + (point_a[1] - point_b[1]) ** 2)


def get_random_element(elements):
    """Return a random element from a non-empty list."""
    if not elements:
        raise ValueError('The elements list cannot be empty.')
    return random.choice(elements)


def normalize_angle(angle):
    """Normalize an angle to the range [0, 360) degrees."""
    return angle % 360


def lmap(func, iterable):
    """Apply a function to all items in an iterable and return a list."""
    return list(map(func, iterable))