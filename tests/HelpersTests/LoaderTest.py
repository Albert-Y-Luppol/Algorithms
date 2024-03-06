import unittest
import time
from src.helpers.loader import print_progress_bar

class LoaderTest(unittest.TestCase):
    def test_0(self):
        total = 100
        print("Starting task...")
        for i in range(0, total + 1):
            time.sleep(0.1)  # Simulate some work
            print_progress_bar(i, total, prefix='Progress:', suffix='Complete', length=50)
        print("Task completed!")

