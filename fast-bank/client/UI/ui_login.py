# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(280, 510)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Login.sizePolicy().hasHeightForWidth())
        Login.setSizePolicy(sizePolicy)
        Login.setMinimumSize(QSize(280, 510))
        Login.setMaximumSize(QSize(332, 510))
        Login.setStyleSheet(u"background-color: rgb(45, 70, 85);")
        self.logo = QLabel(Login)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(10, 10, 260, 91))
        self.logo.setPixmap(QPixmap(u"./assets/images/logo.png"))
        self.logo.setScaledContents(True)
        self.frame = QFrame(Login)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(20, 110, 241, 275))
        self.frame.setStyleSheet(u"background-color: rgba(0, 0, 0,0.2);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.txt_user = QLineEdit(self.frame)
        self.txt_user.setObjectName(u"txt_user")
        self.txt_user.setGeometry(QRect(20, 50, 201, 31))
        font = QFont()
        font.setPointSize(11)
        self.txt_user.setFont(font)
        self.txt_user.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.txt_user.setFrame(True)
        self.txt_user.setAlignment(Qt.AlignCenter)
        self.txt_pasword = QLineEdit(self.frame)
        self.txt_pasword.setObjectName(u"txt_pasword")
        self.txt_pasword.setGeometry(QRect(20, 120, 201, 31))
        self.txt_pasword.setFont(font)
        self.txt_pasword.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.txt_pasword.setEchoMode(QLineEdit.Password)
        self.txt_pasword.setAlignment(Qt.AlignCenter)
        self.txt_pasword.setClearButtonEnabled(False)
        self.btn_login = QPushButton(self.frame)
        self.btn_login.setObjectName(u"btn_login")
        self.btn_login.setGeometry(QRect(20, 195, 201, 31))
        self.btn_login.setFont(font)
        self.btn_login.setStyleSheet(u"QPushButton {\n"
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
        self.lbl_message = QLabel(self.frame)
        self.lbl_message.setObjectName(u"lbl_message")
        self.lbl_message.setGeometry(QRect(10, 13, 221, 20))
        self.lbl_message.setFont(font)
        self.lbl_message.setStyleSheet(u"color: rgb(255, 0, 0);\n"
"background-color: srgb(255, 255, 255, 0);")
        self.lbl_message.setAlignment(Qt.AlignCenter)
        self.label = QLabel(Login)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 430, 151, 41))
        self.label.setPixmap(QPixmap(u"./assets/images/logo_cesmac.png"))
        self.label.setScaledContents(True)
        QWidget.setTabOrder(self.btn_login, self.txt_user)
        QWidget.setTabOrder(self.txt_user, self.txt_pasword)

        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"Form", None))
        self.logo.setText("")
        self.txt_user.setPlaceholderText(QCoreApplication.translate("Login", u"Usu\u00e1rio", None))
        self.txt_pasword.setPlaceholderText(QCoreApplication.translate("Login", u"Senha", None))
        self.btn_login.setText(QCoreApplication.translate("Login", u"Entrar", None))
        self.lbl_message.setText("")
        self.label.setText("")
    # retranslateUi

