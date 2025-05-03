import time, random
from model import ThreePartitionProblem, Assignment
from evaluator import loss
from initializer import random_balanced_assignment
from neighborhood import swap_neighbors


def hill_climbing_deterministic(problem: ThreePartitionProblem, time_limit_seconds: int) -> Assignment:
    start_time = time.time()
    initial_labels = random_balanced_assignment(problem.n, problem.m)
    current_solution = Assignment(initial_labels, problem)
    current_loss_value = loss(current_solution)

    while time.time() - start_time < time_limit_seconds:
        all_swaps = swap_neighbors(current_solution.labels)

        best_candidate = current_solution
        best_candidate_loss = current_loss_value
        for labels in all_swaps:
            candidate = Assignment(labels, problem)
            candidate_loss = loss(candidate)
            if candidate_loss < best_candidate_loss:
                best_candidate, best_candidate_loss = candidate, candidate_loss

        # tu można by było dopisać ograniczenie czasowe odnośnie braku poprawy
        # if best_candidate_loss >= current_loss_value:
        #     break

        current_solution, current_loss_value = best_candidate, best_candidate_loss

    return current_solution


def hill_climbing_stochastic(problem: ThreePartitionProblem, time_limit_seconds: int) -> Assignment:
    start_time = time.time()
    initial_labels = random_balanced_assignment(problem.n, problem.m)
    current_solution = Assignment(initial_labels, problem)
    current_loss_value = loss(current_solution)

    while time.time() - start_time < time_limit_seconds:
        all_swaps = swap_neighbors(current_solution.labels)

        improving = []
        for labels in all_swaps:
            candidate = Assignment(labels, problem)
            if loss(candidate) < current_loss_value:
                improving.append(candidate)

        if not improving:
            break

        current_solution = random.choice(improving)
        current_loss_value = loss(current_solution)

    return current_solution
