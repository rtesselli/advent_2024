from pathlib import Path
from copy import copy
from collections import Counter

Point = tuple[int, int]


def load_values() -> tuple[set[Point], Point, int, int]:
    lines = Path("data/day06.txt").read_text().splitlines()
    blocks = set()
    start = (-1, -1)
    for irow, line in enumerate(lines):
        for icol, char in enumerate(line):
            if char == '#':
                blocks.add((irow, icol))
            if char == '^':
                start = (irow, icol)
    return blocks, start, len(lines), len(lines[0])


def in_bounds(point: Point) -> bool:
    x, y = point
    return 0 <= x < n_rows and 0 <= y < n_cols


def simulate(blocks: set[Point], start: Point) -> tuple[dict[Point, int], bool]:
    curr_pos = start
    marks = Counter()
    orientation = 0
    max_visits = 5
    while in_bounds(curr_pos):
        x, y = curr_pos
        marks[curr_pos] += 1
        if marks[curr_pos] >= max_visits:
            break
        match orientation:
            case 0:
                next_pos = (x - 1, y)
            case 1:
                next_pos = (x, y + 1)
            case 2:
                next_pos = (x + 1, y)
            case 3:
                next_pos = (x, y - 1)
            case _:
                next_pos = (-1, -1)
        if next_pos in blocks:
            orientation += 1
            orientation %= 4
        else:
            curr_pos = next_pos
    return marks, in_bounds(curr_pos)


def find_loops(blocks: set[Point], start: Point) -> int:
    original_blocks = copy(blocks)
    counts = 0
    for irow in range(n_rows):
        for icol in range(n_cols):
            if (irow, icol) not in blocks:
                blocks = copy(original_blocks)
                blocks.add((irow, icol))
                _, is_loop = simulate(blocks, start)
                counts += int(is_loop)
    return counts


if __name__ == '__main__':
    blockers, start_point, n_rows, n_cols = load_values()
    positions, _ = simulate(blockers, start_point)
    print(len(positions))
    print(find_loops(blockers, start_point))
