from typing import Sequence

from aoc.input import INPUT

DAY = 1


def count_increases(data: Sequence[int]) -> int:
    count = 0
    for idx in range(1, len(data)):
        if data[idx] > data[idx - 1]:
            count += 1
    return count


def three_element_sums(data: Sequence) -> Sequence:
    assert len(data) >= 3, "To generate sums of three elements we require at least three elements."
    return tuple(data[idx - 2] + data[idx - 1] + data[idx] for idx in range(2, len(data)))


def main():
    with open(INPUT / f"day_{DAY:02d}.txt", "r") as f:
        data = tuple(int(num) for num in f.readlines())
    print(f"Part 1: Found {count_increases(data)} increases in depth.")
    print(
        f"Part 2: Found {count_increases(three_element_sums(data))} increases in three-element sum."
    )


if __name__ == "__main__":
    main()
