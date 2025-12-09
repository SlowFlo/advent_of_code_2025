import pytest

from invalid_ids import range_2_numbers, is_id_valid, invalid_ids_in_range


@pytest.mark.parametrize(
    ["str_range", "result"],
    [
        ["1-1", (1,)],
        ["1-2", (1, 2)],
        ["1-3", (1, 2, 3)],
    ],
)
def test_range_2_numbers(str_range, result):
    assert range_2_numbers(str_range) == result


@pytest.mark.parametrize(
    ["id", "result"],
    [
        ["1", True],
        ["11", False],
        ["12", True],
        ["123", True],
        ["12345", True],
        ["1010", False],
        ["1188511885", False],
        ["222222", False],
        ["446446", False],
        ["38593859", False],
        ["223222", True],
        ["1288511885", True],
        ["12341234", False],
        ["123123123", False],
        ["1212121212", False],
        ["1111111", False],
    ],
)
def test_is_id_valid(id, result):
    assert is_id_valid(id) is result


@pytest.mark.parametrize(
    ["str_range", "result"],
    [
        ["1-1", ()],
        ["11-11", (11,)],
        ["11-22", (11, 22)],
        ["95-115", (99, 111)],
        ["998-1012", (999, 1010)],
        ["1188511880-1188511890", (1188511885,)],
        ["222220-222224", (222222,)],
        ["1698522-1698528", ()],
        ["446443-446449", (446446,)],
        ["38593856-38593862", (38593859,)],
        ["565653-565659", (565656,)],
        ["824824821-824824827", (824824824,)],
        ["2121212118-2121212124", (2121212121,)],
    ],
)
def test_invalid_ids_in_range(str_range, result):
    assert invalid_ids_in_range(str_range) == result
