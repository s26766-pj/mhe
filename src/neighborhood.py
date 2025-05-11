import random
from typing import List


def swap_neighbors(labels: List[int]) -> List[List[int]]:
    n = len(labels)
    neighbors = []
    for i in range(n):
        for j in range(i+1, n):
            if labels[i] != labels[j]:
                nb = labels.copy()
                nb[i], nb[j] = nb[j], nb[i]
                neighbors.append(nb)
    return neighbors


def random_normal_neighbor(labels: List[int], sigma: float, max_tries: int = 1000) -> List[int]:
    n = len(labels)
    for _ in range(max_tries):
        mean = (n - 1) / 2
        i = int(random.gauss(mean, sigma))
        j = int(random.gauss(mean, sigma))
        if not (0 <= i < n and 0 <= j < n and i < j and labels[i] != labels[j]):
            continue
        neighbor = labels.copy()
        neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
        return neighbor

    i, j = random.sample([idx for idx in range(n)], 2)
    neighbor = labels.copy()
    neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
    return neighbor
