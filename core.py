import functools

class GameAutomationCore:
    """Core module for gaming automation with performance optimizations."""

    def __init__(self):
        self.active_tasks = set()
        self.state_cache = {}

    def add_task(self, task_id):
        # Use set for O(1) addition and lookup
        self.active_tasks.add(task_id)

    @functools.lru_cache(maxsize=512)
    def calculate_efficiency(self, task_type, stats_tuple):
        # Cached computation for performance
        # Simulate complex gaming calculation
        if not stats_tuple:
            base_score = 0
        else:
            base_score = sum(value for _, value in stats_tuple)
        efficiency = (base_score * 1.5) + hash(task_type) % 50
        return efficiency

    def optimize_task_queue(self, tasks, player_stats):
        # Batch process with cache to avoid redundant calculations
        optimized = []
        seen = set()
        for task in tasks:
            if task in seen:
                continue
            seen.add(task)
            task_type = task.get('type', 'default')
            stats = task.get('stats', player_stats)
            stats_tuple = tuple(sorted(stats.items())) if isinstance(stats, dict) else ()
            efficiency = self.calculate_efficiency(task_type, stats_tuple)
            optimized.append((task, efficiency))
        # Sort by efficiency descending
        optimized.sort(key=lambda x: x[1], reverse=True)
        return [item[0] for item in optimized[:10]]

    def process_game_loop(self, incoming_events):
        # Optimized filtering using set
        new_events = []
        for event in incoming_events:
            if event not in self.active_tasks:
                new_events.append(event)
                self.add_task(event)
        return new_events