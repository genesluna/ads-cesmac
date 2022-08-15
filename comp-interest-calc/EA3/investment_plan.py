class InvestmentPlan:
    def __init__(self, start_amount, monthly_invest, years, interest, final_amount=0) -> None:
        self.start_amount = start_amount
        self.monthly_invest = monthly_invest
        self.years = years
        self.interest = interest
        self.final_amount = final_amount

    class Plot:
        year = []
        value = []
