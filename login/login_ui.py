from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(439, 533)
        Dialog.setStyleSheet(u"background-color:rgb(27, 27, 27)")
        self.email = QLabel(Dialog)
        self.email.setObjectName(u"email")
        self.email.setGeometry(QRect(40, 250, 81, 21))
        font = QFont()
        font.setFamilies([u"Terminal"])
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        self.email.setFont(font)
        self.email.setStyleSheet(u"font: 15pt \"Terminal\";")
        self.password = QLabel(Dialog)
        self.password.setObjectName(u"pass")
        self.password.setGeometry(QRect(40, 320, 101, 21))
        self.password.setFont(font)
        self.password.setStyleSheet(u"font: 15pt \"Terminal\";")
        self.email_input = QLineEdit(Dialog)
        self.email_input.setObjectName(u"email_input")
        self.email_input.setGeometry(QRect(162, 240, 241, 41))
        self.email_input.setStyleSheet(u"font: 12pt \"Terminal\";\n"
"background-color:rgb(52, 52, 52);\n"
"")
        self.password_input = QLineEdit(Dialog)
        self.password_input.setObjectName(u"pass_input")
        self.password_input.setGeometry(QRect(160, 310, 241, 41))
        self.password_input.setStyleSheet(u"font: 12pt \"Terminal\";\n"
"background-color:rgb(52, 52, 52);")
        self.loginbutton = QPushButton(Dialog)
        self.loginbutton.setObjectName(u"loginbutton")
        self.loginbutton.setGeometry(QRect(330, 470, 75, 24))
        self.loginbutton.setStyleSheet(u"font: 11pt \"Berlin Sans FB\";\n"
"alternate-background-color: rgb(157, 157, 157);\n"
"background-color: rgb(59, 59, 59);")
        self.login_label = QLabel(Dialog)
        self.login_label.setObjectName(u"login_label")
        self.login_label.setGeometry(QRect(100, 60, 251, 101))
        self.login_label.setTabletTracking(False)
        self.login_label.setStyleSheet(u"font: 22pt \"Bauhaus 93\";\n"
"background-color: rgb(61, 61, 61);\n"
"color: rgb(73, 236, 254);")
        self.email_input_2 = QLineEdit(Dialog)
        self.email_input_2.setObjectName(u"email_input_2")
        self.email_input_2.setGeometry(QRect(160, 380, 241, 41))
        self.email_input_2.setStyleSheet(u"font: 12pt \"Terminal\";\n"
"background-color:rgb(52, 52, 52);\n"
"")
        self.email_2 = QLabel(Dialog)
        self.email_2.setObjectName(u"email_2")
        self.email_2.setGeometry(QRect(38, 390, 101, 21))
        self.email_2.setFont(font)
        self.email_2.setStyleSheet(u"font: 15pt \"Terminal\";")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.email.setText(QCoreApplication.translate("Dialog", u"E-mail : ", None))
        self.password.setText(QCoreApplication.translate("Dialog", u"Password : ", None))
        self.loginbutton.setText(QCoreApplication.translate("Dialog", u"NEXT", None))
        self.login_label.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><h1 align=\"center\" style=\" margin-top:18px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:xx-large; font-weight:700;\">LOGIN</span></h1></body></html>", None))
        self.email_input_2.setText("")
        self.email_2.setText(QCoreApplication.translate("Dialog", u"Username : ", None))
    # retranslateUi

