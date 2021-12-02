from aoc.day_01 import count_increases, three_element_sums


def test_count_increasing():
    data = (1, 2, 4, 3, 3, -12, -11, -11, 7)
    assert count_increases(data) == 4


def test_three_element_sums():
    data = (1, 2, 4, 3, 3, -12, -11, -11, 7)
    assert three_element_sums(data) == (7, 9, 10, -6, -20, -34, -15)
