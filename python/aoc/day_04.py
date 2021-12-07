from copy import copy
from dataclasses import dataclass, field
from typing import List, Set

import numpy as np

from aoc.input import INPUT

DAY = 4

WINNING_CASES = []
WINNING_CASES += [[(x, y) for x in range(5)] for y in range(5)]  # horizontals
WINNING_CASES += [[(x, y) for y in range(5)] for x in range(5)]  # verticals


@dataclass
class BingoCard:
    index: int
    _numbers: np.ndarray
    _active: np.ndarray = field(
        default_factory=lambda: np.array(np.full((5, 5), False, dtype=bool))
    )

    def activate(self, number: int) -> None:
        idxwhere = np.argwhere(self._numbers == number)
        if len(idxwhere) > 0:
            indices = tuple(idxwhere[0])
            print(f"Activating card {self.index} at {indices}")
            self._active[tuple(indices)] = True

    @property
    def bingo(self) -> bool:
        for winning_case in WINNING_CASES:
            if np.all([self._active[indices] for indices in winning_case]):
                return True
        return False

    @property
    def sum_of_unmarked(self) -> int:
        return np.sum(self._numbers, where=np.logical_not(self._active))

    def __str__(self) -> str:
        string = f"======== Card {self.index} ========"
        for num_row, act_row in zip(self._numbers, self._active):
            string += "\n"
            for number, active in zip(num_row, act_row):
                mark = f" {number:2d}" + ("* " if active else "  ")
                string += mark
        return string


@dataclass
class BingoWinner:
    number: int
    card: BingoCard


@dataclass
class BingoGame:
    _selections: np.ndarray
    _cards: Set[BingoCard]

    def play(self, *, verbose: bool = False) -> List[BingoWinner]:
        """Returns the ordered list of winning cards, together with the number on which each won."""
        cards = copy(self._cards)
        winners = []
        for round, number in enumerate(self._selections):
            if verbose:
                print(f"\n*** Round: {round}, Number {number} selected! ***")
            for card in cards:
                card.activate(number)
                if card.bingo:
                    if verbose:
                        print(f"BINGO!\n{card}")
                    winners.append(BingoWinner(number, card))
            cards = [card for card in cards if not card.bingo]
        return winners


def game_from_string(text: str) -> BingoGame:
    text_blocks = text.split("\n\n")
    selections = np.array([int(x) for x in text_blocks[0].split(",")], dtype=np.uint8)
    cards = [
        np.array([int(x) for x in text_block.split()], dtype=np.uint8).reshape(5, 5)
        for text_block in text_blocks[1:]
    ]
    return BingoGame(
        _selections=selections,
        _cards=[BingoCard(index=idx, _numbers=card) for idx, card in enumerate(cards)],
    )


def load_data() -> BingoGame:
    with open(INPUT / f"day_{DAY:02d}.txt", "r") as f:
        return game_from_string(f.read())


def bingo_report(winner: BingoWinner, *, verbose: bool = False) -> int:
    final_score = winner.number * winner.card.sum_of_unmarked
    if verbose:
        print(f"{winner.card}")
        print(f"Sum of unmarked entries: {winner.card.sum_of_unmarked}")
        print(f"Final score: {final_score}")
    return final_score


def part_1(*, verbose: bool = False) -> int:
    game = load_data()
    winners = game.play(verbose=verbose)
    return bingo_report(winners[0], verbose=verbose)


def part_2(*, verbose: bool = False) -> int:
    game = load_data()
    winners = game.play(verbose=verbose)
    return bingo_report(winners[-1], verbose=verbose)


if __name__ == "__main__":
    # part_1(verbose=True)
    part_2(verbose=True)
