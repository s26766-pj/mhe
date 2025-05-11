import random
from typing import List


def random_balanced_assignment(n: int, m: int) -> List[int]:
    group_size = n // m
    labels = []
    for grp in range(m):
        labels += [grp] * group_size
    random.shuffle(labels)
    return labels

