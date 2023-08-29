import unittest
from typing import List
from GreedyAlgorithms.JobsScheduler import Job, JobsScheduler

class JobSchedulerTest(unittest.TestCase):
    def test_1(self):

        def vectorization_fn(job: Job) -> List[int]:
            return [job.weight - job.length, job.weight]

        jobs = [
            Job(1, 2, vectorization_fn),
            Job(4, 3, vectorization_fn),
            Job(3, 5, vectorization_fn),
            Job(1, 1, vectorization_fn),
            Job(2, 2, vectorization_fn),
        ]
        scheduler = JobsScheduler(jobs)
        self.assertEqual(75, scheduler.weighted_completion_time)

    def test_dif_fn(self):
        with open('./test_data/job_schedule_data.txt', 'r') as file:
            input_str = file.read()

        def vectorization_fn(job: Job) -> List[int]:
            return [job.weight - job.length, job.weight]

        rows = [row.strip().split(' ') for row in input_str.strip().split('\n') if len(row.strip().split(' ')) == 2]
        jobs = [Job(int(weight), int(length), vectorization_fn) for weight, length in rows]
        scheduler = JobsScheduler(jobs)

        self.assertEqual(69119377652, scheduler.weighted_completion_time)


    def test_optimal_fn(self):
        with open('./test_data/job_schedule_data.txt', 'r') as file:
            input_str = file.read()

        def vectorization_fn(job: Job) -> List[int]:
            return [job.weight / job.length, job.weight]

        rows = [row.strip().split(' ') for row in input_str.strip().split('\n') if len(row.strip().split(' ')) == 2]
        jobs = [Job(int(weight), int(length), vectorization_fn) for weight, length in rows]
        scheduler = JobsScheduler(jobs)

        self.assertEqual(67311454237, scheduler.weighted_completion_time)