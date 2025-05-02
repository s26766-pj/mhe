from itertools import product
from typing import Iterator, List
from model import ThreePartitionProblem, Assignment
from evaluator import loss


def brute_force_labels(n: int, k: int = 3) -> Iterator[List[int]]:
    for assignment in product(range(k), repeat=n):
        yield list(assignment)


def brute_force_search(problem: ThreePartitionProblem) -> Assignment:
    best = None
    best_score = float('inf')
    for labels in brute_force_labels(problem.n, problem.k):
        assign = Assignment(labels, problem)
        score = loss(assign)
        if score < best_score:
            best, best_score = assign, score

            if best_score == 0:
                break
    return best
