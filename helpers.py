import random
from typing import Tuple

def calculate_click_point(bbox: Tuple[int, int, int, int], variance_pct: float = 0.1) -> Tuple[int, int]:
    """
    Calculates a randomized click coordinate within a bounding box
    to prevent anti-cheat engines from detecting static bot-like clicks.
    
    :param bbox: A tuple representing (x, y, width, height)
    :param variance_pct: Safety margin percentage to avoid clicking the very edge
    :return: A tuple of (x, y) coordinates
    """
    x, y, w, h = bbox
    
    # Restrict clicking boundaries to prevent clicking border pixels
    x_pad = int(w * variance_pct)
    y_pad = int(h * variance_pct)
    
    inner_left = x + x_pad
    inner_right = x + w - x_pad
    inner_top = y + y_pad
    inner_bottom = y + h - y_pad
    
    # Safeguard against highly compressed bounding boxes
    if inner_left >= inner_right:
        inner_left, inner_right = x, x + w
    if inner_top >= inner_bottom:
        inner_top, inner_bottom = y, y + h
        
    target_x = random.randint(inner_left, inner_right)
    target_y = random.randint(inner_top, inner_bottom)
    return target_x, target_y


def scale_coordinate(
    point: Tuple[int, int], 
    base_res: Tuple[int, int],
    target_res: Tuple[int, int]
) -> Tuple[int, int]:
    """
    Scales an (x, y) coordinate mapped in a standard design resolution
    to fit the active display configuration of the running game.
    """
    base_w, base_h = base_res
    target_w, target_h = target_res
    
    scale_x = target_w / base_w
    scale_y = target_h / base_h
    
    scaled_x = int(point[0] * scale_x)
    scaled_y = int(point[1] * scale_y)
    return scaled_x, scaled_y


def rgb_color_match(color_a: Tuple[int, int, int], color_b: Tuple[int, int, int], tolerance: int = 15) -> bool:
    """
    Compares two RGB colors within a given tolerance threshold.
    Typically used for evaluating health bars, cooldown indicators, and UI transitions.
    """
    return all(abs(a - b) <= tolerance for a, b in zip(color_a, color_b))