import locale
import matplotlib.pyplot as plt
from src.models.investment_plan import InvestmentPlan
from src.util.colors import Colors
import os


class CalcUI:

    def __clear_cli() -> None:
        os.system('cls')

    def __currency_fmt(x, pos) -> str:
        if x >= 1e6:
            fmt = 'R${:1.1f}M'.format(x*1e-6)
        else:
            fmt = 'R${:1.0f}K'.format(x*1e-3)
        return fmt

    def set_locale(locale_id: str) -> None:
        locale.setlocale(locale.LC_ALL, locale_id)

    def print_header() -> None:
        CalcUI.__clear_cli()
        print(Colors.fg.cyan)
        print('┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓')
        print('┃      CALCULADORA DE JUROS COMPOSTOS      ┃')
        print('┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛')
        print(Colors.reset)

    def get_investment_plan() -> InvestmentPlan:
        start_amount = float(input(' → Qual o investimento inicial (R$)? '))
        print(' ')
        monthly_invest = float(input(' → Qual o investimento mensal (R$)? '))
        print(' ')
        years = int(input(' → Qual o tempo de investimento (anos)? '))
        print(' ')
        interest = float(input(' → Qual a taxa de juros estimada (%)? ')) / 100
        print(' ')

        investment_plan = InvestmentPlan(
            start_amount, monthly_invest, years, interest)

        return investment_plan

    def print_plan_results(plan: InvestmentPlan) -> None:
        print('Com um investimento inicial de ' +
              str(locale.currency(plan.start_amount, grouping=True)) + ',')
        print('um aporte mesal de ' +
              str(locale.currency(plan.monthly_invest, grouping=True)) + ' e uma taxa')
        print('de juros esperada de ' +
              '{:.2%}'.format(plan.interest) + ' ao ano' + ', você')
        print('terá: ' + Colors.bold + Colors.fmt_color(Colors.fg.green, locale.currency(
            plan.final_amount, grouping=True)) + ' depois de {} anos.'.format(plan.years))
        print(' ')

    def plot_evolution(plan: InvestmentPlan) -> None:
        should_plot = str(
            input('Deseja visualizar o gráfico de evolução? ').lower())
        if should_plot == 'sim' or should_plot == 's':
            fig, ax = plt.subplots()
            ax.bar(plan.Plot.year, plan.Plot.value)
            ax.yaxis.set_major_formatter(CalcUI.__currency_fmt)
            plt.title('Evolução do investimento')
            plt.xlabel('Ano')
            plt.ylabel('Valor acumulado')
            plt.show()

    def good_bye() -> None:
        print(Colors.bold + Colors.fmt_color(Colors.fg.cyan,
              '\nAté a próxima. Continue investindo!!!\n'))
