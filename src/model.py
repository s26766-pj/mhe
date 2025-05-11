from typing import List


class ThreePartitionProblem:
    def __init__(self, elements: List[int]):
        if not all(isinstance(x, int) and x > 0 for x in elements):
            raise ValueError("Wszystkie elementy muszą być dodatnimi liczbami całkowitymi.")

        self.elements = list(elements)
        self.n = len(self.elements)
        if self.n % 3 != 0:
            raise ValueError("Liczba elementów w multizbiorze nie jest podzielna przez trzy.")

        self.total = sum(self.elements)
        self.m = self.n // 3

    @property
    def target(self) -> float:
        return self.total / self.m


class Assignment:
    def __init__(self, labels: List[int], problem: ThreePartitionProblem):
        if len(labels) != problem.n:
            raise ValueError(f"Długość etykiet ({len(labels)}) różni się od liczby elementów ({problem.n}).")
        if not all(0 <= lbl < problem.m for lbl in labels):
            raise ValueError(f"Etykieta poza zakresem: każda etykieta musi być w [0, {problem.m - 1}].")

        self.labels = labels
        self.problem = problem

    def as_partitions(self) -> List[List[int]]:
        partitions: List[List[int]] = [[] for _ in range(self.problem.m)]
        for index, group in enumerate(self.labels):
            partitions[group].append(self.problem.elements[index])
        return partitions
