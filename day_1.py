import pathlib


def solution_line(line: str) -> int:
    first_num = None
    for char in line:
        if char.isnumeric():
            first_num = char
            break
    if first_num is None:
        return 0
    for char in reversed(line):
        if char.isnumeric():
            return int(first_num + char)
    raise Exception


def solution(input_text: str) -> int:
    total = 0
    for line in input_text.split("\n"):
        solution_for_line = solution_line(line)
        total += solution_for_line
    return total


sample_input = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""
first, second, third, fourth = sample_input.split("\n")
first_solution = solution_line(first)
assert first_solution == 12, first_solution
second_solution = solution_line(second)
assert second_solution == 38, second_solution
answer = solution(sample_input)
assert answer == 142, answer
print(solution(pathlib.Path("day_1.txt").read_text()))
