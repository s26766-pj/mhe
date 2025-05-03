import time
import random
import math
from typing import Callable, Dict, Optional

from model import ThreePartitionProblem, Assignment
from evaluator import loss
from initializer import random_balanced_assignment
from neighborhood import random_normal_neighbor


def simulated_annealing(
    problem: ThreePartitionProblem,
    schedule: str = 'exponential',
    schedule_params: Optional[Dict] = None,
    initial_temp: Optional[float] = None,
    sigma: float = 1.0,
    time_limit_seconds: int = 60
) -> Assignment:
    """
    Simulated Annealing dla problemu m-partycji.

    :param problem: instancja zadania
    :param schedule: nazwa schematu temperatury ('linear','exponential','logarithmic')
    :param schedule_params: parametry dla wybranego schematu (alpha, c)
    :param initial_temp: początkowa temperatura (jeśli None, to sum(elements)/m)
    :param sigma: odchylenie standardowe dla rozkładu normalnego w wyborze sąsiada
    :param time_limit_seconds: limit czasu działania
    :return: najlepsze znalezione Assignment
    """
    schedule_params = schedule_params or {}
    temp_func = SCHEDULE_FUNCTIONS.get(schedule)
    if temp_func is None:
        raise ValueError(f"Nieznany schemat wyżarzania: {schedule}")

    start_time = time.time()
    labels = random_balanced_assignment(problem.n, problem.m)
    current = Assignment(labels, problem)
    current_loss = loss(current)
    best = current
    best_loss = current_loss

    if initial_temp is None:
        initial_temp = problem.total / problem.m

    step = 0
    while time.time() - start_time < time_limit_seconds:

        temperature = temp_func(initial_temp, step, schedule_params)
        if temperature <= 0:
            break

        neighbor_labels = random_normal_neighbor(current.labels, sigma)
        neighbor = Assignment(neighbor_labels, problem)
        neighbor_loss = loss(neighbor)

        delta = neighbor_loss - current_loss
        if delta <= 0:
            current, current_loss = neighbor, neighbor_loss
            if current_loss < best_loss:
                best, best_loss = current, current_loss
        else:
            prob = math.exp(-delta / temperature)
            if random.random() < prob:
                current, current_loss = neighbor, neighbor_loss

        step += 1

    return best


def linear_schedule(initial_temp: float, step: int, params: Dict) -> float:
    return max(initial_temp - params.get('alpha', 1.0) * step, 0.0)


def exponential_schedule(initial_temp: float, step: int, params: Dict) -> float:
    return initial_temp * (params.get('alpha', 0.95) ** step)


def logarithmic_schedule(initial_temp: float, step: int, params: Dict) -> float:
    c = params.get('c', 1.0)
    return initial_temp / math.log(step + c)


SCHEDULE_FUNCTIONS: Dict[str, Callable[[float, int, Dict], float]] = {
    'linear': linear_schedule,
    'exponential': exponential_schedule,
    'logarithmic': logarithmic_schedule,
}
