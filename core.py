import time
from typing import Callable, List


class GameTask:
    def __init__(self, name: str, action: Callable[[], bool], interval: float):
        self.name = name
        self.action = action
        self.interval = interval
        self.last_run: float = 0.0

    def is_ready(self, current_time: float) -> bool:
        return current_time - self.last_run >= self.interval


class AutomationEngine:
    def __init__(self):
        self.tasks: List[GameTask] = []
        self.running: bool = False

    def register_task(self, name: str, action: Callable[[], bool], interval: float):
        """Registers a gaming macro or scheduled automation task."""
        task = GameTask(name, action, interval)
        self.tasks.append(task)

    def stop(self):
        """Gracefully stops the execution loop."""
        self.running = False

    def run_once(self) -> int:
        """Runs scheduled actions that have cooled down."""
        current_time = time.time()
        executed_count = 0

        for task in self.tasks:
            if task.is_ready(current_time):
                success = task.action()
                task.last_run = current_time
                if success:
                    executed_count += 1
        return executed_count

    def start_loop(self, tick_rate: float = 0.05):
        """Main loop executing tasks based on tick rate."""
        self.running = True
        while self.running:
            self.run_once()
            time.sleep(tick_rate)
