from PySide2.QtWidgets import (QWidget)
from src.views.ui_login import Ui_Login
from src.services import login_service as ls

from src.controllers.main_window import MainWindow


class Login(QWidget, Ui_Login):

    user = {}

    def __init__(self) -> None:
        super(Login, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Banco Fast - Login')
        self.btn_login.clicked.connect(self.handle_login)

    def handle_login(self) -> None:

        login = ls.login(self.txt_user.text(), self.txt_pasword.text())

        if login['success']:
            self.user = login['user']
            self.lbl_message.setText('')
            self.run_app()
        else:
            self.lbl_message.setText('Falha na autenticação')
            self.clean_fields()

    def run_app(self) -> None:
        self.main_window = MainWindow(self.user)
        self.main_window.show()
        self.close()

    def clean_fields(self) -> None:
        self.txt_user.setText('')
        self.txt_pasword.setText('')
