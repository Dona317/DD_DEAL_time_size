
from csv_data import CsvData
from entities.data import Data

if __name__ == "__main__":
    data: list[Data] = CsvData.read_data_from_csv()

    for d in data:
        print(d)