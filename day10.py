import numpy as np
from pathlib import Path
from collections import Counter

Point = tuple[int, int]


def load_matrix() -> np.ndarray:
    lines = Path("data/day10.txt").read_text().splitlines()
    return np.array([[int(e) if e != '.' else -1 for e in line.strip()] for line in lines], dtype=np.int_)


def in_bounds(x, y):
    return 0 <= x < tmap.shape[0] and 0 <= y < tmap.shape[1]


def count_trailheads(matrix: np.ndarray) -> tuple[int, int]:
    def rec(row: int, col: int, counter: Counter) -> Counter:
        if matrix[row, col] == 9:
            counter[(row, col)] += 1
            return counter
        neighbors = [(row + delta_row, col + delta_col) for delta_row, delta_col in ((-1, 0), (1, 0), (0, -1), (0, 1))
                     if in_bounds(row + delta_row, col + delta_col)]
        for next_row, next_col in neighbors:
            if matrix[next_row, next_col] == matrix[row, col] + 1:
                rec(next_row, next_col, counter)
        return counter

    starts = np.where(matrix == 0)
    counts = 0
    trails = 0
    for row, col in zip(*starts):
        result = rec(row, col, Counter())
        counts += len(result)
        trails += sum(n for n in result.values())
    return counts, trails


if __name__ == '__main__':
    tmap = load_matrix()
    print(count_trailheads(tmap))
