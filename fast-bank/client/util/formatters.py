import locale

locale.setlocale(locale.LC_ALL, 'pt_BR')


def format_currency(value: float) -> str:
    return str(locale.currency(value, grouping=True))
