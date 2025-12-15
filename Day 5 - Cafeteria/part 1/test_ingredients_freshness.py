import pytest

from ingredients_freshness import is_range_included_in_other_range, merge_ranges


@pytest.mark.parametrize(
    ["range_1", "range_2", "result"],
    [
        ["1-2", "3-5", False],
        ["1-3", "2-5", False],
        ["10-14", "16-20", False],
        ["10-14", "8-20", True],
        ["3-5", "1-20", True],
        ["3-5", "3-5", True],
    ],
)
def test_is_range_included_in_other_range(range_1, range_2, result):
    assert is_range_included_in_other_range(range_1, range_2) == result


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
            ["10-14", "13-20"],
            ["10-20"],
        ],
        [
            ["10-14", "16-20", "12-18"],
            ["10-20"],
        ],
        [
            ["3-5", "10-14", "16-20", "12-18"],
            ["3-5", "10-20"],
        ],
    ],
)
def test_merge_ranges(ranges, result):
    assert merge_ranges(ranges) == result


@pytest.mark.parametrize(
    ["ranges", "id", "result"],
    [
        [
            ["1-2"],
            "1",
            True,
        ],
        [
            ["1-2"],
            "3",
            False,
        ],
        [
            ["1-2", "3-5"],
            ["1-2", "3-5"],
        ],
        [
            ["10-14", "13-20"],
            ["10-20"],
        ],
        [
            ["10-14", "16-20", "12-18"],
            ["10-20"],
        ],
        [
            ["3-5", "10-14", "16-20", "12-18"],
            ["3-5", "10-20"],
        ],
    ],
)
def test_is_id_in_ranges(ranges, id, result):
    assert is_id_in_ranges(ranges, id) == result
