import csv
from pathlib import Path

from openpyxl import Workbook
from openpyxl.styles import Font


def _check_suffix(path: Path, expected: str) -> None:
    if path.suffix.lower() != expected:
        raise ValueError(
            f"Неверный тип файла: {path.name}. Ожидалось расширение {expected}"
        )


def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    """
    Конвертирует CSV в XLSX.

    Args:
        csv_path:  str путь
        xlsx_path: str путь

    Returns:
        None

    Exceptions:
        FileNotFoundError: если CSV отсутствует
        ValueError: пустой CSV, отсутствует заголовок, неверное расширение
    """
    cp = Path(csv_path)
    xp = Path(xlsx_path)

    _check_suffix(cp, ".csv")
    _check_suffix(xp, ".xlsx")

    if not cp.exists():
        raise FileNotFoundError(f"Файл не найден: {cp}")

    with cp.open(encoding="utf-8", newline="") as f:
        reader = csv.reader(f)
        try:
            header = next(reader)
        except StopIteration:
            raise ValueError("Пустой CSV")

        rows = [row for row in reader]

    if not header or all(cell == "" for cell in header):
        raise ValueError("CSV без заголовка")

    wb = Workbook()
    ws = wb.active
    ws.title = "Sheet1"

    ws.append(header)
    for cell in ws[1]:
        cell.font = Font(bold=True)

    for row in rows:
        ws.append(row)

    for col_idx, _ in enumerate(header, start=1):
        max_len = 8
        for row_idx in range(1, ws.max_row + 1):
            val = ws.cell(row=row_idx, column=col_idx).value
            if val is not None:
                max_len = max(max_len, len(str(val)))
        col_letter = ws.cell(row=1, column=col_idx).column_letter
        ws.column_dimensions[col_letter].width = max_len

    xp.parent.mkdir(parents=True, exist_ok=True)
    wb.save(xp)