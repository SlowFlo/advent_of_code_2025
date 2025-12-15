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
            """1
1
+""",
            [2],
        ],
        [
            """1
1
*""",
            [1],
        ],
    ],
)
def test_calculate_problems_results(problems, result):
    assert calculate_problems_results(problems) == result
