from pathlib import Path
from collections import Counter


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


def run_efficient(stones: list[int], steps: int) -> Counter:
    counts = Counter()
    for stone in stones:
        counts[stone] += 1
    for step_n in range(steps):
        new = Counter()
        new[1] = counts[0]
        evens = set()
        others = set()
        for n in counts.keys():
            if len(str(n)) % 2 == 0:
                evens.add(n)
            elif n != 0:
                others.add(n)
        for n in others:
            new[n * 2024] = counts[n]
        for n in evens:
            str_n = str(n)
            left = int(str_n[:len(str_n) // 2])
            right = int(str_n[len(str_n) // 2:])
            new[left] += counts[n]
            new[right] += counts[n]
        counts = new
    return counts


if __name__ == '__main__':
    stones = load_values()
    stones = run(stones, 25)
    print(len(stones))
    stones = load_values()
    stones = run_efficient(stones, 75)
    print(sum(stones.values()))
