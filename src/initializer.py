import random
from typing import List


def random_balanced_assignment(n: int, m: int) -> List[int]:
    """
    Zwraca losowy wektor etykiet długości n,
    taki, że każda z m grup ma dokładnie n/m elementów.
    """
    group_size = n // m
    labels = []
    for grp in range(m):
        labels += [grp] * group_size
    random.shuffle(labels)
    return labels

