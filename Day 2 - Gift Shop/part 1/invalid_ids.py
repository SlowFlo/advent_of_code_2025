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
