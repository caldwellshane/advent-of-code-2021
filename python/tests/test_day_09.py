import numpy as np
from aoc.day_09 import get_boundary, load_data, parse_data, part_1, part_2

TEST_DATA = """2199943210
3987894921
9856789892
8767896789
9899965678"""


def test_parse_data():
    data = parse_data(TEST_DATA)
    assert data[0, 0] == 2
    assert data[4, 9] == 8


def test_load_data():
    data = load_data()
    assert load_data[0, 0] == 6
    assert load_data[0, 99] == 1
    assert load_data[99, 0] == 4
    assert load_data[99, 99] == 5
    assert np.shape(data) == (100, 100)


def test_part_1():
    assert part_1(parse_data(TEST_DATA)) == 15

    # Answer to Part 1:
    assert part_1(load_data()) == 436


def test_part_2():
    assert part_2(parse_data(TEST_DATA)) == 1134

    # Answer to Part 2:
    assert part_2(load_data()) == 1317792


def test_boundary():
    data = np.arange(25).reshape(5, 5)
    basin = {(2, 2), (2, 3), (3, 2), (3, 3)}
    assert get_boundary(data, basin) == {
        (1, 2),
        (1, 3),
        (4, 2),
        (4, 3),
        (2, 4),
        (3, 4),
        (2, 1),
        (3, 1),
    }
