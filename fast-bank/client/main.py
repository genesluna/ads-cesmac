from PySide2.QtWidgets import (QApplication)
from login import Login
import sys


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    app.exec_()
