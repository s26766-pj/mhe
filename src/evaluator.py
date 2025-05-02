from model import Assignment


def loss(assign: Assignment) -> float:
    parts = assign.as_partitions()
    target = assign.problem.target
    return sum((sum(p) - target) ** 2 for p in parts)
