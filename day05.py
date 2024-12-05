from pathlib import Path
from collections import defaultdict
from functools import cmp_to_key


def load_values() -> tuple[dict[int, set[int]], list[list[int]]]:
    text = Path("data/day05.txt").read_text()
    rules_text, pages_text = text.split("\n\n")
    rules = rules_text.splitlines()
    pages = pages_text.splitlines()
    rules_map = defaultdict(set)
    for rule in rules:
        left, right = rule.split("|")
        left = int(left)
        right = int(right)
        rules_map[left].add(right)
    return rules_map, [[int(value) for value in row.split(",")] for row in pages]


def is_correct(page_update: list[int], rule_map: dict[int, set[int]]) -> bool:
    for icur, curr_page in enumerate(page_update):
        for icheck in range(icur):
            if page_update[icheck] in rule_map[curr_page]:
                return False
    return True


def get_middle(page_update: list[int]) -> int:
    return page_update[len(page_update) // 2]


def compare(a: int, b: int) -> int:
    if b in rule_map[a]:
        return -1
    if a in rule_map[b]:
        return 1
    return 0


def fix(page_update: list[int]) -> list[int]:
    return sorted(page_update, key=cmp_to_key(compare))


if __name__ == '__main__':
    rule_map, page_updates = load_values()
    correct = [page_update for page_update in page_updates if is_correct(page_update, rule_map)]
    print(sum(get_middle(page_update) for page_update in correct))
    not_correct = [page_update for page_update in page_updates if not is_correct(page_update, rule_map)]
    fixed = [fix(page_update) for page_update in not_correct]
    print(sum(get_middle(page_update) for page_update in fixed))
