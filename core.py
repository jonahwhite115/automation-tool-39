import time

class PerformanceTracker:
    def __init__(self):
        self.start_time = None
        self.end_time = None

    def start(self):
        self.start_time = time.perf_counter()

    def stop(self):
        self.end_time = time.perf_counter()

    def duration(self):
        return self.end_time - self.start_time if self.end_time else None


def optimize_function(data):
    tracker = PerformanceTracker()
    tracker.start()  
    # Perform some CPU-intensive computations
    result = sum(item for item in data if item % 2 == 0)
    tracker.stop()
    duration = tracker.duration()  
    print(f"Function executed in {duration:.6f} seconds")
    return result

if __name__ == '__main__':
    sample_data = range(1, 1000000)
    optimize_function(sample_data)