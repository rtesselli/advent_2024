from pathlib import Path
import numpy as np
from collections import defaultdict


def load_matrix() -> np.ndarray:
    lines = Path("data/day12.txt").read_text().splitlines()
    return np.array([list(line.strip()) for line in lines])


def in_bounds(x, y):
    return 0 <= x < matrix.shape[0] and 0 <= y < matrix.shape[1]


DIRECTIONS = {(-1, 0), (1, 0), (0, -1), (0, 1)}
Point = tuple[int, int]


def get_perimeter(r: int, c: int, neighbors: set[tuple[int, int]]) -> set[tuple[int, int]]:
    return set()


def get_regions(matrix: np.ndarray) -> dict[str, list[set[Point]]]:
    def expand(key: str, r: int, c: int, curr_area: set[Point]) -> set[Point]:
        visited.add((r, c))
        neighbors = {(r + delta_row, c + delta_col) for delta_row, delta_col in DIRECTIONS if
                     in_bounds(r + delta_row, c + delta_col) and (r + delta_row, c + delta_col) not in visited and
                     matrix[r + delta_row, c + delta_col] == key}
        curr_area.add((r, c))
        for next_r, next_c in neighbors:
            curr_area = expand(key, next_r, next_c, curr_area)
        return curr_area

    n_rows, n_cols = matrix.shape
    visited = set()
    regions = defaultdict(list)
    for id_row in range(n_rows):
        for id_col in range(n_cols):
            if (id_row, id_col) not in visited:
                key = str(matrix[id_row, id_col])
                regions[key].append(expand(str(key), id_row, id_col, set()))
    return regions


if __name__ == '__main__':
    matrix = load_matrix()
    regions = get_regions(matrix)
    print(regions)

