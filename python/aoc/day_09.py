from typing import Set, Tuple

import numpy as np

from aoc.input import INPUT

DAY = 9


def parse_data(text: str):
    return np.array([[int(char) for char in line] for line in text.split("\n")], dtype=np.int8)


def load_data():
    with open(INPUT / f"day_{DAY:02d}.txt", "r") as f:
        return parse_data(f.read())


def neighbors(array, i, j):
    imax = np.shape(array)[0] - 1
    jmax = np.shape(array)[1] - 1
    neighbors = {(i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j)}
    if i < 1:
        neighbors.discard((i - 1, j))
    if i >= imax:
        neighbors.discard((i + 1, j))
    if j < 1:
        neighbors.discard((i, j - 1))
    if j >= jmax:
        neighbors.discard((i, j + 1))
    return neighbors


def is_minimum(array, i, j) -> bool:
    return np.all([array[i, j] < array[neighbor] for neighbor in neighbors(array, i, j)])


def part_1(data):
    minimum_indices = []
    for i in range(len(data)):
        for j in range(len(data[0])):
            if is_minimum(data, i, j):
                minimum_indices.append((i, j))
    return sum([data[ij] + 1 for ij in minimum_indices])


def get_boundary(data, basin: Set[Tuple[int, int]]) -> Set[Tuple[int, int]]:
    boundary = set()
    for point in basin:
        boundary |= {neighbor for neighbor in neighbors(data, *point) if not neighbor in basin}
    return boundary


def is_minimum_except_basin(array, basin, i, j):
    return np.all([array[i, j] <= array[neighbor] for neighbor in neighbors(array, i, j) - basin])


def part_2(data):
    minimum_indices = []
    for i in range(len(data)):
        for j in range(len(data[0])):
            if is_minimum(data, i, j):
                minimum_indices.append((i, j))
    basins = [{ij} for ij in minimum_indices]
    for basin in basins:
        in_basin = True
        while in_basin:
            boundary = get_boundary(data, basin)
            new_basin = {
                point
                for point in boundary
                if is_minimum_except_basin(data, basin, *point) and data[point] < 9
            }
            if new_basin == set():
                in_basin = False
            else:
                basin |= new_basin
    sizes = sorted([len(basin) for basin in basins])
    return sizes[-3] * sizes[-2] * sizes[-1]


if __name__ == "__main__":
    data = load_data()
    part_1(data)
    part_2(data)
