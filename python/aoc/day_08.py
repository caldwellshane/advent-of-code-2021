from dataclasses import dataclass
from functools import reduce
from typing import Callable, Dict, FrozenSet, List, Set, Tuple

from aoc.input import INPUT

DAY = 8


@dataclass
class ScrambledOutput:
    digits: Tuple[FrozenSet[str]]
    output: Tuple[FrozenSet[str]]


def parse_data(text: str) -> List[ScrambledOutput]:
    return [
        ScrambledOutput(
            digits=tuple(frozenset(d) for d in line.split("|")[0].split()),
            output=tuple(frozenset(o) for o in line.split("|")[1].split()),
        )
        for line in text.split("\n")
        if line != ""
    ]


def load_data():
    with open(INPUT / f"day_{DAY:02d}.txt", "r") as f:
        return parse_data(f.read())


def part_1(data):
    return sum(1 if len(o) in {2, 3, 4, 7} else 0 for d in data for o in d.output)


def infer(scrambled_output: ScrambledOutput) -> Dict[int, FrozenSet[str]]:
    """Compute the scrambled map of real digit to set of letters representing that digit."""

    def gather_letters(predicate: Callable[[str], bool]) -> FrozenSet[str]:
        return frozenset(
            {char for word in scrambled_output.digits for char in word if predicate(word)}
        )

    inferred_map = {
        1: gather_letters(lambda word: len(word) == 2),
        7: gather_letters(lambda word: len(word) == 3),
        4: gather_letters(lambda word: len(word) == 4),
        8: gather_letters(lambda word: len(word) == 7),
    }
    inferred_map[3] = gather_letters(lambda word: len(word) == 5 and inferred_map[1] < word)
    inferred_map[9] = gather_letters(lambda word: len(word) == 6 and inferred_map[3] < word)
    inferred_map[6] = gather_letters(lambda word: len(word) == 6 and not inferred_map[1] < word)
    inferred_map[2] = gather_letters(
        lambda word: len(word) == 5 and (inferred_map[8] - inferred_map[9]) < word
    )
    inferred_map[5] = gather_letters(
        lambda word: len(word) == 5 and word not in (inferred_map[2], inferred_map[3])
    )
    inferred_map[0] = gather_letters(lambda word: word not in tuple(inferred_map.values()))
    return inferred_map


def part_2(data):
    count = 0
    for d in data:
        inverted_map = {word: number for number, word in infer(d).items()}
        count += int("".join(str(inverted_map[o]) for o in d.output))
    return count


if __name__ == "__main__":
    data = load_data()
    part_1(data)
    part_2(data)
