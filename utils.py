import inspect
from pathlib import Path


def default_input_path() -> Path:
    # inspect.stack() renvoie une liste de frames (cadres de pile)
    # L'index 0 est la frame courante, l'index 1 est celle de l'appelant
    caller_frame = inspect.stack()[1]

    # caller_frame.filename contient le chemin du fichier
    return Path(caller_frame.filename).with_name("puzzle_input.txt")


def read_input_lines(input_path: Path) -> list[str]:
    return [
        line.strip()
        for line in input_path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
