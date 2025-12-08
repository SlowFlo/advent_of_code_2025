import pytest

from invalid_ids import range_2_numbers


def test_range_2_numbers_1_1_is_1():
    assert range_2_numbers("1-1") == (1,)
