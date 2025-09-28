from datetime import datetime

class Deal():
    DATE_FORMATTER = r"%d-%b-%Y"

    def __init__(
    self,
    deal_id: str,
    company: str,
    deal_size: float,
    deal_date: datetime,
    year_founded: int,
    gafam: bool,
    bigtech_narrow: bool,
    bigtech_large_excluding_gafamn: bool,
    bigtech_large_composite: bool,
    ai_giant_narrow: bool,
    ai_giant_large: bool,
    no_bigtech: bool,
    big_no_tech: bool,
    acc_inc_custom: bool,
    acc_inc_pb: bool,
    ):
        self.deal_id = deal_id
        self.company = company
        self.deal_size = deal_size
        self.deal_date = deal_date
        self.year_founded = year_founded
        self.gafam = gafam
        self.bigtech_narrow = bigtech_narrow
        self.bigtech_large_excluding_gafamn = bigtech_large_excluding_gafamn
        self.bigtech_large_composite = bigtech_large_composite
        self.ai_giant_narrow = ai_giant_narrow
        self.ai_giant_large = ai_giant_large
        self.no_bigtech = no_bigtech
        self.big_no_tech = big_no_tech
        self.acc_inc_custom = acc_inc_custom
        self.acc_inc_pb = acc_inc_pb
        self.is_prev_gafam = False
        self.is_prev_bigtech_narrow = False
        self.is_prev_bigtech_large_excluding_gafamn = False
        self.is_prev_bigtech_large_composite = False
        self.is_prev_ai_giant_narrow = False
        self.is_prev_ai_giant_large = False
        self.is_prev_no_bigtech = False
        self.is_prev_big_no_tech =False
        self.is_prev_acc_inc_custom = False
        self.is_prev_acc_inc_pb = False

    #TODO: fixhere
    def __str__(self) -> str:
        return f"id: {self.deal_id}, company: {self.company}, size: {self.deal_size}, date: {self.deal_date}, gafam: {self.gafam}"