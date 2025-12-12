from functools import reduce

from utils import default_input_path, read_input_lines


def total_roll_papers_accessible(grid: str) -> int:
    lines = grid.splitlines()
    total = 0

    for i, line in enumerate(lines):
        upper_row = lines[i - 1] if i > 0 else None
        lower_row = lines[i + 1] if i < len(lines) - 1 else None
        total += count_roll_papers_accessible_in_middle_row(upper_row, line, lower_row)

    return total


def _count_neighbors(
    upper_row: str | None, middle_row: str, lower_row: str | None, index: int
) -> int:
    start = max(0, index - 1)
    end = index + 2

    count = 0

    if upper_row is not None:
        count += upper_row[start:end].count("@")

    if lower_row is not None:
        count += lower_row[start:end].count("@")

    if index > 0 and middle_row[index - 1] == "@":
        count += 1
    if index < len(middle_row) - 1 and middle_row[index + 1] == "@":
        count += 1

    return count


def count_roll_papers_accessible_in_middle_row(
    upper_row: str | None, middle_row: str, lower_row: str | None
) -> int:
    result = 0

    for i, c in enumerate(middle_row):
        if c == "@":
            if _count_neighbors(upper_row, middle_row, lower_row, i) < 4:
                result += 1

    return result


if __name__ == "__main__":
    path = default_input_path()
    lines = read_input_lines(path)

    print(lines)
