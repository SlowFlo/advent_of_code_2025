from utils import default_input_path, read_input_lines


def get_id_operations(operations: str) -> dict[str, list[int]]:
    return {"additions": [], "multiplications": []}


if __name__ == "__main__":
    path = default_input_path()
    lines = read_input_lines(path)

    print(lines)
