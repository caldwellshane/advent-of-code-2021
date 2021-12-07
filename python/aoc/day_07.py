import numpy as np
from scipy.optimize import minimize

from aoc.input import INPUT

DAY = 7


def parse_data(text: str):
    return np.array(text.split(","), np.int32)


def load_data():
    with open(INPUT / f"day_{DAY:02d}.txt", "r") as f:
        return parse_data(f.read())


def part_1(data):
    rounded_median = int(
        np.round(np.median(data))
    )  # cost function is |data-pos|, minimized by median
    return np.sum(np.abs(data - rounded_median))


def cost(position: int, data):
    return np.sum(
        0.5 * np.abs(data - position) * (np.abs(data - position) + 1)
    )  # 1 + 2 + ... + |data-pos|


def part_2(data):
    best_position = int(round(minimize(cost, 100, args=(data,)).x[0]))
    return int(round(cost(best_position, data)))


if __name__ == "__main__":
    data = load_data()
    part_1(data)
    part_2(data)
