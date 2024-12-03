import re
from pathlib import Path


def load_values() -> str:
    return Path("data/day03.txt").read_text()


def extract_commands(text: str) -> list[tuple[int, int]]:
    matches = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", text)
    return [
        (int(a), int(b))
        for a, b in matches
    ]


def extract_commands_enhanced(text: str) -> list[tuple[int, int]]:
    matches = re.findall(r"(?:mul\((\d{1,3}),(\d{1,3})\)|(do\(\))|(don't\(\)))", text)
    add = True
    out = []
    for a, b, do, dont in matches:
        if add and a and b:
            out.append((int(a), int(b)))
        if do:
            add = True
        if dont:
            add = False
    return out


if __name__ == '__main__':
    memory = load_values()
    print(sum(a * b for a, b in extract_commands(memory)))
    print(sum(a * b for a, b in extract_commands_enhanced(memory)))
