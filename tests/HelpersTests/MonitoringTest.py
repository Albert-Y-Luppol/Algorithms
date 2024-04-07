import unittest
import time
import psutil
import os
from src.helpers.monitoring import print_progress_bar, print_memory_utilization


class LoaderTest(unittest.TestCase):
    def test_0_print_progress_bar(self):
        total = 100
        print("Starting task...")
        for i in range(0, total + 1):
            time.sleep(0.1)  # Simulate some work
            print_progress_bar(i, total, prefix='Progress:', suffix='Complete', length=50)
        print("Task completed!")

    def test_0_print_memory_utilization(self):
        initial_usage = psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2
        print(f"Initial memory usage: {initial_usage:.2f} MB")

        # Allocate memory to see the change
        self.allocate_memory(1000, 1000000)  # Adjust these numbers based on your system

        # Measure again after allocation
        final_usage = psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2
        print(f"Memory usage after allocation: {final_usage:.2f} MB")

        # Now print the memory utilization using your function
        print_memory_utilization(prefix='Memory Usage:', suffix='MB', length=50)

        # Here, you would manually verify if the memory usage increase is accurately reflected.
        # An automatic assertion is challenging due to the overhead and variability in memory reporting.

    def setUp(self):
        self.memory_hog = []

    def allocate_memory(self, num_elements, element_size):
        """Allocates memory by appending large strings to a list."""
        for _ in range(num_elements):
            self.memory_hog.append('a' * element_size)
