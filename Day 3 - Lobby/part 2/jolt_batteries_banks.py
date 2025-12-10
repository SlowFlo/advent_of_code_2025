from utils import default_input_path, read_input_lines


def find_12_first_biggest_numbers_in_bank(bank: str) -> int:
    current_bank = [int(c) for c in bank]
    batterie_values = []

    for batterie_id in range(1, 12 + 1):
        batteries_left_to_pick = 12 - batterie_id

        if batteries_left_to_pick == 0:
            search_scope = current_bank
        else:
            search_scope = current_bank[:-batteries_left_to_pick]

        found_value = max(search_scope)
        batterie_values.append(found_value)

        index_in_scope = search_scope.index(found_value)

        current_bank = current_bank[index_in_scope + 1 :]

    return int("".join(map(str, batterie_values)))


if __name__ == "__main__":
    path = default_input_path()
    banks = read_input_lines(path)

    total_output_joltage = sum(map(find_2_first_biggest_numbers_in_bank, banks))

    print(total_output_joltage)
