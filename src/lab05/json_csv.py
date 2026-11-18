import csv
import json
from pathlib import Path


def json_to_csv(json_path: str, csv_path: str) -> None: # Переводит json в csv
    file = Path(json_path)

    if not file.exists():
        raise FileNotFoundError('Файл не существует')
    if file.suffix != '.json':
        raise ValueError('Файл должен быть .json')

    with open(file, encoding='utf-8') as f:
        data = json.load(f)

    if not data or type(data) is not list or not all(type(item) is dict for item in data):
        raise ValueError("Пустой или неверный JSON")

    colums = []
    for item in data:
        for key in item:
            if key not in colums:
                colums.append(key)

    with open(csv_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(colums)
        for item in data:
            values = []
            for i in colums:
                values.append(item.get(i, ''))
            writer.writerow(values)


def csv_to_json(csv_path: str, json_path: str) -> None: # Переводит csv в json
    file = Path(csv_path)

    if not file.exists():
        raise FileNotFoundError('Файл не существует')
    if file.suffix != '.csv':
         raise ValueError('Файл должен быть .csv')

    with open(file, encoding='utf-8') as f:
        i = csv.DictReader(f)
        data = list(i)
        if not i.fieldnames:
                raise ValueError('Пустой CSV или нет заголовка')

    if not data:
        raise ValueError('В CSV нет данных')

    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    json_to_csv('data/lab05/samples/people.json', 'data/lab05/out/people_from_json.csv')
    csv_to_json('data/lab05/samples/people.csv', 'data/lab05/out/people_from_csv.json')
    json_to_csv('data/lab05/samples/products.json', 'data/lab05/out/products_from_json.csv')
    csv_to_json('data/lab05/samples/students.csv', 'data/lab05/out/students_from_csv.json')
