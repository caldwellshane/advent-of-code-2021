from aoc.day_10 import load_data, parse_data, part_1, part_2

TEST_DATA = """\
[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]\
"""


def test_parse_data():
    data = parse_data(TEST_DATA)
    assert data[0][0] == "["
    assert data[0][-1] == ">"
    assert data[-1][0] == "<"
    assert data[-1][-1] == "]"


def test_part_1():
    assert part_1(parse_data(TEST_DATA)) == 26397

    # Answer to Part 1:
    assert part_1(load_data()) == 394647


def test_part_2():
    assert part_2(parse_data(TEST_DATA)) == 288957

    # Answer to Part 2:
    assert part_2(load_data()) == 2380061249
