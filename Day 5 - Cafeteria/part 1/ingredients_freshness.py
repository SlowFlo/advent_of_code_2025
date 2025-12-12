from utils import default_input_path, read_input_lines


def is_range_included_in_other_range(range_1: str, range_2: str) -> bool:
    range_1_start, range_1_end = range_1.split("-")
    range_2_start, range_2_end = range_2.split("-")
    print(range_2_start, range_1_start, range_1_end, range_2_end)
    return (
        int(range_2_start) <= int(range_1_start) <= int(range_1_end) <= int(range_2_end)
    )


def merge_ranges(ranges: list[str]) -> list[str]:
    merged_ranges = []

    for i_current_range, current_range in enumerate(ranges):
        current_range_start, current_range_end = current_range.split("-")
        for i_merged_range, merged_range in enumerate(merged_ranges):
            merged_range_start, merged_range_end = merged_range.split("-")
            if is_range_included_in_other_range(current_range, merged_range):
                break

    return ranges


if __name__ == "__main__":
    path = default_input_path()
    lines = read_input_lines(path)

    print(lines)
