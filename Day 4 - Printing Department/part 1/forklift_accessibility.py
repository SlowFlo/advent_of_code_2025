from functools import reduce

from utils import default_input_path, read_input_lines


def total_roll_papers_accessible(grid: str) -> int:
    return grid.count("@")


def count_roll_papers_accessible_in_middle_row(
    upper_row: str | None, middle_row: str, lower_row: str | None
) -> int:
    result = 0

    for [i, c] in enumerate(middle_row):
        if i == 0:
            start = 0
            middle_row_slice = slice(i + 1, i + 2)
        else:
            start = i - 1
            middle_row_slice = slice(i - 1, i + 2, 2)

        if upper_row is None:
            upper_count = 0
        else:
            upper_count = upper_row[start : i + 2].count("@")

        if lower_row is None:
            lower_count = 0
        else:
            lower_count = lower_row[start : i + 2].count("@")

        if (
            c == "@"
            and upper_count + middle_row[middle_row_slice].count("@") + lower_count < 4
        ):
            result += 1

    return result


if __name__ == "__main__":
    path = default_input_path()
    lines = read_input_lines(path)

    print(lines)
