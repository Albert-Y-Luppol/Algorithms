from typing import Self, Callable, List


class Job:
    def __init__(self, weight: int, length: int, vectorization_fn: Callable[[Self], List[int]]):
        self.__weight = weight
        self.__length = length
        self.__vector_representation = vectorization_fn(self)
        self.__vectorization_fn = vectorization_fn

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, new_weight: int):
        self.__weight = new_weight
        self.__vector_representation = self.__vectorization_fn(self)

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, new_length: int):
        self.__length = new_length
        self.__vector_representation = self.__vectorization_fn(self)

    @property
    def vector_representation(self):
        return self.__vector_representation

    def __gt__(self, other: Self) -> bool:
        for i in range(len(self.__vector_representation)):
            if self.vector_representation[i] == other.vector_representation[i]:
                continue
            else:
                return self.vector_representation[i] > other.vector_representation[i]

        return False

    def __ge__(self, other: Self) -> bool:
        for i in range(len(self.__vector_representation)):
            if self.vector_representation[i] == other.vector_representation[i]:
                continue
            else:
                return self.vector_representation[i] > other.vector_representation[i]

        return True

    def __eq__(self, other: Self) -> bool:
        for i in range(len(self.__vector_representation)):
            if self.vector_representation[i] == other.vector_representation[i]:
                continue
            else:
                return False

        return True

    def __lt__(self, other: Self) -> bool:
        for i in range(len(self.__vector_representation)):
            if self.vector_representation[i] == other.vector_representation[i]:
                continue
            else:
                return self.vector_representation[i] < other.vector_representation[i]

        return False

    def __le__(self, other: Self) -> bool:
        for i in range(len(self.__vector_representation)):
            if self.vector_representation[i] == other.vector_representation[i]:
                continue
            else:
                return self.vector_representation[i] < other.vector_representation[i]

        return True


class JobsScheduler:
    def __init__(self, jobs: List[Job]) -> None:
        self.schedule = jobs
        self.schedule.sort(reverse=True)

    @property
    def weighted_completion_time(self) -> int:
        time = 0
        result = 0
        for job in self.schedule:
            time += job.length
            result += time * job.weight

        return result
