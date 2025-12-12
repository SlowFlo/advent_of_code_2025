from functools import reduce

from utils import default_input_path, read_input_lines


def total_roll_papers_accessible(grid: str) -> int:
    return grid.count("@")


def count_roll_papers_accessible_in_middle_row(
    upper_row: str | None, middle_row: str, lower_row: str | None
) -> int:
    count = 0

    for [i, c] in enumerate(middle_row):
        if c != "@":
            continue

        start = max(0, i - 1)
        end = i + 2

        nb_neighbors = 0

        if upper_row is not None:
            nb_neighbors += upper_row[start:end].count("@")

        if lower_row is not None:
            nb_neighbors += lower_row[start:end].count("@")

        if i > 0 and middle_row[i - 1] == "@":
            nb_neighbors += 1
        if i < len(middle_row) - 1 and middle_row[i + 1] == "@":
            nb_neighbors += 1

        if nb_neighbors < 4:
            count += 1

    return count


if __name__ == "__main__":
    path = default_input_path()
    lines = read_input_lines(path)

    print(lines)
