from itertools import product
from typing import Iterator, List
from model import ThreePartitionProblem, Assignment
from evaluator import loss


def brute_force_label_generator(number_of_elements: int, number_of_groups: int) -> Iterator[List[int]]:
    """
    Generator wszystkich możliwych przydziałów elementów do grup.
    number_of_elements: liczba elementów w problemie.
    number_of_groups: liczba grup m.
    Zwraca sekwencję list etykiet długości number_of_elements.
    """
    for assignment in product(range(number_of_groups), repeat=number_of_elements):
        yield list(assignment)


def brute_force_search(problem: ThreePartitionProblem) -> Assignment:
    """
    Przegląd pełny (brute-force) dla problemu m-partycji na multizbiorze.
    Sprawdza wszystkie przydziały, ale zwraca tylko te, gdzie każda grupa:
      1) ma sumę równą problem.target,
      2) zawiera dokładnie problem.group_size elementów.
    Zwraca Assignment o najlepszej (najniższej) wartości loss (typowo 0) lub
    rzuca RuntimeError, jeśli nie znaleziono rozwiązania.
    """

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
