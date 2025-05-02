import time
import random
from model import ThreePartitionProblem, Assignment
from evaluator import loss
from neighborhood import all_neighbors
from initializer import random_assignment


def hill_climbing_deterministic(problem: ThreePartitionProblem, time_limit_seconds: int) -> Assignment:
    start_time = time.time()
    initial_labels = random_assignment(problem.n, problem.k)
    current_solution = Assignment(initial_labels, problem)
    current_loss_value = loss(current_solution)

    while time.time() - start_time < time_limit_seconds:
        neighbor_labels_list = all_neighbors(current_solution.labels, problem.k)
        best_found_solution = current_solution
        best_found_loss = current_loss_value
        for neighbor_labels in neighbor_labels_list:
            neighbor_solution = Assignment(neighbor_labels, problem)
            neighbor_loss_value = loss(neighbor_solution)
            if neighbor_loss_value < best_found_loss:
                best_found_solution = neighbor_solution
                best_found_loss = neighbor_loss_value

        if best_found_loss >= current_loss_value:
            break

        current_solution = best_found_solution
        current_loss_value = best_found_loss

    return current_solution


def hill_climbing_stochastic(problem: ThreePartitionProblem, time_limit_seconds: int) -> Assignment:
    start_time = time.time()
    initial_labels = random_assignment(problem.n, problem.k)
    current_solution = Assignment(initial_labels, problem)
    current_loss_value = loss(current_solution)

    while time.time() - start_time < time_limit_seconds:
        neighbor_labels_list = all_neighbors(current_solution.labels, problem.k)

        improving_solutions = []
        for neighbor_labels in neighbor_labels_list:
            neighbor_solution = Assignment(neighbor_labels, problem)
            neighbor_loss_value = loss(neighbor_solution)
            if neighbor_loss_value < current_loss_value:
                improving_solutions.append(neighbor_solution)

        if not improving_solutions:
            break

        chosen_solution = random.choice(improving_solutions)
        current_solution = chosen_solution
        current_loss_value = loss(current_solution)

    return current_solution
