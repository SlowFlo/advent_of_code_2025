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


def count_zeros_during_clicks(
    rotations: Iterable[str], *, start: int = 50, size: int = 100
) -> int:
    """Return the number of clicks that land the dial on 0.

    Counts every time an individual click during each rotation (including the
    last click of a rotation) causes the dial to point at 0.

    This is computed arithmetically without iterating per-click:
    - For a right rotation, zero is hit at click offsets s where
      (start + s) % size == 0. The minimal positive s is
      s0 = (size - (start % size)) % size; if s0 == 0, the first positive hit is size.
    - For a left rotation, zero is hit at click offsets s where
      (start - s) % size == 0. The minimal positive s is start % size; if s0 == 0, first is size.
    The count for a move of distance d is 0 if d < first; otherwise
    1 + (d - first) // size.
    """
    pos = start % size
    total = 0

    for move in rotations:
        move = move.strip()
        if not move:
            continue

        direction = move[0].upper()
        try:
            distance = int(move[1:])
        except ValueError as exc:
            raise ValueError(f"Invalid move distance in '{move}'") from exc

        d = distance  # raw distance (clicks), we cannot reduce by modulo before counting

        # Compute first positive click offset that lands on 0 for the current direction
        if direction == "R":
            first = (size - (pos % size)) % size
        elif direction == "L":
            first = pos % size
        else:
            raise ValueError(f"Invalid move direction in '{move}': expected L or R")

        if first == 0:
            first = size

        if d >= first:
            hits = 1 + (d - first) // size
            total += hits

        # Update position after the full rotation (can reduce by modulo here)
        pos = apply_rotation(pos, move, size=size)

    return total


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
    # Method 0x434C49434B: count every click that lands on 0
    password = count_zeros_during_clicks(rotations, start=50, size=100)
    print(password)
