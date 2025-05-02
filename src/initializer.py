import random
from typing import List


def random_assignment(n: int, k: int = 3) -> List[int]:
    return [random.randrange(k) for _ in range(n)]
