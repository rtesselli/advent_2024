from pathlib import Path
from dataclasses import dataclass
import re
import numpy as np

Point = tuple[int, int]

BUTTON_A_COST = 3
BUTTON_B_COST = 1


@dataclass()
class Button:
    delta_x: int
    delta_y: int


@dataclass()
class Problem:
    button_a: Button
    button_b: Button
    prize_coords: Point


def load_values() -> list[Problem]:
    text = Path("data/day13.txt").read_text()
    blocks = text.split("\n\n")
    problems = []
    for block in blocks:
        lines = block.splitlines()
        delta_x, delta_y = re.findall(r"\d+", lines[0])
        button_a = Button(int(delta_x), int(delta_y))
        delta_x, delta_y = re.findall(r"\d+", lines[1])
        button_b = Button(int(delta_x), int(delta_y))
        x, y = re.findall(r"\d+", lines[2])
        problems.append(Problem(button_a, button_b, (int(x), int(y))))
    return problems


def solve(problem: Problem) -> int:
    delta_matrix = np.array(
        [[problem.button_a.delta_x, problem.button_b.delta_x], [problem.button_a.delta_y, problem.button_b.delta_y]])
    target_vector = np.array([[problem.prize_coords[0]], [problem.prize_coords[1]]])
    try:
        inv_delta = np.linalg.inv(delta_matrix)
    except:
        return 0
    result = inv_delta.dot(target_vector)
    cost_vector = np.array([BUTTON_A_COST, BUTTON_B_COST])
    out = cost_vector.dot(result)[0]
    if out == int(out):
        return int(out)
    return 0


if __name__ == '__main__':
    problems = load_values()
    print(sum(solve(problem) or 0 for problem in problems))
