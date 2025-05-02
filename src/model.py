from typing import List


class ThreePartitionProblem:
    def __init__(self, elements: List[int]):
        self.elements = list(set(elements))
        self.n = len(self.elements)
        self.total = sum(self.elements)
        self.k = 3

    @property
    def target(self) -> float:
        return self.total / self.k


class Assignment:
    def __init__(self, labels: List[int], problem: ThreePartitionProblem):
        assert len(labels) == problem.n
        self.labels = labels
        self.problem = problem

    def as_partitions(self) -> List[List[int]]:
        parts = [[] for _ in range(self.problem.k)]
        for idx, part in enumerate(self.labels):
            parts[part].append(self.problem.elements[idx])
        return parts
