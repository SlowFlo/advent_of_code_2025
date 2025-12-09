import pytest

from jolt_batteries_banks import find_2_first_biggest_numbers_in_bank


@pytest.mark.parametrize(
    ["bank", "result"],
    [
        ["987654321111111", "98"],
        ["811111111111119", "89"],
        ["234234234234278", "78"],
        ["818181911112111", "92"],
    ],
)
def test_find_2_first_biggest_numbers_in_bank(str_range, result):
    assert find_2_first_biggest_numbers_in_bank(str_range) == result
