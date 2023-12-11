import pathlib

sample_input = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""


def solution(data):
    total = 0
    lines = data.split("\n")
    prev_line = None
    for lidx, line in enumerate(lines):
        next_line = None
        if lidx < len(lines) - 1:
            next_line = lines[lidx + 1]

        num = ""

        prev_char = None
        for cidx, char in enumerate(line):
            next_char = None
            if cidx < len(line):
                next_char = line[cidx]

            if char.isnumeric():
                num += char
            else:
                if len(num) > 0:
                    num_int = int(num)
                    len_num = len(num)
                    prev_char = line[cidx - len_num - 1]
                    num = ""
                    if (
                        prev_char is not None and prev_char != "." and not prev_char.isnumeric()
                    ) or (next_char is not None and next_char != "." and not next_char.isnumeric()):
                        total += num_int
                        print(num_int)
                    else:
                        line_indices = []
                        for i in range(len_num + 1):
                            if cidx - i >= 0:
                                line_indices.append(cidx - i)
                        if cidx - len_num - 1 >= 0:
                            line_indices.append(cidx - len_num - 1)
                        if cidx + 1 < (len_num - 1):
                            line_indices.append(cidx + 1)
                        if num_int == 509:
                            print("---")
                            print(509)
                            print(f"{len_num=}")
                            print(f"{line_indices=}")
                            print(f"{prev_line=}")
                            print(f"{line=}")
                            print(f"{next_line=}")
                            print("---")
                        for ix in line_indices:
                            if (
                                prev_line is not None
                                and prev_line[ix] != "."
                                and not prev_line[ix].isnumeric()
                            ):
                                total += num_int
                                print(num_int)
                                # print(f"{ix=}")
                                # print(f"{prev_line[ix]=}")
                                # print(f"{prev_line=}")
                                # print(f"{line=}")
                                break
                            if (
                                next_line is not None
                                and next_line
                                and next_line[ix] != "."
                                and not next_line[ix].isnumeric()
                            ):
                                total += num_int
                                print(num_int)
                                # print(f"{ix=}")
                                # print(f"{next_line[ix]=}")
                                # print(f"{next_line=}")
                                break
        prev_line = line
    return total


# print(solution(sample_input))
print(solution(pathlib.Path("day_3.txt").read_text()))
# print(solution(pathlib.Path("day3_short.txt").read_text()))
