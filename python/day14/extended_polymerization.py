from collections import Counter

INPUT_FILE = "../../input/14.txt"

Ruleset = dict[str, str]


def parse_input() -> tuple[str, Ruleset]:
    """
    Parses the input and returns the polymer template and the pair insertion rules
    """
    with open(INPUT_FILE) as f:
        template, _, *rules = f.read().splitlines()
    ruleset = dict(rule.split(" -> ") for rule in rules)
    return (template, ruleset)


def step(ruleset: Ruleset, pair_counter: Counter[str]) -> Counter[str]:
    """
    Applies a single step to the given pair_counter
    """
    new_pair_counter: Counter[str] = Counter()

    for pair, count in pair_counter.items():
        inserted = ruleset[pair]
        first, second = pair
        new_pair_counter[first + inserted] += count
        new_pair_counter[inserted + second] += count

    return new_pair_counter


def calculate_answer(template: str, pair_counter: Counter[str]) -> int:
    """
    Calculates how many times each letter occurs by adding the counts of pairs
    where the given letter comes first and 1 for the last letter of the original
    template (which does not change), then subtracts the lowest count from the
    highest count and returns the answer
    """
    letter_counter = Counter(template[-1])

    for pair, count in pair_counter.items():
        first_letter, _ = pair
        letter_counter[first_letter] += count

    return max(letter_counter.values()) - min(letter_counter.values())


def solve(template: str, ruleset: Ruleset) -> tuple[int, int]:
    """
    Calculates the required answers given the original template and the pair
    insertion rules
    """
    pairs = ("".join(pair) for pair in zip(template, template[1:]))
    pair_counter = Counter(pairs)

    for _ in range(10):
        pair_counter = step(ruleset, pair_counter)

    part1 = calculate_answer(template, pair_counter)

    for _ in range(30):
        pair_counter = step(ruleset, pair_counter)

    part2 = calculate_answer(template, pair_counter)

    return (part1, part2)


if __name__ == "__main__":
    template, ruleset = parse_input()
    part1, part2 = solve(template, ruleset)
    print(part1)
    print(part2)
