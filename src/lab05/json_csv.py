import csv
import json
from pathlib import Path


def _check_suffix(path: Path, expected: str) -> None:
    """Проверяет расширение файла (регистронезависимо)."""
    if path.suffix.lower() != expected:
        raise ValueError(
            f"Неверный тип файла: {path.name}. Ожидалось расширение {expected}"
        )


def json_to_csv(json_path: str, csv_path: str) -> None:
    """
    Преобразует JSON-файл в CSV.

    Args:
        json_path: str путь
        csv_path:  str путь

    Returns:
        None

    Exceptions:
        FileNotFoundError: если входной файл отсутствует
        ValueError: пустой JSON, неверная структура, неверное расширение
    """
    jp = Path(json_path)
    cp = Path(csv_path)

    _check_suffix(jp, ".json")
    _check_suffix(cp, ".csv")

    if not jp.exists():
        raise FileNotFoundError(f"Файл не найден: {jp}")

    with jp.open(encoding="utf-8") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError as e:
            raise ValueError(f"Некорректный JSON: {e}") from e

    if not data:
        raise ValueError("Пустой JSON или неподдерживаемая структура")

    if not isinstance(data, list):
        raise ValueError("Пустой JSON или неподдерживаемая структура")

    for item in data:
        if not isinstance(item, dict):
            raise ValueError("JSON должен быть списком словарей")

    fieldnames: list[str] = []
    seen: set[str] = set()
    for obj in data:
        for key in obj.keys():
            if key not in seen:
                seen.add(key)
                fieldnames.append(key)

    cp.parent.mkdir(parents=True, exist_ok=True)

    with cp.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, restval="")
        writer.writeheader()
        for obj in data:
            writer.writerow({k: obj.get(k, "") for k in fieldnames})


def csv_to_json(csv_path: str, json_path: str) -> None:
    """
    Преобразует CSV в JSON (список словарей).

    Args:
        csv_path:  str путь
        json_path: str путь

    Returns:
        None

    Exceptions:
        FileNotFoundError: если входной файл отсутствует
        ValueError: пустой CSV, отсутствует заголовок, неверное расширение
    """
    cp = Path(csv_path)
    jp = Path(json_path)

    _check_suffix(cp, ".csv")
    _check_suffix(jp, ".json")

    if not cp.exists():
        raise FileNotFoundError(f"Файл не найден: {cp}")

    with cp.open(encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames is None:
            raise ValueError("CSV без заголовка")
        fieldnames = reader.fieldnames
        rows = [dict(row) for row in reader]

    if not rows:
        raise ValueError("Пустой CSV")

    jp.parent.mkdir(parents=True, exist_ok=True)

    with jp.open("w", encoding="utf-8") as f:
        json.dump(rows, f, ensure_ascii=False, indent=2)