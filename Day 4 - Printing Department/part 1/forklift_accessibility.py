from utils import default_input_path, read_input_lines


def nb_roll_papers_accessible(grid: str) -> int:
    return grid.count("@")


if __name__ == "__main__":
    path = default_input_path()
    lines = read_input_lines(path)

    print(lines)
