import statistics
from csv_data import CsvData
from entities.deal import Deal
from manage_deal import ManageDeal
from plot import Plot
from utils import Utils

if __name__ == "__main__":
    deals: list[Deal] = ManageDeal.read_data_from_csv()

    # d1 = ManageDeal.get_deals_by_flag(deals, "no_bigtech")
    # d2 = ManageDeal.get_deals_by_flag(deals, "bigtech_large_composite")
    # print(f"total_deals: {len(deals)}, deals no_bigtech: {len(d1)}, deals bigtech_large_composite: {len(d2)}")

    # count = 0
    # for deal in deals:
    #     if not ManageDeal.is_in_deals(deal, d1) and not ManageDeal.is_in_deals(deal, d2):
    #         count += 1
    #         print(deal)
    # print(f"remaining: {count}")

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
# Fig 1 – Histogram of deals per year [Python fatto]
plot.plot_deals_per_year(deals)

# Fig 2 – Evolution of # deals by investor category no log line 0m (Trend of BigTech vs Non-BigTech vs Accelerators)
plot.plot_deals_over_time_by_flag_noline(deals, "gafam", log_scale=False)
plot.plot_deals_over_time_by_flag_noline(deals, "bigtech_narrow",  log_scale=False)
#plot.plot_deals_over_time_by_flag_noline(deals, "bigtech_large_excluding_gafamn", log_scale=False)
plot.plot_deals_over_time_by_flag_noline(deals, "bigtech_large_composite", log_scale=False)
plot.plot_deals_over_time_by_flag_noline(deals, "ai_giant_narrow", log_scale=False)
plot.plot_deals_over_time_by_flag_noline(deals, "ai_giant_large", log_scale=False)
#plot.plot_deals_over_time_by_flag_noline(deals, "no_bigtech", log_scale=False)
plot.plot_deals_over_time_by_flag_noline(deals, "big_no_tech", log_scale=False)
plot.plot_deals_over_time_by_flag_noline(deals, "acc_inc_custom", log_scale=False)
plot.plot_deals_over_time_by_flag_noline(deals, "acc_inc_pb", log_scale=False)

'''
# Fig 2 – Evolution of # deals by investor category log line 0m (Trend of BigTech vs Non-BigTech vs Accelerators)
plot.plot_deals_over_time_by_flag_noline(deals, "gafam", log_scale=True)
plot.plot_deals_over_time_by_flag_noline(deals, "bigtech_narrow",  log_scale=True)
#plot.plot_deals_over_time_by_flag_noline(deals, "bigtech_large_excluding_gafamn", log_scale=True)
plot.plot_deals_over_time_by_flag_noline(deals, "bigtech_large_composite", log_scale=True)
plot.plot_deals_over_time_by_flag_noline(deals, "ai_giant_narrow", log_scale=True)
plot.plot_deals_over_time_by_flag_noline(deals, "ai_giant_large", log_scale=True)
#plot.plot_deals_over_time_by_flag_noline(deals, "no_bigtech", log_scale=True)
plot.plot_deals_over_time_by_flag_noline(deals, "big_no_tech", log_scale=True)
plot.plot_deals_over_time_by_flag_noline(deals, "acc_inc_custom", log_scale=True)
plot.plot_deals_over_time_by_flag_noline(deals, "acc_inc_pb", log_scale=True)


# Fig 2 – Evolution of # deals by investor category no log line 3m (Trend of BigTech vs Non-BigTech vs Accelerators)
plot.plot_deals_over_time_by_flag(deals, "gafam", window=3, log_scale=False)
plot.plot_deals_over_time_by_flag(deals, "bigtech_narrow", window=3, log_scale=False)
#plot.plot_deals_over_time_by_flag(deals, "bigtech_large_excluding_gafamn", window=4, log_scale=False)
plot.plot_deals_over_time_by_flag(deals, "bigtech_large_composite", window=3, log_scale=False)
plot.plot_deals_over_time_by_flag(deals, "ai_giant_narrow", window=3, log_scale=False)
plot.plot_deals_over_time_by_flag(deals, "ai_giant_large", window=3, log_scale=False)
#plot.plot_deals_over_time_by_flag(deals, "no_bigtech", window=3, log_scale=False)
plot.plot_deals_over_time_by_flag(deals, "big_no_tech", window=3, log_scale=False)
plot.plot_deals_over_time_by_flag(deals, "acc_inc_custom", window=3, log_scale=False)
plot.plot_deals_over_time_by_flag(deals, "acc_inc_pb", window=3, log_scale=False)

    # Fig 2 – Evolution of # deals by investor category log line 4m (Trend of BigTech vs Non-BigTech vs Accelerators)
plot.plot_deals_over_time_by_flag(deals, "gafam", window=4, log_scale=True)
plot.plot_deals_over_time_by_flag(deals, "bigtech_narrow", window=4, log_scale=True)
#plot.plot_deals_over_time_by_flag(deals, "bigtech_large_excluding_gafamn", window=4, log_scale=True)
plot.plot_deals_over_time_by_flag(deals, "bigtech_large_composite", window=4, log_scale=True)
plot.plot_deals_over_time_by_flag(deals, "ai_giant_narrow", window=4, log_scale=True)
plot.plot_deals_over_time_by_flag(deals, "ai_giant_large", window=4, log_scale=True)
#plot.plot_deals_over_time_by_flag(deals, "no_bigtech", window=4, log_scale=True)
plot.plot_deals_over_time_by_flag(deals, "big_no_tech", window=4, log_scale=True)
plot.plot_deals_over_time_by_flag(deals, "acc_inc_custom", window=4, log_scale=True)
plot.plot_deals_over_time_by_flag(deals, "acc_inc_pb", window=4, log_scale=True)
'''