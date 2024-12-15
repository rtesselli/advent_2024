from pathlib import Path
import re
from dataclasses import dataclass
import numpy as np
from matplotlib import pyplot as plt

Point = tuple[int, int]

MATRIX_ROWS = 103
MATRIX_COLS = 101

# MATRIX_ROWS = 7
# MATRIX_COLS = 11


@dataclass()
class Robot:
    position: Point
    velocity: Point


def load_values() -> list[Robot]:
    lines = Path("data/day14.txt").read_text().splitlines()
    out = []
    for line in lines:
        pcol, prow, vcol, vrow = re.findall(r"-?\d+", line)
        out.append(
            Robot(
                (int(prow), int(pcol)),
                (int(vrow), int(vcol))
            )
        )
    return out


def step(position: Point, velocity: Point) -> Point:
    position_x, position_y = position
    v_x, v_y = velocity
    return (position_x + v_x) % MATRIX_ROWS, (position_y + v_y) % MATRIX_COLS


def show(robots: list[Robot]) -> None:
    matrix = np.zeros((MATRIX_ROWS, MATRIX_COLS), dtype=np.uint8)
    for robot in robots:
        x, y = robot.position
        matrix[x, y] = 1
    plt.imshow(matrix)
    plt.show()



def simulate(robots: list[Robot], steps: int) -> list[Robot]:
    for step_n in range(steps):
        show(robots)
        for robot in robots:
            robot.position = step(robot.position, robot.velocity)
    return robots


def count_qdrants(robots: list[Robot]) -> int:
    count_tl = 0
    count_tr = 0
    count_bl = 0
    count_br = 0
    for robot in robots:
        x, y = robot.position
        if 0 <= x < MATRIX_ROWS // 2 and 0 <= y < MATRIX_COLS // 2:
            count_tl += 1
        elif x > MATRIX_ROWS // 2 and 0 <= y < MATRIX_COLS // 2:
            count_bl += 1
        elif 0 <= x < MATRIX_ROWS // 2 and y > MATRIX_COLS // 2:
            count_tr += 1
        elif x > MATRIX_ROWS // 2 and y > MATRIX_COLS // 2:
            count_br += 1
    print(count_tl, count_tr, count_bl, count_br)
    return count_tl * count_tr * count_bl * count_br


if __name__ == '__main__':
    robots = load_values()
    robots = simulate(robots, 500)
    print(count_qdrants(robots))
