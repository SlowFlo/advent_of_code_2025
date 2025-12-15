import pytest

from math_homework import get_id_operations


@pytest.mark.parametrize(
    ["operations", "result"],
    [
        ["", {"additions": [], "multiplications": []}],
    ],
)
def test_get_id_operations(operations, result):
    assert get_id_operations(operations) == result
