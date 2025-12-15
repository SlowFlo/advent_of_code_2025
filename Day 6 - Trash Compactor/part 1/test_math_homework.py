import pytest

from math_homework import get_id_operations


@pytest.mark.parametrize(
    ["operations_str", "result"],
    [
        ["", {"additions": [], "multiplications": []}],
        ["+", {"additions": [0], "multiplications": []}],
    ],
)
def test_get_id_operations(operations_str, result):
    assert get_id_operations(operations_str) == result
