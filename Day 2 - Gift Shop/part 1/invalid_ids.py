def range_2_numbers(str_range: str) -> tuple[int]:
    beginning, end = str_range.split("-")
    return tuple(range(int(beginning), int(end) + 1))


def is_id_valid(id: int) -> bool:
    return True
