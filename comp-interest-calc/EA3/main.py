# Compound interest calculator
from src.ui.calc_ui import CalcUI
from src.util.interest import Interest


def main():
    CalcUI.set_locale('pt-BR')
    CalcUI.print_header()
    investment_plan = CalcUI.get_investment_plan()
    calculated_plan = Interest.compound(investment_plan)
    CalcUI.print_plan_results(calculated_plan)
    CalcUI.plot_evolution(calculated_plan)
    CalcUI.good_bye()


if __name__ == "__main__":
    main()
