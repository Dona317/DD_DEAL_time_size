
import statistics
from csv_data import CsvData
from entities.deal import Deal
from manage_deal import ManageDeal
from plot import Plot
from utils import Utils

if __name__ == "__main__":
    deals: list[Deal] = CsvData.read_data_from_csv()

    deltas_months = ManageDeal.deltas_time_months_for_all_deals(deals)

    avg_months = statistics.mean(deltas_months)
    std_months = statistics.stdev(deltas_months) if len(deltas_months) > 1 else 0.5 # only if there are at least 2 values
    print(f"Avg delta time (months): {avg_months:.2f}")
    print(f"Standard deviation (months): {std_months:.2f}")

    filtered_deltas = Utils.remove_outliers_iqr(deltas_months)

    avg_months = statistics.mean(filtered_deltas)
    std_months = statistics.stdev(filtered_deltas) if len(filtered_deltas) > 1 else 0.5 # only if there are at least 2 values
    print(f"Avg delta time (months) (outlier): {avg_months:.2f}")
    print(f"Standard deviation (months) (outlier): {std_months:.2f}")

    plot = Plot()
    plot.plot_std_data(deltas_months)
    plot.plot_std_data(filtered_deltas)
