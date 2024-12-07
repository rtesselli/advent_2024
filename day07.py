from pathlib import Path


def load_values() -> list[tuple[int, list[int]]]:
    lines = Path("data/day07.txt").read_text().splitlines()
    return [
        (int(line.split(": ")[0]), [int(value) for value in line.split(": ")[1].split()])
        for line in lines
    ]


def is_correct(problem: tuple[int, list[int]]) -> bool:
    def rec(curr: int, operands: list[int]) -> bool:
        if curr == 0:
            return True
        if not operands:
            return False
        last_operand = operands[-1]
        if curr % last_operand == 0:
            ok = rec(curr // last_operand, operands[:-1])
            if ok:
                return True
        return rec(curr - last_operand, operands[:-1])

    start, operands = problem
    return rec(start, operands)


def is_correct2(problem: tuple[int, list[int]]) -> bool:
    def rec(curr: int, operands: list[int]) -> bool:
        if curr == 0:
            return True
        if curr < 0:
            return False
        if not operands:
            return False
        last_operand = operands[-1]
        if curr % last_operand == 0:
            ok = rec(curr // last_operand, operands[:-1])
            if ok:
                return True
        if str(curr).endswith(str(last_operand)):
            remain = str(curr).removesuffix(str(last_operand))
            if not remain:
                return True
            ok = rec(int(remain), operands[:-1])
            if ok:
                return True
        return rec(curr - last_operand, operands[:-1])

    start, operands = problem
    return rec(start, operands)


if __name__ == '__main__':
    problems = load_values()
    correct = [problem for problem in problems if is_correct(problem)]
    print(sum(problem[0] for problem in correct))
    correct = [problem for problem in problems if is_correct2(problem)]
    print(sum(problem[0] for problem in correct))
