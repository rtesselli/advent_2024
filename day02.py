from pathlib import Path
from itertools import pairwise
from copy import copy


def load_values() -> list[list[int]]:
    lines = Path("data/day02.txt").read_text().splitlines()
    return [
        [int(value) for value in line.split()] for line in lines
    ]


def is_monotonic(values: list[int]) -> bool:
    return all(first <= second for first, second in pairwise(values)) or all(
        first >= second for first, second in pairwise(values))


def levels_near(values: list[int]) -> bool:
    return all(1 <= abs(first - second) <= 3 for first, second in pairwise(values))


def is_safe(values: list[int]) -> bool:
    return is_monotonic(values) and levels_near(values)


def is_robust_safe(values: list[int]) -> bool:
    original_values = copy(values)
    for i in range(len(values)):
        values.pop(i)
        if is_safe(values):
            return True
        values = copy(original_values)
    return False


if __name__ == '__main__':
    reports = load_values()
    safes = [report for report in reports if is_safe(report)]
    print(len(safes))
    unsafes = [report for report in reports if not is_safe(report)]
    robust_safes = [unsafe for unsafe in unsafes if is_robust_safe(unsafe)]
    print(len(safes) + len(robust_safes))
