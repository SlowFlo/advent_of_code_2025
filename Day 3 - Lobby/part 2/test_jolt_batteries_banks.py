import pytest

from jolt_batteries_banks import find_2_first_biggest_numbers_in_bank


@pytest.mark.parametrize(
    ["bank", "result"],
    [
        ["987654321111111", 987654321111],
        ["811111111111119", 811111111119],
        ["234234234234278", 434234234278],
        ["818181911112111", 888911112111],
    ],
)
def test_find_2_first_biggest_numbers_in_bank(bank, result):
    assert find_2_first_biggest_numbers_in_bank(bank) == result
