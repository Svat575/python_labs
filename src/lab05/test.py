import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from src.lab05.csv_xlsx import csv_to_xlsx
from src.lab05.json_csv import csv_to_json, json_to_csv

DATA = ROOT / "data" / "lab05"

json_to_csv(DATA / "samples/people.json", DATA / "out/people_from_json.csv")
csv_to_json(DATA / "samples/people.csv", DATA / "out/people_from_csv.json")
csv_to_xlsx(DATA / "samples/cities.csv", DATA / "out/people.xlsx")