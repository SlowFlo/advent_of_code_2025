import pytest

from math_homework import (
    get_id_operations,
    calculate_problems_results,
    get_problem_numbers,
)


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
            """52
 3
* """,
            [115],
        ],
        [
            """52
3
* """,
            [106],
        ],
        [
            """52
 3
+ """,
            [28],
        ],
        [
            """52
3
+ """,
            [55],
        ],
        [
            """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """,
            [8544, 625, 3253600, 1058],
        ],
    ],
)
def test_calculate_problems_results(problems, result):
    assert calculate_problems_results(problems) == result


@pytest.mark.parametrize(
    ["problems", "problems_sizes", "result"],
    [
        [
            "5",
            [1],
            [[5]],
        ],
        [
            """5
4""",
            [1],
            [[54]],
        ],
        [
            """12
 4""",
            [2],
            [[1, 24]],
        ],
        [
            """328
64 
98 """,
            [3],
            [[369, 248, 8]],
        ],
        [
            """123 328
 45 64 
  6 98 """,
            [3, 3],
            [[1, 24, 356], [369, 248, 8]],
        ],
    ],
)
def test_get_problems_numbers(problems, problems_sizes, result):
    assert get_problem_numbers(problems, problems_sizes) == result
