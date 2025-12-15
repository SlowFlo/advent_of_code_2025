import pytest

from math_homework import get_id_operations, calculate_problems_results


@pytest.mark.parametrize(
    ["operations_str", "result"],
    [
        ["", {"additions": [], "multiplications": []}],
        ["+", {"additions": [0], "multiplications": []}],
        ["*", {"additions": [], "multiplications": [0]}],
        ["+ *", {"additions": [0], "multiplications": [1]}],
        ["+ +", {"additions": [0, 1], "multiplications": []}],
        ["+ * +", {"additions": [0, 2], "multiplications": [1]}],
        ["*   +   *   +  ", {"additions": [1, 3], "multiplications": [0, 2]}],
    ],
)
def test_get_id_operations(operations_str, result):
    assert get_id_operations(operations_str) == result


@pytest.mark.parametrize(
    ["problems", "result"],
    [
        [
            """5
4
+""",
            [9],
        ],
        [
            """7
3
*""",
            [21],
        ],
        [
            """122
0
*""",
            [0],
        ],
        [
            """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """,
            [33210, 490, 4243455, 401],
        ],
    ],
)
def test_calculate_problems_results(problems, result):
    assert calculate_problems_results(problems) == result
