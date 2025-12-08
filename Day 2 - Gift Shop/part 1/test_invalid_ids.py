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


def test_is_id_valid():
    assert is_id_valid(1)


def test_range_2_numbers_1_3_is_1_2_3():
    assert range_2_numbers("1-3") == (1, 2, 3)
