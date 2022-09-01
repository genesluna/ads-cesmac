from PySide2.QtWidgets import QMainWindow
from UI.ui_main_window import Ui_MainWindow
from services import users_service as us
from util import messages, formatters


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, user: dict) -> None:
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Banco Fast')
        self.user = user
        self.lbl_greeting.setText(f'Olá, {user["name"]}')
        self.lbl_acount_balance.setText(
            formatters.format_currency(self.user['balance']))
        self.lbl_credit_balance.setText(
            formatters.format_currency(self.user['balance_credit']))
        self.lbl_investment_balance.setText(
            formatters.format_currency(self.user['balance_investment']))

        # Navigation events
        self.btn_home.clicked.connect(self.navigate_home)
        self.btn_deposit.clicked.connect(self.navigate_deposit)
        self.btn_withdraw.clicked.connect(self.navigate_withdraw)

        # Buttons events
        self.btn_deposit_amount.clicked.connect(self.handle_deposit)
        self.btn_withdraw_amount.clicked.connect(self.handle_withdraw)

    def navigate_home(self) -> None:
        self.refresh_user()
        self.lbl_acount_balance.setText(
            formatters.format_currency(self.user['balance']))
        self.Pages.setCurrentWidget(self.page_home)

    def navigate_deposit(self) -> None:
        self.refresh_user()
        self.lbl_acc_balance_deposit.setText(
            formatters.format_currency(self.user['balance']))
        self.Pages.setCurrentWidget(self.page_deposit)

    def navigate_withdraw(self) -> None:
        self.refresh_user()
        self.lbl_acc_balance_withdraw.setText(
            formatters.format_currency(self.user['balance']))
        self.Pages.setCurrentWidget(self.page_withdraw)

    def handle_deposit(self) -> None:
        amount = float(self.txt_deposit_amount.text())

        if amount <= 0:
            messages.show_alert(
                'Erro de validação', 'O valor tem que ser maior que zero.')
            self.txt_withdraw_amount.setText('')
            return None

        us.deposit(self.user['id'], amount)
        self.refresh_user()
        self.lbl_acc_balance_deposit.setText(
            formatters.format_currency(self.user['balance']))
        self.txt_deposit_amount.setText('')

    def handle_withdraw(self) -> None:
        amount = float(self.txt_withdraw_amount.text())

        if amount > self.user['balance']:
            messages.show_alert(
                'Saldo infuficiente', 'O valor que você deseja sacar é maior que o saldo disponível.')
            self.txt_withdraw_amount.setText('')
            return None
        elif amount <= 0:
            messages.show_alert(
                'Erro de validação', 'O valor tem que ser maior que zero.')
            self.txt_withdraw_amount.setText('')
            return None

        us.withdraw(self.user['id'], amount)
        self.refresh_user()
        self.lbl_acc_balance_withdraw.setText(
            formatters.format_currency(self.user['balance']))
        self.txt_withdraw_amount.setText('')

    def refresh_user(self) -> None:
        self.user = us.get_user_by_id(str(self.user['id']))
