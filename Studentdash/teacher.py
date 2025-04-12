# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Teacher-Dashboard.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTextEdit,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(781, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 771, 91))
        self.frame.setStyleSheet(u"background-color: rgb(3, 1, 21);")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.USERNAME = QTextEdit(self.frame)
        self.USERNAME.setObjectName(u"USERNAME")
        self.USERNAME.setGeometry(QRect(110, 10, 181, 31))
        self.Institutename = QTextEdit(self.frame)
        self.Institutename.setObjectName(u"Institutename")
        self.Institutename.setGeometry(QRect(110, 40, 181, 31))
        self.Institutename.setOverwriteMode(False)
        self.Profileimage = QFrame(self.frame)
        self.Profileimage.setObjectName(u"Profileimage")
        self.Profileimage.setGeometry(QRect(20, 10, 81, 61))
        self.Profileimage.setFrameShape(QFrame.Shape.StyledPanel)
        self.Profileimage.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 90, 771, 451))
        self.frame_2.setStyleSheet(u"background-color: rgb(3, 1, 21);")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.Classroom1 = QPushButton(self.frame_2)
        self.Classroom1.setObjectName(u"Classroom1")
        self.Classroom1.setGeometry(QRect(20, 70, 351, 81))
        self.Classroom1.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(10, 0, 40);\n"
"font: italic 12pt \"Verdana\";")
        self.Classroom1.setAutoExclusive(False)
        self.CreateClaaroom = QPushButton(self.frame_2)
        self.CreateClaaroom.setObjectName(u"CreateClaaroom")
        self.CreateClaaroom.setGeometry(QRect(690, 10, 71, 31))
        self.CreateClaaroom.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(89, 243, 62);\n"
"font: italic 12pt \"Verdana\";")
        self.CreateClaaroom.setAutoExclusive(False)
        self.Classroom2 = QPushButton(self.frame_2)
        self.Classroom2.setObjectName(u"Classroom2")
        self.Classroom2.setGeometry(QRect(380, 70, 351, 81))
        self.Classroom2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(10, 0, 40);\n"
"font: italic 12pt \"Verdana\";")
        self.Classroom2.setAutoExclusive(False)
        self.Classroom3 = QPushButton(self.frame_2)
        self.Classroom3.setObjectName(u"Classroom3")
        self.Classroom3.setGeometry(QRect(20, 160, 351, 81))
        self.Classroom3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(10, 0, 40);\n"
"font: italic 12pt \"Verdana\";")
        self.Classroom3.setAutoExclusive(False)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 781, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.USERNAME.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-style:italic;\">USER NAME</span></p></body></html>", None))
        self.Institutename.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">@Institute name</span></p></body></html>", None))
        self.Classroom1.setText(QCoreApplication.translate("MainWindow", u"CLASS 1A", None))
        self.CreateClaaroom.setText(QCoreApplication.translate("MainWindow", u"NEW", None))
        self.Classroom2.setText(QCoreApplication.translate("MainWindow", u"CLASS 1A", None))
        self.Classroom3.setText(QCoreApplication.translate("MainWindow", u"CLASS 1A", None))
    # retranslateUi

