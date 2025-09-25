
from csv_data import CsvData
from entities.deal import Deal

if __name__ == "__main__":
    deals: list[Deal] = CsvData.read_data_from_csv()

    companies = Deal.get_unique_companies(deals)
    for company in companies:
        company_deals = Deal.get_deals_by_company_name(deals, company)
        Deal.order_by_deal_date(company_deals)
        Deal.print_deals(company_deals)