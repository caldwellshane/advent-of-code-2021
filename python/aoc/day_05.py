from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Sequence, Tuple

import re

from aoc.input import INPUT

DAY = 5


@dataclass
class Point:
    x: int
    y: int

    def __hash__(self) -> int:
        return hash((self.x, self.y))


REGEX = re.compile(r"(\d+)\D+(\d+)\D+(\d+)\D+(\d+)")


@dataclass
class Segment:
    p0: Point
    p1: Point

    @classmethod
    def from_str(cls, s: str):
        result = REGEX.search(s)
        if result is not None:
            a, b, c, d = tuple(REGEX.search(s).groups())
            return cls(p0=Point(x=int(a), y=int(b)), p1=Point(x=int(c), y=int(d)))
        else:
            return None

    @property
    def is_diagonal(self) -> bool:
        """Segment diagonal if it has unequal points and x and y intervals have equal magnitude."""
        return self.p0.x != self.p1.x and (abs(self.p1.x - self.p0.x) == abs(self.p1.y - self.p0.y))

    @property
    def is_rectilinear(self) -> bool:

        return self.p0.x == self.p1.x or self.p0.y == self.p1.y

    def interpolate(self) -> Tuple[Point, ...]:
        if self.p0.x == self.p1.x:
            m = min(self.p0.y, self.p1.y)
            M = max(self.p0.y, self.p1.y)
            return tuple(Point(self.p0.x, y) for y in range(m, M + 1))
        elif self.p0.y == self.p1.y:
            m = min(self.p0.x, self.p1.x)
            M = max(self.p0.x, self.p1.x)
            return tuple(Point(x, self.p0.y) for x in range(m, M + 1))
        elif self.is_diagonal:
            x_sign = 1 if self.p0.x < self.p1.x else -1
            y_sign = 1 if self.p0.y < self.p1.y else -1
            xm = min(self.p0.x, self.p1.x)
            xM = max(self.p0.x, self.p1.x)
            ym = min(self.p0.y, self.p1.y)
            yM = max(self.p0.y, self.p1.y)
            # The diagonals are parallel to either x=y or x=-y
            if x_sign == y_sign:
                return tuple(Point(x, y) for x, y in zip(range(xm, xM + 1), range(ym, yM + 1)))
            else:
                return tuple(Point(x, y) for x, y in zip(range(xm, xM + 1), range(yM, ym - 1, -1)))
        else:
            raise ValueError(f"Segment is neither rectilinear nor diagonal.")


class Registry(dict):
    """All the Points that belong to any, with values of how many segments they belong to."""
    def add(self, point: Point):
        if point not in self.keys():
            self[point] = 1
        else:
            self[point] += 1


def parse_data(text: str) -> Sequence[Segment]:
    segments = []
    for line in text.split("\n"):
        s = Segment.from_str(line)
        if s is not None:
            segments.append(s)
    return segments


def load_data() -> Sequence[Segment]:
    with open(INPUT / f"day_{DAY:02d}.txt", "r") as f:
        return parse_data(f.read())


def part_1(data) -> int:
    registry = Registry()
    for segment in data:
        if segment.is_rectilinear:
            for point in segment.interpolate():
                registry.add(point)
    return len([point for point in registry if registry[point] > 1])


def part_2(data):
    registry = Registry()
    for segment in data:
        for point in segment.interpolate():
            registry.add(point)
    return len([point for point in registry if registry[point] > 1])


if __name__ == "__main__":
    data = load_data()
    print(f"Part 1: {part_1(data)}")
    print(f"Part 2: {part_2(data)}")
