from PySide2.QtWidgets import QMessageBox


def show_alert(title, message):
    alert = QMessageBox()
    alert.setIcon(QMessageBox.Warning)
    alert.setWindowTitle(title)
    alert.setText(message)
    alert.exec_()
