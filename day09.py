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
        if value != -1:
            out += value * idx
    return out


def expand2(value: str) -> list[tuple[int, int]]:
    out = []
    curr_id = 0
    for idx, char in enumerate(value):
        if idx % 2 == 0:
            out.append((curr_id, int(char)))
            curr_id += 1
        else:
            if char != "0":
                out.append((-1, int(char)))
    return out


def defrag2(values: list[tuple[int, int]]) -> list[int]:
    idx = len(values) - 1
    while idx > 0:
        value, size = values[idx]
        if value != -1:
            idj = 0
            found = False
            while not found and idj < idx:
                if values[idj][0] == -1 and values[idj][1] >= size:
                    found = True
                else:
                    idj += 1
            if found:
                space_left = values[idj][1] - size
                values[idj] = (value, size)
                if space_left:
                    values.insert(idj + 1, (-1, space_left))
                    idx += 1
                values[idx] = (-1, size)
        idx -= 1
    out = []
    for value, size in values:
        out.extend([value] * size)
    return out


if __name__ == '__main__':
    mem_map = load_string()
    expanded = expand(mem_map)
    defragged = defrag(expanded)
    print(checksum(defragged))
    expanded = expand2(mem_map)
    defragged = defrag2(expanded)
    print(checksum(defragged))
