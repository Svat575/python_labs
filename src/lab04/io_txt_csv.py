import csv
from collections.abc import Iterable, Sequence
from pathlib import Path


def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    """
    Reads text from file

    Args: 
        path: str | Path
        encoding = "utf-8": str

    Returns: 
        Type: str

    Exceptions:
        FileNotFoundError
        UnicodeDecodeError
    """
    p = Path(path)
    return p.read_text(encoding=encoding)

def write_csv(rows: Iterable[Sequence], path: str | Path,
    header: tuple[str, ...] | None = None) -> None:
    """
    Writes CSV-table

    Args:
        rows: Iterable[Sequence]
        path: str | Path
        header: tuple[str, ...] | None = None

    Returns:
        None

    Exceptions:
        ValueError: rows must be similar length.
    """
    p = Path(path)
    rows = list(rows)
    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)
        
        if len(rows) != 0:
            expected_len = len(header) if header is not None else len(rows[0])
            for r in rows:
                if len(r) != expected_len:
                    raise ValueError("rows must be similar length.")
                w.writerow(r)

def ensure_parent_dir(path: str | Path) -> None:
    """
    Creates parent directory.

    Args:
    path: str | Path

    Returns:
        None
    """
    path = Path(path)
    parts = path.parts
    if not Path(*parts[:-1]).exists():
        Path(*parts[:-1]).mkdir()