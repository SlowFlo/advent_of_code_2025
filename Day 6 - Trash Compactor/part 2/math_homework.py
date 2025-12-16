from utils import default_input_path, read_input_lines


def get_id_operations(operations_str: str) -> dict[str, list[int]]:
    operations = [operation.strip() for operation in operations_str.split()]

    operations_ids = {"additions": [], "multiplications": []}
    for id, operation in enumerate(operations):
        if operation == "+":
            operations_ids["additions"].append(id)
        elif operation == "*":
            operations_ids["multiplications"].append(id)

    return operations_ids


def calculate_problems_results(problems: str) -> list[int]:
    problems_lines = problems.splitlines()

    operations_ids = get_id_operations(problems_lines[-1])
    numbers_lines = [numbers.split(" ") for numbers in problems_lines[:-1]]

    results = [0 for _ in range(len(numbers_lines[0]))]
    for addition_id in operations_ids["additions"]:
        for numbers in numbers_lines:
            results[addition_id] += int(numbers[addition_id])

    for multiplication_id in operations_ids["multiplications"]:
        results[multiplication_id] = 1
        for numbers in numbers_lines:
            results[multiplication_id] *= int(numbers[multiplication_id])

    return results


def get_problem_numbers(problems: str) -> list[int]:
    lines = problems.splitlines()
    str_numbers = ["" for _ in range(len(lines[0]))]

    for line in lines:
        for i, c in enumerate(line):
            str_numbers[i] += c

    numbers = [int(str_number) for str_number in str_numbers if str_number.strip()]

    return numbers


if __name__ == "__main__":
    path = default_input_path()
    problems = read_input_lines(path, True)[0]

    grand_total = sum(calculate_problems_results(problems))

    print(grand_total)
