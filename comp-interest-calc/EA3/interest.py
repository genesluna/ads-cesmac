from investment_plan import InvestmentPlan
from datetime import datetime


class Interest:
    def compound(plan: InvestmentPlan) -> InvestmentPlan:
        current_year = int(datetime.now().strftime('%Y'))
        for i in range(0, plan.years):
            if plan.final_amount == 0:
                plan.final_amount = plan.start_amount

            plan.final_amount = (
                plan.final_amount + (plan.monthly_invest * 12)) * (1 + plan.interest)
            current_year += 1
            plan.Plot.year.append(current_year)
            plan.Plot.value.append(plan.final_amount)

        return plan
