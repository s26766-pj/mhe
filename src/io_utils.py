from typing import List


def read_instance(path: str = None) -> List[int]:
    if path is None:
        data = input().strip().split()
    else:
        with open(path) as f:
            data = f.read().strip().split()
    return list(map(int, data))
