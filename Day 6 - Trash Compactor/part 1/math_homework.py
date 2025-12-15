from utils import default_input_path, read_input_lines


def get_id_operations(operations_str: str) -> dict[str, list[int]]:
    operations = [
        operation.strip() for operation in operations_str.split(" ") if operation
    ]

    operations_ids = {"additions": [], "multiplications": []}
    for id, operation in enumerate(operations):
        if operation == "+":
            operations_ids["additions"].append(id)
        elif operation == "*":
            operations_ids["multiplications"].append(id)

    return operations_ids


def calculate_problems_results(problems: str) -> list[int]:
    pass


if __name__ == "__main__":
    path = default_input_path()
    lines = read_input_lines(path)

    print(lines)
