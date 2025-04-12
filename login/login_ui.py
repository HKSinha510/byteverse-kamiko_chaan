# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'log_in2.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QPushButton, QSizePolicy,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(446, 539)
        Dialog.setStyleSheet(u"background-color:rgb(27, 27, 27)")
        self.password = QLabel(Dialog)
        self.password.setObjectName(u"password")
        self.password.setGeometry(QRect(40, 340, 101, 21))
        font = QFont()
        font.setFamilies([u"Terminal"])
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        self.password.setFont(font)
        self.password.setStyleSheet(u"font: 15pt \"Terminal\";")
        self.password_input = QLineEdit(Dialog)
        self.password_input.setObjectName(u"password_input")
        self.password_input.setGeometry(QRect(160, 330, 241, 41))
        self.password_input.setStyleSheet(u"font: 12pt \"Terminal\";\n"
"background-color:rgb(52, 52, 52);")
        self.login_label = QLabel(Dialog)
        self.login_label.setObjectName(u"login_label")
        self.login_label.setGeometry(QRect(100, 60, 251, 101))
        self.login_label.setTabletTracking(False)
        self.login_label.setStyleSheet(u"font: 22pt \"Bauhaus 93\";\n"
"background-color: rgb(61, 61, 61);\n"
"color: rgb(73, 236, 254);")
        self.user_input = QLineEdit(Dialog)
        self.user_input.setObjectName(u"user_input")
        self.user_input.setGeometry(QRect(160, 240, 241, 41))
        self.user_input.setStyleSheet(u"font: 12pt \"Terminal\";\n"
"background-color:rgb(52, 52, 52);\n"
"")
        self.user = QLabel(Dialog)
        self.user.setObjectName(u"user")
        self.user.setGeometry(QRect(38, 250, 101, 21))
        self.user.setFont(font)
        self.user.setStyleSheet(u"font: 15pt \"Terminal\";")
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 440, 390, 71))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(190)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SizeConstraint.SetNoConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.register_2 = QPushButton(self.widget)
        self.register_2.setObjectName(u"register_2")
        self.register_2.setEnabled(False)
        self.register_2.setStyleSheet(u"font: 11pt \"Berlin Sans FB\";\n"
"alternate-background-color: rgb(157, 157, 157);\n"
"background-color: rgb(59, 59, 59);")

        self.horizontalLayout.addWidget(self.register_2)

        self.login_next = QPushButton(self.widget)
        self.login_next.setObjectName(u"login_next")
        self.login_next.setMaximumSize(QSize(16777215, 27))
        self.login_next.setStyleSheet(u"font: 11pt \"Berlin Sans FB\";\n"
"alternate-background-color: rgb(157, 157, 157);\n"
"background-color: rgb(59, 59, 59);")

        self.horizontalLayout.addWidget(self.login_next)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.password.setText(QCoreApplication.translate("Dialog", u"Password : ", None))
        self.password_input.setPlaceholderText(QCoreApplication.translate("Dialog", u"password", None))
        self.login_label.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><h1 align=\"center\" style=\" margin-top:18px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:xx-large; font-weight:700;\">LOGIN</span></h1></body></html>", None))
        self.user_input.setText("")
        self.user_input.setPlaceholderText(QCoreApplication.translate("Dialog", u"username", None))
        self.user.setText(QCoreApplication.translate("Dialog", u"Username : ", None))
        self.register_2.setText(QCoreApplication.translate("Dialog", u"Register", None))
        self.login_next.setText(QCoreApplication.translate("Dialog", u"Next", None))
    # retranslateUi

