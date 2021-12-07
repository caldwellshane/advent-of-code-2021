from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable, Dict, Optional, Sequence, Set, Tuple, List

from aoc.input import INPUT

DAY = 6


@dataclass
class Lanternfish:
    timer: int = 8

    def age_a_day(self) -> Optional[Lanternfish]:
        if self.timer == 0:
            self.timer = 6
            return Lanternfish()
        else:
            self.timer -= 1
            return None


def parse_data(text: str) -> List[Lanternfish]:
    return [Lanternfish(timer=int(value)) for value in text.split(",")]


def load_data() -> List[Lanternfish]:
    with open(INPUT / f"day_{DAY:02d}.txt", "r") as f:
        return parse_data(f.read())


def part_1(fishes: List[Lanternfish], days: int) -> int:
    for _ in range(days):
        new_fishes = []
        for fish in fishes:
            new_fish = fish.age_a_day()
            if new_fish is not None:
                new_fishes.append(new_fish)
        fishes += new_fishes
    return len(fishes)


@dataclass
class FishPopulation:
    histogram: Dict[int, int]  # timer: number with that timer
    
    @classmethod
    def from_fishes(cls, fishes: List[Lanternfish]) -> FishPopulation:
        histo = {timer: 0 for timer in range(9)}
        for fish in fishes:
            histo[fish.timer] += 1
        return cls(histogram=histo)
    
    def age_a_day(self) -> None:
        new_histo = {timer-1: number for timer, number in self.histogram.items() if timer > 0}
        new_histo[6] += self.histogram[0]
        new_histo[8] = self.histogram[0]
        self.histogram = new_histo
    
    def total(self) -> int:
        return sum(self.histogram.values())

def part_2(fishes: List[Lanternfish], days: int) -> int:
    population = FishPopulation.from_fishes(fishes)
    for _ in range(days):
        print(f"Day {_}: Total: {population.total()}")
        population.age_a_day()
    return population.total()


if __name__ == "__main__":
    data = load_data()
    # print(f"Part 1: {part_1(data, 80)}")
    print(f"Part 2: {part_2(data, 256)}")
