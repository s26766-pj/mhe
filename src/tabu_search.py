import time
from collections import deque
from typing import Optional, Tuple

from model import ThreePartitionProblem, Assignment
from evaluator import loss
from initializer import random_balanced_assignment
from neighborhood import swap_neighbors


def tabu_search(
        problem: ThreePartitionProblem,
        tabu_size: Optional[int] = 50,
        time_limit_seconds: int = 60
) -> Assignment:

    start_time = time.time()
    initial_labels = random_balanced_assignment(problem.n, problem.m)
    current_solution = Assignment(initial_labels, problem)
    current_loss = loss(current_solution)
    best_solution = current_solution
    best_loss = current_loss
    maxlen = tabu_size if tabu_size and tabu_size > 0 else None
    tabu_list: deque[Tuple[int, int]] = deque(maxlen=maxlen)

    while time.time() - start_time < time_limit_seconds:
        neighbors = swap_neighbors(current_solution.labels)

        candidate_solution = None
        candidate_loss = float('inf')
        candidate_move = None

        for move_labels in neighbors:
            move = next(
                (i, j) for i in range(problem.n) for j in range(i + 1, problem.n)
                if current_solution.labels[i] != current_solution.labels[j] and
                move_labels[i] == current_solution.labels[j] and
                move_labels[j] == current_solution.labels[i]
            )

            if move in tabu_list:
                temp_assign = Assignment(move_labels, problem)
                temp_loss = loss(temp_assign)
                if temp_loss >= best_loss:
                    continue

            temp_assign = Assignment(move_labels, problem)
            temp_loss = loss(temp_assign)
            if temp_loss < candidate_loss:
                candidate_solution = temp_assign
                candidate_loss = temp_loss
                candidate_move = move

        # tu można by było dopisać ograniczenie czasowe odnośnie braku poprawy
        # if candidate_solution is None or candidate_loss >= current_loss:
        #     break

        if candidate_solution is None:
            break

        current_solution = candidate_solution
        current_loss = candidate_loss
        tabu_list.append(candidate_move)

        if current_loss < best_loss:
            best_solution = current_solution
            best_loss = current_loss
            if best_loss == 0:
                break

    return best_solution
