from pathlib import Path


def load_string() -> str:
    return Path("data/day09.txt").read_text().splitlines()[0]


def expand(value: str) -> list[int]:
    out = []
    curr_id = 0
    for idx, char in enumerate(value):
        if idx % 2 == 0:
            out.extend([curr_id] * int(char))
            curr_id += 1
        else:
            out.extend([-1] * int(char))
    return out


def defrag(values: list[int]) -> list[int]:
    left_idx = values.index(-1)
    while left_idx >= 0:
        values[left_idx] = values[-1]
        values.pop(len(values) - 1)
        try:
            left_idx = values.index(-1)
        except ValueError:
            left_idx = -1
    return values


def checksum(values: list[int]) -> int:
    out = 0
    for idx, value in enumerate(values):
        out += value * idx
    return out


if __name__ == '__main__':
    mem_map = load_string()
    expanded = expand(mem_map)
    defragged = defrag(expanded)
    print(checksum(defragged))
