
from csv_data import CsvData
from entities.deal import Deal
from manage_deal import ManageDeal

if __name__ == "__main__":
    deals: list[Deal] = CsvData.read_data_from_csv()

    avg_months = ManageDeal.avg_delta_time_months_for_all_deals(deals)
    print(f"Avg delta time (months): {round(avg_months, 2)}")
