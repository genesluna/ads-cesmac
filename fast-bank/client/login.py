from PySide2.QtWidgets import (QWidget)
from UI.ui_login import Ui_Login
from services import users_service as us
from services import login_service as ls

from main_window import MainWindow


class Login(QWidget, Ui_Login):
    def __init__(self) -> None:
        super(Login, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Banco Fast - Login')
        self.btn_login.clicked.connect(self.handle_login)

    def handle_login(self) -> None:

        if ls.login(self.txt_user.text(), self.txt_pasword.text()):
            self.lbl_message.setText('')
            self.run_app()
        else:
            self.lbl_message.setText('Falha na autenticação')
            self.clean_fields()

    def run_app(self) -> None:
        user = us.get_user(self.txt_user.text())
        self.main_window = MainWindow(user)
        self.main_window.show()
        self.close()

    def clean_fields(self) -> None:
        self.txt_user.setText('')
        self.txt_pasword.setText('')
