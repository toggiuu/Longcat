import time

class Timer:
    def __init__(self):
        self.start_time = None

    def start(self):
        self.start_time = time.time()

    def get_elapsed(self):
        return time.time() - self.start_time if self.start_time else 0

    def reset(self):
        self.start_time = None