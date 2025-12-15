from utils import default_input_path, read_input_lines


def is_range_included_in_other_range(range_1: str, range_2: str) -> bool:
    range_1_start, range_1_end = range_1.split("-")
    range_2_start, range_2_end = range_2.split("-")
    return (
        int(range_2_start) <= int(range_1_start) <= int(range_1_end) <= int(range_2_end)
    )


def merge_ranges(ranges: list[str]) -> list[str]:
    parsed: list[tuple[int, int]] = []
    for r in ranges:
        start_s, end_s = r.split("-")
        start, end = int(start_s), int(end_s)
        parsed.append((start, end))

    parsed.sort(key=lambda t: (t[0], t[1]))

    merged = [parsed[0]]

    for start, end in parsed:
        last_start, last_end = merged[-1]

        if start <= last_end:
            merged[-1] = (last_start, max(last_end, end))
        else:
            merged.append((start, end))

    return [f"{start}-{end}" for start, end in merged]


def is_id_in_ranges(ranges: list[str], id: str) -> bool:
    pass


if __name__ == "__main__":
    path = default_input_path()
    lines = read_input_lines(path)

    ranges = []
    for line in lines:
        if line == "":
            break

        ranges.append(line)

    print(len(ranges))
    print(len(merge_ranges(ranges)))
