import pytest

from forklift_accessibility import (
    mark_roll_papers_accessible,
    mark_roll_papers_accessible_in_middle_row,
)


@pytest.mark.parametrize(
    ["grid", "result"],
    [
        [
            """...
.@.
...""",
            """...
.X.
...""",
        ],
        [
            """...
.@@
...""",
            """...
.XX
...""",
        ],
        [
            """..@
.@@
..@""",
            """..X
.XX
..X""",
        ],
        [
            """.@@
.@@
..@""",
            """.XX
.@@
..X""",
        ],
        [
            """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.""",
            """..XX.XX@X.
X@@.@.@.@@
@@@@@.X.@@
@.@@@@..@.
X@.@@@@.@X
.@@@@@@@.@
.@.@.@.@@@
X.@@@.@@@@
.@@@@@@@@.
X.X.@@@.X.""",
        ],
    ],
)
def test_total_roll_papers_accessible(grid, result):
    assert mark_roll_papers_accessible(grid) == result


@pytest.mark.parametrize(
    ["upper_row", "middle_row", "lower_row", "result"],
    [
        ["..@", ".@@", "..@", ".XX"],
        [".@@", ".@@", "..@", ".@@"],
        [".@@", "@@@", "..@", "X@@"],
        [None, "@@@", "..@", "XXX"],
        ["..@", "@@.", None, "XX."],
        [None, "@.@", None, "X.X"],
    ],
)
def test_mark_roll_papers_accessible_in_middle_row(
    upper_row, middle_row, lower_row, result
):
    assert (
        mark_roll_papers_accessible_in_middle_row(upper_row, middle_row, lower_row)
        == result
    )
