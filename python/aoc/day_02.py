from typing import Tuple

from aoc.input import INPUT

DAY = 2


def update_postiion(direction: str, displacement: int, x: int, y: int) -> Tuple[int, int]:
    """
    Update (x, y) position based on direction and displacement instruction.

    Coordinate system:
      x = horiztonal position
      y = depth, ie. direction of "down" increases y
    """
    if direction == "forward":
        return x + displacement, y
    elif direction == "down":
        return x, y + displacement
    elif direction == "up":
        return x, y - displacement
    else:
        raise ValueError(f"Invalid direction {direction} encountered.")


def part_1():
    x, y = 0, 0
    with open(INPUT / f"day_{DAY:02d}.txt", "r") as f:
        for line in f.readlines():
            direction, displacement = line.split()
            x, y = update_postiion(direction, int(displacement), x, y)
    print(f"Part 1: Final (x, y) = ({x}, {y}). Product x*y = {x*y}.")


def update_postiion_and_aim(
    direction: str, displacement: int, x: int, y: int, aim: int
) -> Tuple[int, int, int]:
    """
    Update (x, y, aim) based on direction and displacement instruction.

    Coordinate system:
      x = horiztonal position
      y = depth, ie. direction of "down" increases y
    """
    if direction == "forward":
        return x + displacement, y + displacement * aim, aim
    elif direction == "down":
        return x, y, aim + displacement
    elif direction == "up":
        return x, y, aim - displacement
    else:
        raise ValueError(f"Invalid direction {direction} encountered.")


def part_2():
    x, y, aim = 0, 0, 0
    with open(INPUT / f"day_{DAY:02d}.txt", "r") as f:
        for line in f.readlines():
            direction, displacement = line.split()
            x, y, aim = update_postiion_and_aim(direction, int(displacement), x, y, aim)
    print(f"Part 2: Final (x, y) = ({x}, {y}). Product x*y = {x*y}.")


def main():
    part_1()
    part_2()


if __name__ == "__main__":
    main()
