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


def get_corners(region: set[Point]) -> int:
    def count_corners(point: Point) -> int:
        curr_x, curr_y = point
        neighbors = set()
        for delta_x, delta_y in DIRECTIONS:
            if (curr_x + delta_x, curr_y + delta_y) in region:
                neighbors.add((delta_x, delta_y))
        if len(neighbors) == 0:
            return 4
        if len(neighbors) == 1:
            return 2
        if len(neighbors) == 2:
            if (0, -1) in neighbors and (-1, 0) in neighbors:
                return 1 + ((curr_x - 1, curr_y - 1) not in region)
            if (0, -1) in neighbors and (1, 0) in neighbors:
                return 1 + ((curr_x + 1, curr_y - 1) not in region)
            if (0, 1) in neighbors and (-1, 0) in neighbors:
                return 1 + ((curr_x - 1, curr_y + 1) not in region)
            if (0, 1) in neighbors and (1, 0) in neighbors:
                return 1 + ((curr_x + 1, curr_y + 1) not in region)
        if len(neighbors) == 3:
            if (1, 0) not in neighbors:
                return int((curr_x - 1, curr_y - 1) not in region) + int((curr_x - 1, curr_y + 1) not in region)
            if (-1, 0) not in neighbors:
                return int((curr_x + 1, curr_y - 1) not in region) + int((curr_x + 1, curr_y + 1) not in region)
            if (0, 1) not in neighbors:
                return int((curr_x - 1, curr_y - 1) not in region) + int((curr_x + 1, curr_y - 1) not in region)
            if (0, -1) not in neighbors:
                return int((curr_x - 1, curr_y + 1) not in region) + int((curr_x + 1, curr_y + 1) not in region)
        if len(neighbors) == 4:
            return int((curr_x - 1, curr_y - 1) not in region) + int((curr_x + 1, curr_y - 1) not in region) + int(
                (curr_x - 1, curr_y + 1) not in region) + int((curr_x + 1, curr_y + 1) not in region)
        return 0

    return sum(
        count_corners(point) for point in region
    )


def get_cost(region: set[Point]) -> tuple[int, int]:
    def get_perimeter(r: int, c: int) -> set[Point]:
        return {(r + delta_row, c + delta_col) for delta_row, delta_col in DIRECTIONS if
                (r + delta_row, c + delta_col) not in region}

    area = len(region)
    perimeter = defaultdict(int)
    for row, col in region:
        boundaries = get_perimeter(row, col)
        for position in boundaries:
            perimeter[position] += 1
    corners = get_corners(region)
    return area * sum(perimeter.values()), area * corners


# F +1, V +4, J +2, E +6,


if __name__ == '__main__':
    matrix = load_matrix()
    regions = get_regions(matrix)
    print(sum(get_cost(region)[0] for _, sub_regions in regions.items() for region in sub_regions))
    print(sum(get_cost(region)[1] for _, sub_regions in regions.items() for region in sub_regions))
