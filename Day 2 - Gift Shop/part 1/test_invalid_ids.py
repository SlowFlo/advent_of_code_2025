import pytest

from invalid_ids import range_2_numbers


def test_range_2_numbers_1_1_is_1():
    assert range_2_numbers("1-1") == (1,)


def test_range_2_numbers_1_2_is_1_2():
    assert range_2_numbers("1-2") == (1, 2)


def test_range_2_numbers_1_3_is_1_2_3():
    assert range_2_numbers("1-3") == (1, 2, 3)
