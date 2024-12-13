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


def get_best(problem: Problem) -> Point | None:
    # best = None
    min_cost = None
    for n_a in range(1, 101):
        for n_b in range(1, 101):
            target = (n_a * problem.button_a.delta_x + n_b * problem.button_b.delta_x,
                      n_a * problem.button_a.delta_y + n_b * problem.button_b.delta_y)
            if target == problem.prize_coords:
                cost = BUTTON_A_COST * n_a + BUTTON_B_COST * n_b
                if min_cost is None or cost < min_cost:
                    min_cost = cost
                    # best = (n_a, n_b)
    return min_cost


if __name__ == '__main__':
    problems = load_values()
    print(sum(get_best(problem) or 0 for problem in problems))
