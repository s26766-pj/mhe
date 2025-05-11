from itertools import product
from typing import Iterator, List
from model import ThreePartitionProblem, Assignment
from evaluator import loss


def brute_force_label_generator(number_of_elements: int, number_of_groups: int) -> Iterator[List[int]]:
    for assignment in product(range(number_of_groups), repeat=number_of_elements):
        yield list(assignment)


def brute_force_search(problem: ThreePartitionProblem) -> Assignment:
    if problem.total % problem.m != 0:
        raise ValueError(
            f"Suma elementów ({problem.total}) nie jest podzielna przez liczbę grup ({problem.m})."
        )

    group_size = problem.n // problem.m

    best_solution = None
    best_loss = float('inf')

    for labels in brute_force_label_generator(problem.n, problem.m):
        partitions = {i: [] for i in range(problem.m)}
        for idx, grp in enumerate(labels):
            partitions[grp].append(problem.elements[idx])

        if any(len(partitions[i]) != group_size for i in partitions):
            continue

        if not all(sum(partitions[i]) == problem.target for i in partitions):
            continue

        candidate = Assignment(labels, problem)
        candidate_loss = loss(candidate)

        if candidate_loss < best_loss:
            best_solution = candidate
            best_loss = candidate_loss
            if best_loss == 0:
                break

    if best_solution is None:
        raise RuntimeError("Brak rozwiązania spełniającego warunki m-partycji.")

    return best_solution
