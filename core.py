import math
from collections import defaultdict
from typing import Dict, List, Tuple

class SpatialGrid:
    """Optimized grid mapping for fast entity proximity lookups in game screens."""
    def __init__(self, cell_size: int = 50):
        self.cell_size = cell_size
        self.grid: Dict[Tuple[int, int], List[Dict]] = defaultdict(list)

    def _get_key(self, x: float, y: float) -> Tuple[int, int]:
        """Maps coordinate to grid cell key."""
        return int(x // self.cell_size), int(y // self.cell_size)

    def clear(self) -> None:
        """Resets the spatial index."""
        self.grid.clear()

    def insert(self, entity: Dict) -> None:
        """Inserts an entity with 'x', 'y' and 'id' fields into the grid."""
        key = self._get_key(entity["x"], entity["y"])
        self.grid[key].append(entity)

    def find_nearby(self, x: float, y: float, radius: float) -> List[Dict]:
        """Finds entities within a circular radius of a coordinate using spatial buckets."""
        nearby = []
        min_x = int((x - radius) // self.cell_size)
        max_x = int((x + radius) // self.cell_size)
        min_y = int((y - radius) // self.cell_size)
        max_y = int((y + radius) // self.cell_size)

        radius_sq = radius ** 2

        # Scan adjacent cell buckets instead of global O(N) iteration
        for cx in range(min_x, max_x + 1):
            for cy in range(min_y, max_y + 1):
                cell_key = (cx, cy)
                if cell_key in self.grid:
                    for entity in self.grid[cell_key]:
                        dist_sq = (entity["x"] - x) ** 2 + (entity["y"] - y) ** 2
                        if dist_sq <= radius_sq:
                            # Cache squared distance to avoid redundant calculations during sorting
                            entity["_dist_sq"] = dist_sq
                            nearby.append(entity)

        # Sort targets by distance (closest first) for prioritized execution
        nearby.sort(key=lambda e: e.get("_dist_sq", 0))
        return nearby