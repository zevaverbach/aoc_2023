import pathlib


sample_input = """..F7.
.FJ|.
SJ.L7
|F--J
LJ..."""


def get_start_cell(rows: list[str]) -> tuple[int, int]:
    for i, row in enumerate(rows):
        for j, char in enumerate(row):
            if char == "S":
                return i, j
    raise Exception


NE_SW = 1, 1
SE_NW = -1, 1
SW_NE = -1, -1
NW_SE = 1, -1


DIRECTIONS = {
    "F": NE_SW,
    "L": SE_NW,
    "J": SW_NE,
    "7": NW_SE,
}


VALID_PAIRS = (
    ("|", "|"),
    ("F", "|"),
    ("7", "|"),
    ("|", "L"),
    ("|", "J"),
    ("-", "-"),
    ("F", "-"),
    ("L", "-"),
    ("-", "7"),
    ("-", "J"),
    ("F", "7"),
    ("F", "J"),
    ("L", "J"),
    ("L", "7"),
    ("J", "7"),
    ("J", "F"),
    ("7", "J"),
    ("7", "L"),
)


def get_next_tile(rows: list[str], s: tuple[int, int]) -> tuple[tuple[str, int, int], str]:
    i, j = s

    for name, (x, _) in DIRECTIONS.items():
        next_tile_x = i + x
        next_tile_y = j

        if next_tile_x < 0 or next_tile_x > len(rows):
            continue

        next_tile = rows[next_tile_x][next_tile_y]

        if next_tile == ".":
            continue
        elif (name, next_tile) not in VALID_PAIRS:
            continue
        else:
            s_serves_as = name
            return (
                (next_tile, next_tile_x, next_tile_y),
                s_serves_as,
            )

    raise Exception


def print_matrix(rows: list[str]) -> None:
    print()
    for idx, row in enumerate(rows):
        if row.strip():
            num_spaces = 2 if len(str(idx)) == 1 else 1 if len(str(idx)) == 2 else 0
            spaces = ""
            for _ in range(num_spaces):
                spaces += " "
            print(f"{spaces}{idx}) {row}")
    print()


def solution(matrix_text: str) -> int:
    rows = matrix_text.split("\n")
    i, j = get_start_cell(rows)

    next_tile_tup, s_serves_as = get_next_tile(rows, s=(i, j))

    next_tile, next_tile_x, next_tile_y = next_tile_tup

    print(f"S is located at {i}, {j}")
    print(f"S serves as '{s_serves_as}'")

    prev_tile_x = i
    prev_tile_y = j
    iters = 1

    ### TRAVERSE

    while next_tile != "S":
        direction_x = next_tile_x - prev_tile_x
        direction_y = next_tile_y - prev_tile_y
        prev_tile_x = next_tile_x
        prev_tile_y = next_tile_y
        if next_tile not in "-|":
            n_x, n_y = DIRECTIONS[next_tile]
            if direction_x == n_x:
                next_tile_y -= n_y
            elif direction_x == -n_x:
                next_tile_y += n_y
            elif direction_y == n_y:
                next_tile_x -= n_x
            elif direction_y == -n_y:
                next_tile_x += n_x
        else:
            if next_tile == "|":
                next_tile_x += direction_x
            elif next_tile == "-":
                next_tile_y += direction_y
        next_tile = rows[next_tile_x][next_tile_y]
        iters += 1
        print(f"i{iters}: {next_tile} {next_tile_x},{next_tile_y}", end=" ")

    print_matrix(rows)

    print(f"{i=}, {j=}")
    return iters // 2


entries = pathlib.Path("day_10.txt").read_text()
print(solution(entries))
