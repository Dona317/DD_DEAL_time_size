from entities.deal import Deal

class ManageDeal():
    @staticmethod
    def print_deals(deals: list[Deal]):
        [print(deal) for deal in deals]

    @staticmethod
    def avg_delta_time_months_for_all_deals(deals: list[Deal]) -> float:
        ordered_deals: list[Deal] = ManageDeal.__get_order_deals_by_company_and_date(deals)

        total_delta = 0
        count = 0

        for i in range(len(ordered_deals) - 1):
            if ordered_deals[i].company == ordered_deals[i+1].company:
                delta = ordered_deals[i+1].deal_date - ordered_deals[i].deal_date
                total_delta += delta.total_seconds()
                count += 1

        if count == 0:
            return 0

        avg_seconds = total_delta / count
        seconds_per_month = 60 * 60 * 24 * 30
        return avg_seconds / seconds_per_month

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