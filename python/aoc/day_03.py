from typing import Callable, Tuple

import numpy as np

from aoc.input import INPUT

DAY = 3


def is_binary_order(number: int, order: int) -> bool:
    """True if the given number in binary has a 1 at the given order."""
    return True if (number >> order) & 1 else False


def gamma_epsilon_bitstrings(data) -> Tuple[str, str]:
    sum = np.sum(data, axis=1)
    gamma_array = np.where(sum >= 500, True, False)
    gamma = "".join("1" if x else "0" for x in gamma_array)
    epsilon = "".join("0" if x else "1" for x in gamma_array)
    return gamma, epsilon


def load_data():
    data = np.zeros((12, 1000), np.uint8)
    with open(INPUT / f"day_{DAY:02d}.txt", "r") as f:
        for idx, line in enumerate(f.readlines()):
            for jdx, char in enumerate(line[:12]):
                # Transpose the data so that row n is the nth digit of each bitstring
                data[jdx, idx] = char
    return data


def part_1(data):
    gamma_bits, epsilon_bits = gamma_epsilon_bitstrings(data)
    gamma = int(gamma_bits, 2)
    epsilon = int(epsilon_bits, 2)
    print(
        "Part 1:\n"
        f"    γ: {gamma} ({gamma:012b}), ϵ: {epsilon} ({epsilon:012b}), power: {gamma*epsilon}."
    )


def o2_filter_value(bincount: np.ndarray) -> int:
    return np.argmax(bincount) if bincount[0] != bincount[1] else 1


def co2_filter_value(bincount: np.ndarray) -> int:
    return np.argmin(bincount) if bincount[0] != bincount[1] else 0


def get_indices(
    data: np.ndarray, order: int, indices: np.ndarray, rule: Callable[[np.ndarray], int]
) -> np.ndarray:
    print(f"len indices {len(indices)}")
    bincount = np.bincount(data[order, indices])
    print(f"bincount: {bincount}")
    filter_value = rule(bincount)
    return np.array([idx for idx in indices if data[order, idx] == filter_value])


def part_2(data):
    o2_indices = [np.arange(len(data[0]))]
    co2_indices = [np.arange(len(data[0]))]

    for indices, rule in (
        (o2_indices, o2_filter_value),
        (co2_indices, co2_filter_value),
    ):
        for order in range(12):
            print(f"==============================\nOrder {order}\nLen Indices {len(o2_indices)}")
            indices.append(get_indices(data, order, indices[-1], rule))
            print(f"len indices {len(indices[-1])} ({indices[-1][0]})")
            if len(indices[-1]) == 1:
                break
        # print(o2_indices[order + 1])
        # print(co2_indices[order + 1])
    o2_index = o2_indices[-1][0]
    co2_index = co2_indices[-1][0]
    o2_bitstring = "".join(str(bit) for bit in data[:, o2_index])
    co2_bitstring = "".join(str(bit) for bit in data[:, co2_index])
    o2_value = int(o2_bitstring, 2)
    co2_value = int(co2_bitstring, 2)
    print(f"O2 index: {o2_index}, value: {o2_value} ({o2_value:012b}).")
    print(f"CO2 index: {co2_index}, value: {co2_value} ({co2_value:012b}).")
    print(f"Life support value: {o2_value*co2_value}.")


if __name__ == "__main__":
    data = load_data()
    part_1(data)
    part_2(data)
