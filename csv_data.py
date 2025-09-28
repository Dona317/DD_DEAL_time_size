import csv
from datetime import datetime

from entities.deal import Deal

CSV_FILE_INPUT = "./assets/deal_tempo_size.csv"
CSV_FILE_OUTPUT = "./assets/deal_tempo_size_output.csv"

class CsvData():
    @staticmethod
    def read_data_from_csv() -> list[Deal]:
        deals: list[Deal] = []
        with open(CSV_FILE_INPUT, newline='', encoding='utf-8') as f:
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
                        CsvData.__to_bool(row[5]),
                        CsvData.__to_bool(row[6]),
                        CsvData.__to_bool(row[7]),
                        CsvData.__to_bool(row[8]),
                        CsvData.__to_bool(row[9]),
                        CsvData.__to_bool(row[10]),
                        CsvData.__to_bool(row[11]),
                        CsvData.__to_bool(row[12]),
                        CsvData.__to_bool(row[13]),
                        CsvData.__to_bool(row[14])),
                    )
        return deals

    @staticmethod
    def write_data_to_csv(csv_string_list: list[str]) -> None:
        with open(CSV_FILE_OUTPUT, 'w', newline='', encoding='utf-8') as csvfile:
            spamwriter = csv.writer(csvfile, quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for line in csv_string_list:
                spamwriter.writerow(line)

    @staticmethod
    def __to_bool(value: str) -> bool:
        return value.strip().lower() in ("1", "true", "yes")