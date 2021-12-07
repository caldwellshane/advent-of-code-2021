from aoc.input import INPUT

DAY = 0


def parse_data(text: str):
    pass


def load_data():
    with open(INPUT / f"day_{DAY:02d}.txt", "r") as f:
        parse_data(f.read())


def part_1(data):
    pass


def part_2(data):
    pass


if __name__ == "__main__":
    data = load_data()
    part_1(data)
    part_2(data)
