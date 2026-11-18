from pathlib import Path
from openpyxl import Workbook
import csv


def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None: # Переводит csv в xlsx 
    file = Path(csv_path)

    if not file.exists():
        raise FileNotFoundError('Файл не существует')
    if file.suffix != '.csv':
        raise ValueError('Файл не .csv')

    with open(file, encoding='utf-8') as f:
        reader = csv.reader(f)
        data = list(reader)

    if not data:
        raise ValueError('Файл пустой')

    wb = Workbook()
    ws = wb.active
    ws.title = "Sheet1"

    for item in data:
        ws.append(item)

    for col in ws.columns:
        mx_len = 0
        for i in col:
            if i.value is not None:
                dlina = len(str(i.value))
                if dlina > mx_len:
                    mx_len = dlina
        bukva = col[0].column_letter
        ws.column_dimensions[bukva].width = max(mx_len + 2, 8)

    wb.save(xlsx_path)


if __name__ == '__main__':
    csv_to_xlsx('data/lab05/samples/people.csv', 'data/lab05/out/people.xlsx')
    csv_to_xlsx('data/lab05/samples/cities.csv', 'data/lab05/out/cities.xlsx')
