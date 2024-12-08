import numpy as np
from pathlib import Path
from itertools import combinations

Point = tuple[int, int]


def load_matrix() -> np.ndarray:
    lines = Path("data/day08.txt").read_text().splitlines()
    return np.array([list(line.strip()) for line in lines])


def get_antinodes(matrix: np.ndarray) -> set[Point]:
    antenna_ids = set(np.unique(matrix).tolist()) - {'.'}
    antinode_positions = set()
    for antenna_id in antenna_ids:
        xs, ys = np.where(matrix == antenna_id)
        positions = [(int(x), int(y)) for x, y in zip(xs, ys)]
        for first, second in combinations(positions, 2):
            delta = np.array(second) - np.array(first)
            antinode_positions.add(tuple((np.array(second) + delta).tolist()))
            antinode_positions.add(tuple((np.array(first) - delta).tolist()))
    return antinode_positions


def in_bounds(x: int, y: int) -> bool:
    return 0 <= x < matrix.shape[0] and 0 <= y < matrix.shape[1]


def get_antinodes2(matrix: np.ndarray) -> set[Point]:
    antenna_ids = set(np.unique(matrix).tolist()) - {'.'}
    antinode_positions = set()
    for antenna_id in antenna_ids:
        xs, ys = np.where(matrix == antenna_id)
        positions = [(int(x), int(y)) for x, y in zip(xs, ys)]
        for first, second in combinations(positions, 2):
            delta = np.array(second) - np.array(first)
            curr_pos = first + delta
            while in_bounds(*curr_pos):
                antinode_positions.add(tuple(curr_pos.tolist()))
                curr_pos += delta
            curr_pos = second - delta
            while in_bounds(*curr_pos):
                antinode_positions.add(tuple(curr_pos.tolist()))
                curr_pos -= delta
    return antinode_positions


if __name__ == '__main__':
    matrix = load_matrix()
    antinodes = get_antinodes(matrix)
    print(sum(1 for x, y in antinodes if in_bounds(x, y)))
    antinodes = get_antinodes2(matrix)
    print(len(antinodes))
