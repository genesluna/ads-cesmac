# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'main_window.ui'
##
# Created by: Qt User Interface Compiler version 5.15.2
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(280, 510)
        MainWindow.setMinimumSize(QSize(280, 510))
        MainWindow.setMaximumSize(QSize(280, 510))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(45, 70, 85);")
        self.frm_header = QFrame(self.centralwidget)
        self.frm_header.setObjectName(u"frm_header")
        self.frm_header.setGeometry(QRect(9, 9, 263, 81))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.frm_header.sizePolicy().hasHeightForWidth())
        self.frm_header.setSizePolicy(sizePolicy)
        self.frm_header.setFrameShape(QFrame.StyledPanel)
        self.frm_header.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frm_header)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(3, -8, 260, 91))
        self.label.setPixmap(QPixmap(u"./assets/images/logo.png"))
        self.label.setScaledContents(True)
        self.frm_body = QFrame(self.centralwidget)
        self.frm_body.setObjectName(u"frm_body")
        self.frm_body.setGeometry(QRect(-10, 83, 301, 351))
        sizePolicy.setHeightForWidth(
            self.frm_body.sizePolicy().hasHeightForWidth())
        self.frm_body.setSizePolicy(sizePolicy)
        self.frm_body.setFrameShape(QFrame.NoFrame)
        self.frm_body.setFrameShadow(QFrame.Plain)
        self.verticalLayout = QVBoxLayout(self.frm_body)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Pages = QStackedWidget(self.frm_body)
        self.Pages.setObjectName(u"Pages")
        self.Pages.setStyleSheet(u"background-color: rgb(35, 54, 66);")
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.lbl_greeting = QLabel(self.page_home)
        self.lbl_greeting.setObjectName(u"lbl_greeting")
        self.lbl_greeting.setGeometry(QRect(20, 18, 241, 20))
        font = QFont()
        font.setPointSize(11)
        self.lbl_greeting.setFont(font)
        self.lbl_greeting.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lbl_greeting.setMargin(0)
        self.lbl_greeting.setIndent(-1)
        self.frame = QFrame(self.page_home)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(20, 60, 242, 80))
        self.frame.setStyleSheet(u"background-color: rgba(255, 233, 138, 0.6);\n"
                                 "border-radius: 10px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 15, 111, 16))
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(False)
        font1.setWeight(50)
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"background-color: rgba(255, 255, 255,0);")
        self.lbl_acount_balance = QLabel(self.frame)
        self.lbl_acount_balance.setObjectName(u"lbl_acount_balance")
        self.lbl_acount_balance.setGeometry(QRect(20, 40, 160, 30))
        font2 = QFont()
        font2.setPointSize(15)
        font2.setBold(False)
        font2.setWeight(50)
        self.lbl_acount_balance.setFont(font2)
        self.lbl_acount_balance.setStyleSheet(
            u"background-color: rgba(255, 255, 255,0);")
        self.frame_2 = QFrame(self.page_home)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(20, 150, 242, 80))
        self.frame_2.setStyleSheet(u"background-color: rgba(255, 233, 138, 0.6);\n"
                                   "border-radius: 10px;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 15, 111, 16))
        self.label_7.setFont(font1)
        self.label_7.setStyleSheet(u"background-color: rgba(255, 255, 255,0);")
        self.lbl_credit_balance = QLabel(self.frame_2)
        self.lbl_credit_balance.setObjectName(u"lbl_credit_balance")
        self.lbl_credit_balance.setGeometry(QRect(20, 40, 160, 30))
        self.lbl_credit_balance.setFont(font2)
        self.lbl_credit_balance.setStyleSheet(
            u"background-color: rgba(255, 255, 255,0);")
        self.frame_3 = QFrame(self.page_home)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(20, 240, 242, 80))
        self.frame_3.setStyleSheet(u"background-color: rgba(255, 233, 138, 0.6);\n"
                                   "border-radius: 10px;")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.label_9 = QLabel(self.frame_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(20, 15, 111, 16))
        self.label_9.setFont(font1)
        self.label_9.setStyleSheet(u"background-color: rgba(255, 255, 255,0);")
        self.lbl_investment_balance = QLabel(self.frame_3)
        self.lbl_investment_balance.setObjectName(u"lbl_investment_balance")
        self.lbl_investment_balance.setGeometry(QRect(20, 40, 160, 30))
        self.lbl_investment_balance.setFont(font2)
        self.lbl_investment_balance.setStyleSheet(
            u"background-color: rgba(255, 255, 255,0);")
        self.Pages.addWidget(self.page_home)
        self.page_deposit = QWidget()
        self.page_deposit.setObjectName(u"page_deposit")
        self.frame_4 = QFrame(self.page_deposit)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(20, 70, 242, 80))
        self.frame_4.setStyleSheet(u"background-color: rgba(255, 233, 138, 0.6);\n"
                                   "border-radius: 10px;")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.label_6 = QLabel(self.frame_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 15, 111, 16))
        self.label_6.setFont(font1)
        self.label_6.setStyleSheet(u"background-color: rgba(255, 255, 255,0);")
        self.lbl_acc_balance_deposit = QLabel(self.frame_4)
        self.lbl_acc_balance_deposit.setObjectName(u"lbl_acc_balance_deposit")
        self.lbl_acc_balance_deposit.setGeometry(QRect(20, 40, 160, 30))
        self.lbl_acc_balance_deposit.setFont(font2)
        self.lbl_acc_balance_deposit.setStyleSheet(
            u"background-color: rgba(255, 255, 255,0);")
        self.txt_deposit_amount = QLineEdit(self.page_deposit)
        self.txt_deposit_amount.setObjectName(u"txt_deposit_amount")
        self.txt_deposit_amount.setGeometry(QRect(20, 210, 241, 31))
        font3 = QFont()
        font3.setPointSize(10)
        self.txt_deposit_amount.setFont(font3)
        self.txt_deposit_amount.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                              "padding-left: 5 px;")
        self.label_2 = QLabel(self.page_deposit)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 184, 141, 16))
        self.label_2.setFont(font3)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.btn_deposit_amount = QPushButton(self.page_deposit)
        self.btn_deposit_amount.setObjectName(u"btn_deposit_amount")
        self.btn_deposit_amount.setGeometry(QRect(156, 270, 101, 31))
        self.btn_deposit_amount.setFont(font3)
        self.btn_deposit_amount.setStyleSheet(u"QPushButton {\n"
                                              "	background-color: rgb(63, 97, 118);\n"
                                              "	color: rgb(255, 255, 255);\n"
                                              "	border-radius: 10px;\n"
                                              "}\n"
                                              "\n"
                                              "QPushButton:hover {\n"
                                              "	background-color: rgb(255, 233, 138);\n"
                                              "	\n"
                                              "	color: rgb(45, 70, 85);\n"
                                              "}")
        self.label_12 = QLabel(self.page_deposit)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(20, 20, 251, 31))
        font4 = QFont()
        font4.setPointSize(16)
        self.label_12.setFont(font4)
        self.label_12.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_12.setAlignment(
            Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.Pages.addWidget(self.page_deposit)
        self.page_withdraw = QWidget()
        self.page_withdraw.setObjectName(u"page_withdraw")
        self.frame_5 = QFrame(self.page_withdraw)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(20, 70, 242, 80))
        self.frame_5.setStyleSheet(u"background-color: rgba(255, 233, 138, 0.6);\n"
                                   "border-radius: 10px;")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.label_11 = QLabel(self.frame_5)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(20, 15, 111, 16))
        self.label_11.setFont(font1)
        self.label_11.setStyleSheet(
            u"background-color: rgba(255, 255, 255,0);")
        self.lbl_acc_balance_withdraw = QLabel(self.frame_5)
        self.lbl_acc_balance_withdraw.setObjectName(
            u"lbl_acc_balance_withdraw")
        self.lbl_acc_balance_withdraw.setGeometry(QRect(20, 40, 160, 30))
        self.lbl_acc_balance_withdraw.setFont(font2)
        self.lbl_acc_balance_withdraw.setStyleSheet(
            u"background-color: rgba(255, 255, 255,0);")
        self.label_3 = QLabel(self.page_withdraw)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 184, 141, 16))
        self.label_3.setFont(font3)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.btn_withdraw_amount = QPushButton(self.page_withdraw)
        self.btn_withdraw_amount.setObjectName(u"btn_withdraw_amount")
        self.btn_withdraw_amount.setGeometry(QRect(156, 270, 101, 31))
        self.btn_withdraw_amount.setFont(font3)
        self.btn_withdraw_amount.setStyleSheet(u"QPushButton {\n"
                                               "	background-color: rgb(63, 97, 118);\n"
                                               "	color: rgb(255, 255, 255);\n"
                                               "	border-radius: 10px;\n"
                                               "}\n"
                                               "\n"
                                               "QPushButton:hover {\n"
                                               "	background-color: rgb(255, 233, 138);\n"
                                               "	\n"
                                               "	color: rgb(45, 70, 85);\n"
                                               "}")
        self.txt_withdraw_amount = QLineEdit(self.page_withdraw)
        self.txt_withdraw_amount.setObjectName(u"txt_withdraw_amount")
        self.txt_withdraw_amount.setGeometry(QRect(20, 210, 241, 31))
        self.txt_withdraw_amount.setFont(font3)
        self.txt_withdraw_amount.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                               "padding-left: 5 px;")
        self.label_4 = QLabel(self.page_withdraw)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 20, 251, 31))
        self.label_4.setFont(font4)
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_4.setAlignment(
            Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.Pages.addWidget(self.page_withdraw)

        self.verticalLayout.addWidget(self.Pages)

        self.frm_nav = QFrame(self.centralwidget)
        self.frm_nav.setObjectName(u"frm_nav")
        self.frm_nav.setGeometry(QRect(0, 435, 280, 80))
        sizePolicy.setHeightForWidth(
            self.frm_nav.sizePolicy().hasHeightForWidth())
        self.frm_nav.setSizePolicy(sizePolicy)
        self.frm_nav.setCursor(QCursor(Qt.ArrowCursor))
        self.frm_nav.setFrameShape(QFrame.NoFrame)
        self.frm_nav.setFrameShadow(QFrame.Plain)
        self.horizontalLayout = QHBoxLayout(self.frm_nav)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 0, 10, 17)
        self.btn_home = QPushButton(self.frm_nav)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setAutoFillBackground(False)
        self.btn_home.setStyleSheet(u"QPushButton {\n"
                                    "	border-radius: 10px;\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton:hover {\n"
                                    "	\n"
                                    "	background-color: rgb(63, 97, 118);\n"
                                    "}")
        icon = QIcon()
        icon.addFile(u"./assets/images/home.png",
                     QSize(), QIcon.Normal, QIcon.Off)
        self.btn_home.setIcon(icon)
        self.btn_home.setIconSize(QSize(48, 48))
        self.btn_home.setCheckable(False)
        self.btn_home.setAutoDefault(False)
        self.btn_home.setFlat(True)

        self.horizontalLayout.addWidget(self.btn_home)

        self.btn_deposit = QPushButton(self.frm_nav)
        self.btn_deposit.setObjectName(u"btn_deposit")
        self.btn_deposit.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_deposit.setStyleSheet(u"QPushButton {\n"
                                       "	border-radius: 10px;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:hover {\n"
                                       "	\n"
                                       "	background-color: rgb(63, 97, 118);\n"
                                       "}")
        icon1 = QIcon()
        icon1.addFile(u"./assets/images/deposit.png",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.btn_deposit.setIcon(icon1)
        self.btn_deposit.setIconSize(QSize(48, 48))
        self.btn_deposit.setAutoDefault(False)
        self.btn_deposit.setFlat(True)

        self.horizontalLayout.addWidget(self.btn_deposit)

        self.btn_withdraw = QPushButton(self.frm_nav)
        self.btn_withdraw.setObjectName(u"btn_withdraw")
        self.btn_withdraw.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_withdraw.setStyleSheet(u"QPushButton {\n"
                                        "	border-radius: 10px;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "	\n"
                                        "	background-color: rgb(63, 97, 118);\n"
                                        "}")
        icon2 = QIcon()
        icon2.addFile(u"./assets/images/withdraw.png",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.btn_withdraw.setIcon(icon2)
        self.btn_withdraw.setIconSize(QSize(48, 48))
        self.btn_withdraw.setAutoDefault(False)
        self.btn_withdraw.setFlat(True)

        self.horizontalLayout.addWidget(self.btn_withdraw)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.Pages.setCurrentIndex(0)
        self.btn_home.setDefault(False)
        self.btn_deposit.setDefault(False)
        self.btn_withdraw.setDefault(False)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate(
            "MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.lbl_greeting.setText(QCoreApplication.translate(
            "MainWindow", u"Ol\u00e1, Tacyana", None))
        self.label_5.setText(QCoreApplication.translate(
            "MainWindow", u"Conta Corrente", None))
        self.lbl_acount_balance.setText(
            QCoreApplication.translate("MainWindow", u"R$ 1.350,00", None))
        self.label_7.setText(QCoreApplication.translate(
            "MainWindow", u"Cart\u00e3o de cr\u00e9dito", None))
        self.lbl_credit_balance.setText(
            QCoreApplication.translate("MainWindow", u"R$ 0,00", None))
        self.label_9.setText(QCoreApplication.translate(
            "MainWindow", u"Investimentos", None))
        self.lbl_investment_balance.setText(
            QCoreApplication.translate("MainWindow", u"R$ 0,00", None))
        self.label_6.setText(QCoreApplication.translate(
            "MainWindow", u"Saldo dispon\u00edvel", None))
        self.lbl_acc_balance_deposit.setText(
            QCoreApplication.translate("MainWindow", u"R$ 1.350,00", None))
        self.txt_deposit_amount.setText("")
        self.label_2.setText(QCoreApplication.translate(
            "MainWindow", u"Valor a depositar", None))
        self.btn_deposit_amount.setText(
            QCoreApplication.translate("MainWindow", u"Depositar", None))
        self.label_12.setText(QCoreApplication.translate(
            "MainWindow", u"Dep\u00f3sito", None))
        self.label_11.setText(QCoreApplication.translate(
            "MainWindow", u"Saldo dispon\u00edvel", None))
        self.lbl_acc_balance_withdraw.setText(
            QCoreApplication.translate("MainWindow", u"R$ 1.350,00", None))
        self.label_3.setText(QCoreApplication.translate(
            "MainWindow", u"Valor a sacar", None))
        self.btn_withdraw_amount.setText(
            QCoreApplication.translate("MainWindow", u"Sacar", None))
        self.label_4.setText(QCoreApplication.translate(
            "MainWindow", u"Saque", None))
# if QT_CONFIG(tooltip)
        self.btn_home.setToolTip("")
#endif // QT_CONFIG(tooltip)
# if QT_CONFIG(whatsthis)
        self.btn_home.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.btn_home.setText("")
        self.btn_deposit.setText("")
        self.btn_withdraw.setText("")
    # retranslateUi
