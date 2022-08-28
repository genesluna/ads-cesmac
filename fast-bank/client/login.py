from PySide2.QtWidgets import (QWidget)
from UI.ui_login import Ui_Login


class Login(QWidget, Ui_Login):
    def __init__(self) -> None:
        super(Login, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Banco Fast - Login')
        self.btn_login.clicked.connect(self.handle_login)

    def handle_login(self) -> None:
        if self.txt_user.text() != '' and self.txt_pasword.text() != '':
            print('OK')
            self.lbl_message.setText('')
        else:
            self.lbl_message.setText('Informações inválidas')
