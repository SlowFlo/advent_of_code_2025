from utils import default_input_path, read_input_lines


def total_roll_papers_accessible(grid: str) -> int:
    return grid.count("@")


def count_roll_papers_accessible_in_middle_row(
    upper_row: str, middle_row: str, lower_row: str
) -> int:
    result = 0
    for [i, c] in enumerate(middle_row):
        if i == 0:
            start = 0
            middle_row_slice = slice(i + 1, i + 2)
        else:
            start = i - 1
            middle_row_slice = slice(i - 1, i + 2, 2)

        print(
            upper_row[start : i + 2],
            upper_row[start : i + 2].count("@"),
        )
        print(
            middle_row[middle_row_slice],
            middle_row[middle_row_slice].count("@"),
        )
        print(
            lower_row[start : i + 2],
            lower_row[start : i + 2].count("@"),
        )
        print()
        if (
            c == "@"
            and upper_row[start : i + 2].count("@")
            + middle_row[middle_row_slice].count("@")
            + lower_row[start : i + 2].count("@")
            < 4
        ):
            result += 1

    return result


if __name__ == "__main__":
    path = default_input_path()
    lines = read_input_lines(path)

    print(lines)
