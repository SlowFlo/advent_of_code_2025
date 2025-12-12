import pytest

from ingredients_freshness import merge_ranges


@pytest.mark.parametrize(
    ["ranges", "result"],
    [
        [
            ["1-2"],
            ["1-2"],
        ],
        [
            ["1-2", "3-5"],
            ["1-2", "3-5"],
        ],
        [
            ["3-5", "10-14", "16-20", "12-18"],
            ["3-5", "10-20"],
        ],
    ],
)
def test_merge_ranges(ranges, result):
    assert merge_ranges(ranges) == result
