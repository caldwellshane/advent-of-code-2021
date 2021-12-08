from aoc.day_08 import parse_data, load_data, part_1, part_2

TEST_DATA = """
be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce
"""


def test_parse_data():
    data = parse_data(TEST_DATA)
    assert data[0].digits[3] == frozenset("fgaecd") and data[0].output[2] == frozenset("cefbgd")
    assert data[9].digits[5] == frozenset("abcdeg") and data[9].output[3] == frozenset("bagce")


def test_part_1():
    assert part_1(parse_data(TEST_DATA)) == 26

    # Answer to Part 1:
    assert part_1(load_data()) == 409


def test_part_2():
    assert part_2(parse_data(TEST_DATA)) == 61229

    # Answer to Part 2:
    assert part_2(load_data()) == 1024649
