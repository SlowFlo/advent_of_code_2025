import pytest

from forklift_accessibility import (
    total_roll_papers_accessible,
    count_roll_papers_accessible_in_middle_row,
)


@pytest.mark.parametrize(
    ["grid", "result"],
    [
        [
            """...
.@.
...""",
            1,
        ],
        [
            """...
.@@
...""",
            2,
        ],
        [
            """..@
.@@
..@""",
            4,
        ],
        [
            """.@@
.@@
..@""",
            4,
        ],
    ],
)
def test_total_roll_papers_accessible(grid, result):
    assert total_roll_papers_accessible(grid) == result


@pytest.mark.parametrize(
    ["upper_row", "middle_row", "lower_row", "result"],
    [
        ["..@", ".@@", "..@", 2],
        [".@@", ".@@", "..@", 0],
        [".@@", "@@@", "..@", 1],
    ],
)
def test_count_roll_papers_accessible_in_middle_row(
    upper_row, middle_row, lower_row, result
):
    assert (
        count_roll_papers_accessible_in_middle_row(upper_row, middle_row, lower_row)
        == result
    )
