import math
from typing import Dict, List, Tuple


class SpatialEntityGrid:
    """Spatial hashing grid to optimize entity proximity and collision checks in frame loops."""

    def __init__(self, cell_size: int = 64):
        self.cell_size = cell_size
        self.grid: Dict[Tuple[int, int], List[Dict]] = {}

    def _get_cell_coords(self, x: float, y: float) -> Tuple[int, int]:
        return (math.floor(x / self.cell_size), math.floor(y / self.cell_size))

    def clear(self) -> None:
        """Reset grid buckets for the next frame."""
        self.grid.clear()

    def insert_entity(
        self, entity_id: str, x: float, y: float, radius: float = 0.0
    ) -> None:
        """Insert an entity into all overlapping spatial grid cells."""
        min_x, max_x = x - radius, x + radius
        min_y, max_y = y - radius, y + radius

        min_cell_x, min_cell_y = self._get_cell_coords(min_x, min_y)
        max_cell_x, max_cell_y = self._get_cell_coords(max_x, max_y)

        entity_data = {"id": entity_id, "x": x, "y": y, "radius": radius}

        for cx in range(min_cell_x, max_cell_x + 1):
            for cy in range(min_cell_y, max_cell_y + 1):
                cell = (cx, cy)
                if cell not in self.grid:
                    self.grid[cell] = []
                self.grid[cell].append(entity_data)

    def get_nearby_entities(
        self, x: float, y: float, query_radius: float
    ) -> List[str]:
        """Retrieve unique IDs of entities within query_radius of target point."""
        min_cell_x, min_cell_y = self._get_cell_coords(
            x - query_radius, y - query_radius
        )
        max_cell_x, max_cell_y = self._get_cell_coords(
            x + query_radius, y + query_radius
        )

        seen_ids = set()
        nearby = []

        for cx in range(min_cell_x, max_cell_x + 1):
            for cy in range(min_cell_y, max_cell_y + 1):
                cell_entities = self.grid.get((cx, cy), [])
                for entity in cell_entities:
                    eid = entity["id"]
                    if eid in seen_ids:
                        continue

                    dx = entity["x"] - x
                    dy = entity["y"] - y
                    dist_sq = dx * dx + dy * dy
                    max_dist = query_radius + entity["radius"]

                    if dist_sq <= max_dist * max_dist:
                        seen_ids.add(eid)
                        nearby.append(eid)

        return nearby
