from pathlib import Path
from dataclasses import dataclass
import re

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


def solve(problem: Problem, ignore_big: bool = True) -> int:
    x_t = problem.prize_coords[0]
    y_t = problem.prize_coords[1]
    d_xa = problem.button_a.delta_x
    d_xb = problem.button_b.delta_x
    d_ya = problem.button_a.delta_y
    d_yb = problem.button_b.delta_y
    n_b = (y_t * d_xa - x_t * d_ya) // (d_xa * d_yb - d_xb * d_ya)
    n_a = (x_t - n_b * d_xb) // d_xa
    if not (n_a * d_xa + n_b * d_xb == x_t and
            n_a * d_ya + n_b * d_yb == y_t):
        return 0
    if ignore_big:
        if n_a >= 100 or n_b >= 100:
            return 0
    return n_a * BUTTON_A_COST + n_b * BUTTON_B_COST


if __name__ == '__main__':
    problems = load_values()
    print(sum(solve(problem) or 0 for problem in problems))
    big_problems = []
    for problem in problems:
        big = Problem(problem.button_a, problem.button_b,
                      (problem.prize_coords[0] + 10000000000000, problem.prize_coords[1] + 10000000000000))
        big_problems.append(big)
    print(sum(solve(problem, ignore_big=False) or 0 for problem in big_problems))
