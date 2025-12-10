import pytest

from forklift_accessibility import *


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
def test_find_2_first_biggest_numbers_in_bank(grid, result):
    assert nb_roll_papers_accessible(grid) == result
