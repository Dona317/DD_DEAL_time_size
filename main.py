import statistics
from csv_data import CsvData
from entities.deal import Deal
from manage_deal import ManageDeal
from plot import Plot
from utils import Utils

if __name__ == "__main__":
    deals: list[Deal] = ManageDeal.read_data_from_csv()

    deltas_months = ManageDeal.deltas_time_months_for_all_deals(deals)

    avg_months = statistics.mean(deltas_months)
    std_months = statistics.stdev(deltas_months) if len(deltas_months) > 1 else 0.5
    print(f"Avg delta time (months): {avg_months:.2f}")
    print(f"Standard deviation (months): {std_months:.2f}")

    filtered_deltas = Utils.remove_outliers_iqr(deltas_months)

    avg_months = statistics.mean(filtered_deltas)
    std_months = statistics.stdev(filtered_deltas) if len(filtered_deltas) > 1 else 0.5
    print(f"Avg delta time (months) (outlier removed): {avg_months:.2f}")
    print(f"Standard deviation (months) (outlier removed): {std_months:.2f}")

    csv_data = ManageDeal.to_csv_list_str(deals, True)
    CsvData.write_data_to_csv(csv_data)

    plot = Plot()
    # plot.plot_std_data(deltas_months,title="Distribution of deal deltas (months)",xlabel="Delta (months)",ylabel="Frequency")
    # plot.plot_std_data(filtered_deltas,title="Distribution of deal deltas (months) - Outliers removed",xlabel="Delta (months)",ylabel="Frequency")

    plot.plot_deals_over_time_by_flag(deals, "gafam", window=4, log_scale=True)
    plot.plot_deals_over_time_by_flag(deals, "bigtech_narrow", window=4, log_scale=True)
    plot.plot_deals_over_time_by_flag(deals, "bigtech_large_excluding_gafamn", window=4, log_scale=True)
    plot.plot_deals_over_time_by_flag(deals, "bigtech_large_composite", window=4, log_scale=True)
    plot.plot_deals_over_time_by_flag(deals, "ai_giant_narrow", window=4, log_scale=True)
    plot.plot_deals_over_time_by_flag(deals, "ai_giant_large", window=4, log_scale=True)
    plot.plot_deals_over_time_by_flag(deals, "no_bigtech", window=4, log_scale=True)
    plot.plot_deals_over_time_by_flag(deals, "big_no_tech", window=4, log_scale=True)
    plot.plot_deals_over_time_by_flag(deals, "acc_inc_custom", window=4, log_scale=True)
    plot.plot_deals_over_time_by_flag(deals, "acc_inc_pb", window=4, log_scale=True)

