from aoc.day_06 import load_data, parse_data, part_1, part_2


def test_load_data():
    fishes = load_data()
    assert fishes[0].timer == 3
    assert fishes[-1].timer == 5


TEST_DATA = """
3,4,3,1,2
 """
TEST_FISHES = parse_data(TEST_DATA)

def test_part_1():
    assert part_1(TEST_FISHES, 80) == 5934
    
    # Answer to Part 1:
    assert part_1(load_data(), 80) == 362740


def test_part_2():
    assert part_2(TEST_FISHES, 256) == 26984457539

    # Answer to Part 2:
    assert part_2(load_data(), 256) == 1644874076764
