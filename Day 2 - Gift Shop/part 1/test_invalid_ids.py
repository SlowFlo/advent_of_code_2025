import pytest

from invalid_ids import range_2_numbers, is_id_valid


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
    ],
)
def test_is_id_valid(id, result):
    assert is_id_valid(id) is result


def test_range_2_numbers_1_3_is_1_2_3():
    assert range_2_numbers("1-3") == (1, 2, 3)
