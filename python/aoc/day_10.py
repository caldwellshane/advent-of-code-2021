from functools import reduce

from aoc.input import INPUT

DAY = 10


BRACKETS = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}

ERROR_SCORE = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

AUTOCOMPLETE_SCORE = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}


def parse_data(text: str):
    return text.split("\n")


def load_data():
    with open(INPUT / f"day_{DAY:02d}.txt", "r") as f:
        return parse_data(f.read())


def part_1(data):
    score = 0
    for line in data:
        stack = []
        for char in line:
            if char in BRACKETS.keys():
                stack.append(char)
            elif stack != []:
                if char == BRACKETS[stack[-1]]:
                    stack.pop()
                else:
                    score += ERROR_SCORE[char]
                    break
    return score


def part_2(data):
    scores = []
    for line in data:
        score = 0
        stack = []
        for char in line:
            if char in BRACKETS.keys():
                stack.append(char)
            elif stack != []:
                if char == BRACKETS[stack[-1]]:
                    stack.pop()
                else:
                    break
        else:
            score = 0
            for char in reversed(stack):
                score = 5 * score + AUTOCOMPLETE_SCORE[BRACKETS[char]]
            scores.append(score)
    return sorted(scores)[(len(scores) - 1) // 2]


if __name__ == "__main__":
    data = load_data()
    part_1(data)
    part_2(data)
