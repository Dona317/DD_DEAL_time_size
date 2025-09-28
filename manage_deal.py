from csv_data import CsvData
from entities.deal import Deal

SECONDS_PER_MONTH = 60 * 60 * 24 * 30

class ManageDeal():
    @staticmethod
    def print_deals(deals: list[Deal]):
        [print(deal) for deal in deals]

    @staticmethod
    def read_data_from_csv() -> list[Deal]:
        deals = CsvData.read_data_from_csv()
        ordered_deals: list[Deal] = ManageDeal.__get_order_deals_by_company_and_date(deals)
        ManageDeal.__init_all_deals(ordered_deals)
        return ordered_deals

    @staticmethod
    def deltas_time_months_for_all_deals(deals: list[Deal]) -> list[float]:

        deltas_months = []

        for i in range(len(deals) - 1):
            if deals[i].company == deals[i+1].company:
                delta = deals[i+1].deal_date - deals[i].deal_date
                deltas_months.append(delta.total_seconds() / SECONDS_PER_MONTH)

        if not deltas_months:
            return []

        return deltas_months

    @staticmethod
    def to_csv_list_str(deals: list[Deal], header: bool = True) -> list:
        data = [ManageDeal.__csv_header()] if header else []
        data += [ManageDeal.__to_csv_line(deal) for deal in deals]
        return data

    @staticmethod
    def get_deals_by_flag(deals: list[Deal], flag: str) -> list[Deal]:
        deals_flagged = [d for d in deals if getattr(d, flag, False)]
        return deals_flagged

    @staticmethod
    def is_in_deals(deal_to_search: Deal, deals: list[Deal]) -> bool:
        for deal in deals:
            if deal.deal_id == deal_to_search.deal_id:
                return True
        return False

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
            "is_prev_gafam","is_prev_bigtech_narrow","is_prev_bigtech_large_excluding_gafamn","is_prev_bigtech_large_composite",
            "is_prev_ai_giant_narrow","is_prev_ai_giant_large","is_prev_no_bigtech","is_prev_big_no_tech","is_prev_acc_inc_custom","is_prev_acc_inc_pb"
        ]

    @staticmethod
    def __to_csv_line(deal: Deal) -> list:
        return [
            deal.deal_date,deal.company,deal.deal_size,deal.deal_date,deal.year_founded,ManageDeal.__to_int(deal.gafam),ManageDeal.__to_int(deal.bigtech_narrow),ManageDeal.__to_int(deal.bigtech_large_excluding_gafamn),
            ManageDeal.__to_int(deal.bigtech_large_composite),ManageDeal.__to_int(deal.ai_giant_narrow),ManageDeal.__to_int(deal.ai_giant_large),ManageDeal.__to_int(deal.no_bigtech),ManageDeal.__to_int(deal.big_no_tech),ManageDeal.__to_int(deal.acc_inc_custom),ManageDeal.__to_int(deal.acc_inc_pb),
            ManageDeal.__to_int(deal.is_prev_gafam),ManageDeal.__to_int(deal.is_prev_bigtech_narrow),ManageDeal.__to_int(deal.is_prev_bigtech_large_excluding_gafamn),ManageDeal.__to_int(deal.is_prev_bigtech_large_composite),
            ManageDeal.__to_int(deal.is_prev_ai_giant_narrow),ManageDeal.__to_int(deal.is_prev_ai_giant_large),ManageDeal.__to_int(deal.is_prev_no_bigtech),ManageDeal.__to_int(deal.is_prev_big_no_tech),ManageDeal.__to_int(deal.is_prev_acc_inc_custom),ManageDeal.__to_int(deal.is_prev_acc_inc_pb)
        ]

    @staticmethod
    def __to_int(value: bool) -> int:
        return 1 if value else 0

    @staticmethod
    def __init_all_deals(deals: list[Deal]):
        for i in range(1, len(deals)):
            previous = deals[i-1]
            current = deals[i]
            if previous.company != current.company:
                continue
            if previous.gafam:
                current.is_prev_gafam = True
            if previous.bigtech_narrow:
                current.is_prev_bigtech_narrow = True
            if previous.bigtech_large_excluding_gafamn:
                current.is_prev_bigtech_large_excluding_gafamn = True
            if previous.bigtech_large_composite:
                current.is_prev_bigtech_large_composite = True
            if previous.ai_giant_narrow:
                current.is_prev_ai_giant_narrow = True
            if previous.ai_giant_large:
                current.is_prev_ai_giant_large = True
            if previous.no_bigtech:
                current.is_prev_no_bigtech = True
            if previous.big_no_tech:
                current.is_prev_big_no_tech = True
            if previous.acc_inc_custom:
                current.is_prev_acc_inc_custom = True
            if previous.acc_inc_pb:
                current.is_prev_acc_inc_pb = True

