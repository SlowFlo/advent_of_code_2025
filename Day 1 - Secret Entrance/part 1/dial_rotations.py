from __future__ import annotations

from pathlib import Path
from typing import Iterable


def apply_rotation(position: int, move: str, *, size: int) -> int:
    """Apply a single rotation move to the dial and return the new position.

    A move is a string like "L68" or "R5" where the first character is the
    direction (L for left/toward lower numbers, R for right/toward higher
    numbers) and the remaining part is a non-negative integer distance.

    The dial positions are 0..size-1 and wrap around modulo size.
    """
    if not move:
        raise ValueError("Empty move")

    direction = move[0].upper()
    try:
        distance = int(move[1:])
    except ValueError as exc:
        raise ValueError(f"Invalid move distance in '{move}'") from exc

    distance %= size

    if direction == "L":
        return (position - distance) % size
    if direction == "R":
        return (position + distance) % size

    raise ValueError(f"Invalid move direction in '{move}': expected L or R")


def count_zeros_after_rotations(
    rotations: Iterable[str], *, start: int = 50, size: int = 100
) -> int:
    """Return how many times the dial points at 0 after applying each rotation.

    - rotations: iterable of moves like "L68" / "R5".
    - start: starting position (default 50).
    - size: dial size (default 100 for 0..99).
    """
    pos = start % size
    zeros = 0

    for move in rotations:
        move = move.strip()
        if not move:
            continue
        pos = apply_rotation(pos, move, size=size)
        if pos == 0:
            zeros += 1
    return zeros


def _read_input_lines(input_path: Path) -> list[str]:
    return [
        line.strip()
        for line in input_path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


def _default_input_path() -> Path:
    # The input file is puzzle_input.txt in the same folder as this module
    return Path(__file__).with_name("puzzle_input.txt")


if __name__ == "__main__":
    path = _default_input_path()
    rotations = _read_input_lines(path)
    password = count_zeros_after_rotations(rotations, start=50, size=100)
    print(password)
