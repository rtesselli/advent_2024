from pathlib import Path


def load_values() -> list[str]:
    return Path("data/day04.txt").read_text().splitlines()


def find_h(irow: int, icol: int, values: list[str]) -> int:
    return int(values[irow][icol: icol + 4] == 'XMAS') + int(values[irow][icol - 3: icol + 1] == 'SAMX')


def find_v(irow: int, icol: int, values: list[str]) -> int:
    up = "".join([values[irow - j][icol] for j in range(4) if irow - j >= 0])
    down = "".join([values[irow + j][icol] for j in range(4) if irow + j < len(values)])
    return int(up == 'XMAS') + int(down == "XMAS")


def find_d(irow: int, icol: int, values: list[str]) -> int:
    lu = "".join([values[irow - j][icol - j] for j in range(4) if irow - j >= 0 and icol - j >= 0])
    ru = "".join([values[irow - j][icol + j] for j in range(4) if irow - j >= 0 and icol + j < len(values[irow])])
    ld = "".join([values[irow + j][icol - j] for j in range(4) if irow + j < len(values) and icol - j >= 0])
    rd = "".join(
        [values[irow + j][icol + j] for j in range(4) if irow + j < len(values) and icol + j < len(values[irow])])
    return int(lu == 'XMAS') + int(ru == 'XMAS') + int(ld == 'XMAS') + int(rd == 'XMAS')


def find_all_xmas(values: list[str]) -> int:
    counts = 0
    for irow, row in enumerate(values):
        for icol, char in enumerate(row):
            if char == 'X':
                counts += find_h(irow, icol, values) + find_v(irow, icol, values) + find_d(irow, icol, values)
    return counts


def find_x_mas(irow: int, icol: int, values: list[str]) -> int:
    return ((((irow - 1 >= 0 and icol - 1 >= 0) and (values[irow - 1][icol - 1] == 'M')) and (
            (irow + 1 < len(values) and icol + 1 < len(values[irow])) and (values[irow + 1][icol + 1] == 'S'))) or (
                    ((irow - 1 >= 0 and icol - 1 >= 0) and (values[irow - 1][icol - 1] == 'S')) and (
                    (irow + 1 < len(values) and icol + 1 < len(values[irow])) and (
                    values[irow + 1][icol + 1] == 'M')))) and (
            (((irow - 1 >= 0 and icol + 1 < len(values[irow])) and (values[irow - 1][icol + 1] == 'M')) and (
                    (irow + 1 < len(values) and icol - 1 >= 0) and (values[irow + 1][icol - 1] == 'S'))) or (
                    ((irow - 1 >= 0 and icol + 1 < len(values[irow])) and (values[irow - 1][icol + 1] == 'S')) and (
                    (irow + 1 < len(values) and icol - 1 >= 0) and (values[irow + 1][icol - 1] == 'M'))))


def find_all_x_mas(values: list[str]) -> int:
    counts = 0
    for irow, row in enumerate(values):
        for icol, char in enumerate(row):
            if char == 'A':
                counts += find_x_mas(irow, icol, values)
    return counts


if __name__ == '__main__':
    matrix = load_values()
    print(find_all_xmas(matrix))
    print(find_all_x_mas(matrix))
