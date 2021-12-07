import numpy as np

from aoc.day_07 import load_data, parse_data, part_1, part_2


TEST_DATA = """
16,1,2,0,4,2,7,1,2,14
"""


def test_parse_data():
    assert np.array_equal(parse_data(TEST_DATA), np.array([16, 1, 2, 0, 4, 2, 7, 1, 2, 14]))


def test_part_1():
    assert part_1(parse_data(TEST_DATA)) == 37

    # Answer to Part 1:
    assert part_1(load_data()) == 336040


def test_part_2():
    assert part_2(parse_data(TEST_DATA)) == 168

    # Answer to Part 2:
    assert part_2(load_data()) == 94813675
