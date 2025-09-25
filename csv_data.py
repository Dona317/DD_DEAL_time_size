import csv
from datetime import datetime

from entities.deal import Deal

CSV_FILE = "./assets/deal_tempo_size.csv"

class CsvData():
    @staticmethod
    def read_data_from_csv() -> list[Deal]:
        deals: list[Deal] = []
        with open(CSV_FILE, newline='', encoding='utf-8') as f:
            reader = csv.reader(f, delimiter=',')
            next(reader, None)  # skip the headers
            for row in reader:
                deals.append(
                    Deal(
                        row[0],
                        row[1],
                        float(row[2]) if row[2] != '' else 0,
                        datetime.strptime(row[3], Deal.DATE_FORMATTER),
                        int(row[4]) if row[4] != '' else 0,
                        CsvData.to_bool(row[5]),
                        CsvData.to_bool(row[6]),
                        CsvData.to_bool(row[7]),
                        CsvData.to_bool(row[8]),
                        CsvData.to_bool(row[9]),
                        CsvData.to_bool(row[10]),
                        CsvData.to_bool(row[11]),
                        CsvData.to_bool(row[12]),
                        CsvData.to_bool(row[13]),
                        CsvData.to_bool(row[14])),
                    )
        return deals

    @staticmethod
    def to_bool(value: str) -> bool:
        return value.strip().lower() in ("1", "true", "yes")