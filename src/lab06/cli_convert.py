import argparse

from src.lab05.json_csv import json_to_csv, csv_to_json
from src.lab05.csv_xlsx import csv_to_xlsx


def main():
    parser = argparse.ArgumentParser(description="Конвертеры данных")
    sub = parser.add_subparsers(dest="command")

    p1 = sub.add_parser("json_to_csv", help="JSON в CSV")
    p1.add_argument("--in", dest="input", required=True, help="Входной файл.json")
    p1.add_argument("--out", dest="output", required=True, help="Выходной файл.csv")

    p2 = sub.add_parser("csv_to_json", help="CSV в JSON")
    p2.add_argument("--in", dest="input", required=True, help="Входной файл.csv")
    p2.add_argument("--out", dest="output", required=True, help="Выходной файл.json")

    p3 = sub.add_parser("csv_to_xlsx", help="CSV в XLSX")
    p3.add_argument("--in", dest="input", required=True, help="Входной файл.csv")
    p3.add_argument("--out", dest="output", required=True, help="Выходной файл.xlsx")

    args = parser.parse_args()

    try:
        if args.command == "json_to_csv":
            json_to_csv(args.input, args.output)
        elif args.command == "csv_to_json":
            csv_to_json(args.input, args.output)
        elif args.command == "csv_to_xlsx":
            csv_to_xlsx(args.input, args.output)
        else:
            parser.print_help()
    except FileNotFoundError:
        print("Файл не найден")


if __name__ == "__main__":
    main()
