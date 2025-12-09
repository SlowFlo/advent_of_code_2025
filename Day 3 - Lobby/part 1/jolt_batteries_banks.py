from utils import default_input_path, read_input_lines


def find_2_first_biggest_numbers_in_bank(bank: str) -> int:
    first = 0
    second = 0

    for c in bank[:-1]:
        if int(c) > first:
            first = int(c)

    for c in bank[bank.index(str(first)) + 1 :]:
        if int(c) > second:
            second = int(c)

    return int(f"{first}{second}")


if __name__ == "__main__":
    path = default_input_path()
    banks = read_input_lines(path)

    print(banks)
