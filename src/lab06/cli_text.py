import argparse
from pathlib import Path

from src.lib.text import normalize, tokenize, count_freq, top_n


def cat(path: str, number: bool) -> None:
    try: 
        file = Path(path)
        with file.open(encoding = 'utf-8') as f:
            number_line = 1
            for line in f:
                line = line.strip('\n')
                if number: 
                    print(number_line, line)
                else:
                    print(line)
                number_line+=1
    except FileNotFoundError:
        print("Файл не найден")


def stats(path: str, top: int) -> None:
    try:
        file = Path(path)
        with file.open(encoding = 'utf-8') as f:
            text = f.read()
            freq = count_freq(tokenize(normalize(text)))
            for key, value in top_n(freq, top):
                print(f'{key}: {value}')
    except FileNotFoundError:
        print("Файл не найден")


def main():
    parser = argparse.ArgumentParser(description="CLI‑утилиты")
    subparsers = parser.add_subparsers(dest="command")

    cat_parser = subparsers.add_parser("cat", help="Вывод содержания файла")
    cat_parser.add_argument("--input", required=True, help="Путь к файлу")
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")

    stats_parser = subparsers.add_parser("stats", help="Вывод частоты слов")
    stats_parser.add_argument("--input", required=True, help="Путь к файлу")
    stats_parser.add_argument("--top", type=int, default=5, help="Сколько слов вывести")

    args = parser.parse_args()

    try:
        if args.command == 'cat':
            cat(args.input, args.n)
        elif args.command == 'stats':
            if args.top <=0:
                parser.error("--top должен быть больше 0")
            stats(args.input, args.top)
        else:
            parser.print_help()
    except FileNotFoundError:
        print("Файл не найден")


if __name__ == '__main__':
    main()
