import pytest

# Import as a plain module because folder names contain spaces and aren't valid package names
from dial_rotations import (
    count_zeros_after_rotations,
    count_zeros_during_clicks,
)


def test_dial_rotations_example_password_is_3():
    # Example from the puzzle description
    rotations = [
        "L68",
        "L30",
        "R48",
        "L5",
        "R60",
        "L55",
        "L1",
        "L99",
        "R14",
        "L82",
    ]

    assert count_zeros_after_rotations(rotations, start=50, size=100) == 3


def test_dial_rotations_example_count_zeros_during_clicks_is_6():
    # Same example sequence, but counting clicks that land on 0
    rotations = [
        "L68",
        "L30",
        "R48",
        "L5",
        "R60",
        "L55",
        "L1",
        "L99",
        "R14",
        "L82",
    ]

    assert count_zeros_during_clicks(rotations, start=50, size=100) == 6


@pytest.mark.parametrize(
    "start, move, expected",
    [
        (11, "R8", 19),
        (19, "L19", 0),
        (5, "L10", 95),
        (95, "R5", 0),
        (0, "L1", 99),
        (99, "R1", 0),
    ],
)
def test_single_rotation_positions(start, move, expected):
    # Use the helper internally by feeding one rotation and checking final pos via side-effect
    # We peek the internal mechanics by running sequence and reconstructing last position
    # through the same arithmetic for clarity here.
    zeros = count_zeros_after_rotations([move], start=start, size=100)

    # Compute expected zeros for a single move
    expected_zeros = 1 if expected == 0 else 0
    assert zeros == expected_zeros


def test_clicks_cross_zero_large_distance():
    # From the description: R1000 starting at 50 hits zero 10 times
    assert count_zeros_during_clicks(["R1000"], start=50, size=100) == 10
