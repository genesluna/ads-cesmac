# Compound interest calculator

import locale

locale.setlocale(locale.LC_ALL, 'pt_BR')

print('\033[36m')
print('┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓')
print('┃      CALCULADORA DE JUROS COMPOSTOS      ┃')
print('┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛')
print('\033[0m')
start_amount = float(input(' → Qual o investimento inicial (R$)? '))
print(' ')
monthly_invest = float(input(' → Qual o investimento mensal (R$)? '))
print(' ')
years = int(input(' → Qual o tempo de investimento (anos)? '))
print(' ')
interest = float(input(' → Qual a taxa de juros estimada (%)? ')) / 100
print(' ')

final_amount = 0

for i in range(0, years):
    if final_amount == 0:
        final_amount = start_amount

    final_amount = (final_amount + (monthly_invest * 12)) * (1 + interest)

print('Com um investimento inicial de ' + str(locale.currency(start_amount, grouping=True)) + ',\n' +
      'um aporte mesal de ' + str(locale.currency(monthly_invest, grouping=True)) + ' e uma taxa' + '\n' +
      'de juros esperada de ' + '{:.2%}'.format(interest) + ' ao ano' + ', você' + '\n' +
      'terá: ' + '\033[01m\033[32m{}\033[00m'.format(locale.currency(final_amount, grouping=True)) +
      ' depois de {} anos.'.format(years))

print(' ')
