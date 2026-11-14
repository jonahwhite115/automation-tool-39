import time
import math
from typing import List, Tuple, Dict, Any

class GameDataProcessor:
    """Processes raw telemetry and screen coordinate data for gaming automation."""

    def __init__(self, target_resolution: Tuple[int, int] = (1920, 1080)) -> None:
        self.base_width, self.base_height = target_resolution
        self.last_execution_time = time.time()

    def scale_coordinates(
        self, coords: Tuple[int, int], current_resolution: Tuple[int, int]
    ) -> Tuple[int, int]:
        """Scales coordinates from base resolution to current monitor resolution."""
        curr_w, curr_h = current_resolution
        scale_x = curr_w / self.base_width
        scale_y = curr_h / self.base_height
        return (int(coords[0] * scale_x), int(coords[1] * scale_y))

    def calculate_distance(self, pt1: Tuple[int, int], pt2: Tuple[int, int]) -> float:
        """Calculates Euclidean distance between two in-game positions or screen points."""
        return math.hypot(pt2[0] - pt1[0], pt2[1] - pt1[1])

    def filter_targets_by_proximity(
        self, origin: Tuple[int, int], targets: List[Dict[str, Any]], max_distance: float
    ) -> List[Dict[str, Any]]:
        """Filters target entities based on distance from the player or crosshair."""
        valid_targets = []
        for target in targets:
            pos = target.get("position")
            if pos and isinstance(pos, (tuple, list)) and len(pos) >= 2:
                dist = self.calculate_distance(origin, (pos[0], pos[1]))
                if dist <= max_distance:
                    target_copy = target.copy()
                    target_copy["distance"] = round(dist, 2)
                    valid_targets.append(target_copy)
        return sorted(valid_targets, key=lambda x: x["distance"])

    def pace_execution(self, target_fps: int = 60) -> None:
        """Maintains frame timing loop to prevent high CPU utilization."""
        frame_duration = 1.0 / target_fps
        elapsed = time.time() - self.last_execution_time
        if elapsed < frame_duration:
            time.sleep(frame_duration - elapsed)
        self.last_execution_time = time.time()