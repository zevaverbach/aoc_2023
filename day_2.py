import pathlib


NUMBERS = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def solution_line(line: str) -> int:
    first_num = None
    pending_chars = ""
    break_out = False
    for char in line:
        if break_out:
            print("breaking")
            break
        if char.isnumeric():
            first_num = char
            pending_chars = ""
            break
        else:
            pending_chars += char
            if pending_chars in NUMBERS:
                first_num = str(NUMBERS[pending_chars])
                break
            else:
                for word in NUMBERS:
                    if pending_chars.startswith(word) or pending_chars.endswith(word):
                        first_num = str(NUMBERS[word])
                        break_out = True
                        break
    if first_num is None:
        return 0
    pending_chars = ""
    for char in line[::-1]:
        if char.isnumeric():
            return int(first_num + char)
        else:
            pending_chars += char
            if pending_chars[::-1] in NUMBERS:
                last_num = str(NUMBERS[pending_chars[::-1]])
                return int(first_num + last_num)
            else:
                for word in NUMBERS:
                    if pending_chars[::-1].startswith(word) or pending_chars[::-1].endswith(word):
                        return int(first_num + str(NUMBERS[word]))
    raise Exception


def solution(input_text: str) -> int:
    total = 0
    for line in input_text.split("\n"):
        solution_for_line = solution_line(line)
        total += solution_for_line
    return total


sample_input = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""
first, second, third, fourth, fifth, sixth, seventh = sample_input.split("\n")
first_solution = solution_line(first)
assert first_solution == 29, first_solution
second_solution = solution_line(second)
assert second_solution == 83, second_solution
third_solution = solution_line(third)
assert third_solution == 13, third_solution
fourth_solution = solution_line(fourth)
assert fourth_solution == 24, fourth_solution
fifth_solution = solution_line(fifth)
assert fifth_solution == 42, fifth_solution
sixth_solution = solution_line(sixth)
assert sixth_solution == 14, sixth_solution
seventh_solution = solution_line(seventh)
assert seventh_solution == 76, seventh_solution
answer = solution(sample_input)
assert answer == 281, answer
print(solution(pathlib.Path("day_1.txt").read_text()))
