from entities.deal import Deal

SECONDS_PER_MONTH = 60 * 60 * 24 * 30

class ManageDeal():
    @staticmethod
    def print_deals(deals: list[Deal]):
        [print(deal) for deal in deals]

    @staticmethod
    def deltas_time_months_for_all_deals(deals: list[Deal]) -> list[float]:
        ordered_deals: list[Deal] = ManageDeal.__get_order_deals_by_company_and_date(deals)

        deltas_months = []

        for i in range(len(ordered_deals) - 1):
            if ordered_deals[i].company == ordered_deals[i+1].company:
                delta = ordered_deals[i+1].deal_date - ordered_deals[i].deal_date
                deltas_months.append(delta.total_seconds() / SECONDS_PER_MONTH)

        if not deltas_months:
            return []

        return deltas_months

    @staticmethod
    def to_csv_list_str(deals: list[Deal], header: bool = True) -> list[str]:
        data = [ManageDeal.__csv_header()] if header else []
        data += [ManageDeal.__to_csv_line(deal) for deal in deals]
        return data

    @staticmethod
    def __get_unique_companies(deals: list[Deal]) -> list[str]:
        companies = {deal.company for deal in deals}
        return list(companies)

    @staticmethod
    def __get_deals_by_company_name(all_deals: list[Deal], company_name: str) -> list[Deal]:
        company_deals = [deal for deal in all_deals if deal.company == company_name]
        return company_deals

    @staticmethod
    def __order_by_deal_date(deals: list[Deal]) -> None:
        deals.sort(key=lambda deal: deal.deal_date)

    @staticmethod
    def __get_order_deals_by_company_and_date(deals: list[Deal]) -> list[Deal]:
        ordered_deals_by_company_and_date = []
        companies = ManageDeal.__get_unique_companies(deals)
        for company in companies:
            company_deals = ManageDeal.__get_deals_by_company_name(deals, company)
            ManageDeal.__order_by_deal_date(company_deals)
            ordered_deals_by_company_and_date.extend(company_deals)
        return ordered_deals_by_company_and_date

    @staticmethod
    def __csv_header() -> list:
        return [
            "deal_id","company","deal_size","deal_date","year_founded","gafam","bigtech_narrow","bigtech_large_excluding_gafamn",
            "bigtech_large_composite","ai_giant_narrow","ai_giant_large","no_bigtech","big_no_tech","acc_inc_custom","acc_inc_pb",
            "is_prev_gafam","is_prev_bigtech_narroFalsew","is_prev_bigtech_large_excludinFalseg_gafamn","is_prev_bigtech_large_composite",
            "is_prev_ai_giant_narrow","is_prev_ai_giant_large","is_prev_no_bigtech","is_prev_big_no_tech","is_prev_acc_inc_customFalse","is_prev_acc_inc_pb"
        ]

    @staticmethod
    def __to_csv_line(deal: Deal) -> list:
        return [
            deal.deal_date,deal.company,deal.deal_size,deal.deal_date,deal.year_founded,deal.gafam,deal.bigtech_narrow,deal.bigtech_large_excluding_gafamn,
            deal.bigtech_large_composite,deal.ai_giant_narrow,deal.ai_giant_large,deal.no_bigtech,deal.big_no_tech,deal.acc_inc_custom,deal.acc_inc_pb,
            deal.is_prev_gafam,deal.is_prev_bigtech_narroFalsew,deal.is_prev_bigtech_large_excludinFalseg_gafamn,deal.is_prev_bigtech_large_composite,
            deal.is_prev_ai_giant_narrow,deal.is_prev_ai_giant_large,deal.is_prev_no_bigtech,deal.is_prev_big_no_tech,deal.is_prev_acc_inc_customFalse,deal.is_prev_acc_inc_pb
        ]