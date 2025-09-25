import csv

from entities.data import Data

CSV_FILE = "./assets/deal_tempo_size.csv"

class CsvData():
    @staticmethod
    def read_data_from_csv() -> list[Data]:
        data: list[Data] = []
        with open(CSV_FILE, newline='', encoding='utf-8') as f:
            reader = csv.reader(f, delimiter=',')
            next(reader, None)  # skip the headers
            for row in reader:
                data.append(
                    Data(
                        row[0],
                        row[1],
                        float(row[2]) if row[2] != '' else 0,
                        int(row[3]),
                        bool(row[4]),
                        bool(row[5]),
                        bool(row[6]),
                        bool(row[7]),
                        bool(row[8]),
                        bool(row[9]),
                        bool(row[10]),
                        bool(row[11]),
                        bool(row[12]),
                        bool(row[13]))
                    )
        return data