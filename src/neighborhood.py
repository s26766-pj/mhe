import random
from typing import List


def all_neighbors(labels: List[int], k: int = 3) -> List[List[int]]:
    n = len(labels)
    neighbors = []

    for i in range(n):
        for new_part in range(k):
            if labels[i] != new_part:
                nb = labels.copy()
                nb[i] = new_part
                neighbors.append(nb)

    for i in range(n):
        for j in range(i+1, n):
            if labels[i] != labels[j]:
                nb = labels.copy()
                nb[i], nb[j] = nb[j], nb[i]
                neighbors.append(nb)

    return neighbors


def random_neighbors(labels: List[int], k: int = 3, m: int = 100) -> List[List[int]]:
    all_nb = all_neighbors(labels, k)
    random.shuffle(all_nb)
    return all_nb[:m]
