import numpy as np
from aoc.day_04 import bingo_report, game_from_string, load_data, part_1, part_2


def test_load_data():
    game = load_data()
    assert game._selections[0] == 28
    assert game._selections[-1] == 52
    assert np.array_equal(
        game._cards[0]._numbers,
        np.array(
            [
                [31, 88, 71, 23, 61],
                [4, 9, 14, 93, 51],
                [52, 50, 6, 34, 55],
                [70, 64, 78, 65, 95],
                [12, 22, 41, 60, 57],
            ]
        ),
    )
    assert np.array_equal(
        game._cards[-1]._numbers,
        np.array(
            [
                [42, 9, 63, 56, 93],
                [79, 59, 38, 36, 7],
                [6, 23, 48, 0, 55],
                [82, 45, 13, 27, 83],
                [1, 32, 8, 40, 46],
            ]
        ),
    )
    assert game._cards[0].index == 0
    assert game._cards[-1].index == 99

    # Make sure the defaulted _active fieldss aren't sharing the same underlying array
    game._cards[-1]._active[0, 0] = True
    assert game._cards[-1]._active[0, 0]
    assert not game._cards[0]._active[0, 0]


TEST_DATA = """
7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
 """

TEST_GAME = game_from_string(TEST_DATA)


def test_part_1():
    winners = TEST_GAME.play()
    assert winners[0].card.index == 2
    assert winners[0].number == 24
    assert bingo_report(winners[0]) == 4512

    # Answer to Part 1:
    assert part_1() == 51034


def test_part_2():
    winners = TEST_GAME.play()
    assert winners[-1].card.index == 1
    assert winners[-1].number == 13
    assert bingo_report(winners[-1]) == 1924

    # Answer to Part 2:
    assert part_2() == 5434
