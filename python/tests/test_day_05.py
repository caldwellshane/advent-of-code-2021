import numpy as np
from aoc.day_05 import Segment, load_data, parse_data, part_1, part_2


def test_load_data():
    segments = load_data()
    assert segments[0].p1.y == 861
    assert segments[-1].p0.y == 185
    assert segments[-1].p1.x == 67


TEST_DATA = """
0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
 """
TEST_SEGMENTS = parse_data(TEST_DATA)


def test_part_1():
    assert part_1(TEST_SEGMENTS) == 5
    

    # Answer to Part 1:
    assert part_1(load_data()) == 5690


def test_part_2():
    assert part_2(TEST_SEGMENTS) == 12

    # Answer to Part 2:
    assert part_2(load_data()) == 17741
