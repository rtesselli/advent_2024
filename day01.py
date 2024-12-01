from pathlib import Path
from collections import Counter


def load_values() -> tuple[list[int], list[int]]:
    lines = Path("data/day01.txt").read_text().splitlines()
    return [int(line.split()[0].strip()) for line in lines], [int(line.split()[1].strip()) for line in lines]


def distance(a, b) -> int:
    return sum(abs(first - second) for first, second in zip(sorted(a), sorted(b)))


def similarity(a, b) -> int:
    counts = Counter(b)
    return sum(value * counts[value] for value in a)


if __name__ == '__main__':
    list_a, list_b = load_values()
    print(distance(list_a, list_b))
    print(similarity(list_a, list_b))
