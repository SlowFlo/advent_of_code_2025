import itertools

from utils import default_input_path, read_input_lines


def range_2_numbers(str_range: str) -> tuple[int]:
    beginning, end = str_range.split("-")
    return tuple(range(int(beginning), int(end) + 1))


def is_id_valid(id: str) -> bool:
    if len(id) % 2 == 1:
        return True

    if id[: len(id) // 2] == id[len(id) // 2 :]:
        return False

    return True


def invalid_ids_in_range(str_range: str) -> tuple[int, ...]:
    numbers_in_range = range_2_numbers(str_range)

    return tuple(x for x in numbers_in_range if not is_id_valid(str(x)))


if __name__ == "__main__":
    path = default_input_path()
    ranges = read_input_lines(path)[0].split(",")

    invalid_ids_sum = sum(
        # flatten the iterable (from_iterable(map...) => flatMap in JS)
        itertools.chain.from_iterable(map(invalid_ids_in_range, ranges))
    )
    print(invalid_ids_sum)
