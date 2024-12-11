from pathlib import Path


def load_values() -> list[int]:
    line = Path("data/day11.txt").read_text().strip()
    return [int(number) for number in line.split()]

def run(stones: list[int], steps: int) -> list[int]:
    for step_n in range(steps):
        new = []
        for stone in stones:
            str_stone = str(stone)
            if stone == 0:
                new.append(1)
            elif len(str_stone) % 2 == 0:
                left = int(str_stone[:len(str_stone) // 2])
                right = int(str_stone[len(str_stone) // 2:])
                new.append(left)
                new.append(right)
            else:
                new.append(stone * 2024)
        stones = new
    return stones


if __name__ == '__main__':
    stones = load_values()
    stones = run(stones, 25)
    print(len(stones))

