def range_2_numbers(str_range: str) -> tuple[int]:
    beginning, end = str_range.split("-")
    return tuple(range(int(beginning), int(end) + 1))


def is_id_valid(id: str) -> bool:
    if len(id) % 2 == 1:
        return True

    if id[: len(id) // 2] == id[len(id) // 2 :]:
        return False

    return True
