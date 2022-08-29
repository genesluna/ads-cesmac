from PySide2.QtWidgets import QMainWindow, QMessageBox
from UI.ui_main_window import Ui_MainWindow
from services import users_service as us
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR')


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, user) -> None:
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Banco Fast')
        self.user = user
        self.lbl_greeting.setText(f'Olá, {user["name"]}')
        self.lbl_acount_balance.setText(
            str(locale.currency(self.user['balance'], grouping=True)))

        # Navigation events
        self.btn_home.clicked.connect(self.navigate_home)
        self.btn_deposit.clicked.connect(self.navigate_deposit)
        self.btn_withdraw.clicked.connect(self.navigate_withdraw)

        # Buttons events
        self.btn_deposit_amount.clicked.connect(self.handle_deposit)
        self.btn_withdraw_amount.clicked.connect(self.handle_withdraw)

    def navigate_home(self):
        self.refresh_user()
        self.lbl_acount_balance.setText(
            self.format_currency(self.user['balance']))
        self.Pages.setCurrentWidget(self.page_home)

    def navigate_deposit(self):
        self.refresh_user()
        self.lbl_acc_balance_deposit.setText(
            self.format_currency(self.user['balance']))
        self.Pages.setCurrentWidget(self.page_deposit)

    def navigate_withdraw(self):
        self.refresh_user()
        self.lbl_acc_balance_withdraw.setText(
            self.format_currency(self.user['balance']))
        self.Pages.setCurrentWidget(self.page_withdraw)

    def handle_deposit(self):
        amount = float(self.txt_deposit_amount.text())
        us.deposit(self.user['id'], amount)
        self.refresh_user()
        self.lbl_acc_balance_deposit.setText(
            self.format_currency(self.user['balance']))
        self.txt_deposit_amount.setText('')

    def handle_withdraw(self):
        amount = float(self.txt_withdraw_amount.text())

        if amount > self.user['balance']:
            self.show_alert(
                'Saldo infuficiente', 'O valor que você deseja sacar é maior que o saldo disponível.')
            self.txt_withdraw_amount.setText('')
            return None

        us.withdraw(self.user['id'], amount)
        self.refresh_user()
        self.lbl_acc_balance_withdraw.setText(
            self.format_currency(self.user['balance']))
        self.txt_withdraw_amount.setText('')

    def refresh_user(self):
        self.user = us.get_user_by_id(str(self.user['id']))

    def format_currency(self, value):
        return str(locale.currency(value, grouping=True))

    def show_alert(self, title, message):
        alert = QMessageBox()
        alert.setIcon(QMessageBox.Warning)
        alert.setWindowTitle(title)
        alert.setText(message)
        alert.exec_()
