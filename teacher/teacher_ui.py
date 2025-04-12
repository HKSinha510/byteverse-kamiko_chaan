# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'teacher class.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLineEdit, QListView,
    QListWidget, QListWidgetItem, QMainWindow, QMenuBar,
    QPlainTextEdit, QPushButton, QScrollArea, QSizePolicy,
    QStackedWidget, QStatusBar, QTabWidget, QTextEdit,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.header = QFrame(self.centralwidget)
        self.header.setObjectName(u"header")
        self.header.setGeometry(QRect(0, 0, 781, 91))
        self.header.setStyleSheet(u"background-color: rgb(3, 1, 21);")
        self.header.setFrameShape(QFrame.Shape.StyledPanel)
        self.header.setFrameShadow(QFrame.Shadow.Raised)
        self.USERNAME = QTextEdit(self.header)
        self.USERNAME.setObjectName(u"USERNAME")
        self.USERNAME.setGeometry(QRect(110, 10, 181, 31))
        self.Institutename = QTextEdit(self.header)
        self.Institutename.setObjectName(u"Institutename")
        self.Institutename.setGeometry(QRect(110, 40, 181, 31))
        self.Institutename.setOverwriteMode(False)
        self.Profileimage = QFrame(self.header)
        self.Profileimage.setObjectName(u"Profileimage")
        self.Profileimage.setGeometry(QRect(20, 10, 81, 61))
        self.Profileimage.setFrameShape(QFrame.Shape.StyledPanel)
        self.Profileimage.setFrameShadow(QFrame.Shadow.Raised)
        self.textEdit = QTextEdit(self.header)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(540, 10, 231, 64))
        self.messagearea = QFrame(self.centralwidget)
        self.messagearea.setObjectName(u"messagearea")
        self.messagearea.setGeometry(QRect(0, 90, 561, 381))
        self.messagearea.setStyleSheet(u"border-color: rgb(8, 3, 59);\n"
"background-color: rgb(3, 1, 21);")
        self.messagearea.setFrameShape(QFrame.Shape.StyledPanel)
        self.messagearea.setFrameShadow(QFrame.Shadow.Raised)
        self.scrollArea = QScrollArea(self.messagearea)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(0, 0, 561, 381))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 559, 379))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.Messagebox = QFrame(self.centralwidget)
        self.Messagebox.setObjectName(u"Messagebox")
        self.Messagebox.setGeometry(QRect(0, 470, 561, 80))
        self.Messagebox.setStyleSheet(u"border-color: rgb(8, 3, 59);\n"
"background-color: rgb(3, 1, 21);")
        self.Messagebox.setFrameShape(QFrame.Shape.StyledPanel)
        self.Messagebox.setFrameShadow(QFrame.Shadow.Raised)
        self.messagebox = QLineEdit(self.Messagebox)
        self.messagebox.setObjectName(u"messagebox")
        self.messagebox.setGeometry(QRect(10, 10, 531, 51))
        self.Sendbutton = QPushButton(self.Messagebox)
        self.Sendbutton.setObjectName(u"Sendbutton")
        self.Sendbutton.setGeometry(QRect(460, 30, 75, 24))
        self.friendlist = QFrame(self.centralwidget)
        self.friendlist.setObjectName(u"friendlist")
        self.friendlist.setGeometry(QRect(560, 310, 221, 241))
        self.friendlist.setStyleSheet(u"border-color: rgb(8, 3, 59);\n"
"background-color: rgb(3, 1, 21);")
        self.friendlist.setFrameShape(QFrame.Shape.StyledPanel)
        self.friendlist.setFrameShadow(QFrame.Shadow.Raised)
        self.tabWidget = QTabWidget(self.friendlist)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 10, 221, 221))
        self.All = QWidget()
        self.All.setObjectName(u"All")
        self.listView_3 = QListView(self.All)
        self.listView_3.setObjectName(u"listView_3")
        self.listView_3.setGeometry(QRect(0, 0, 211, 201))
        self.tabWidget.addTab(self.All, "")
        self.Online = QWidget()
        self.Online.setObjectName(u"Online")
        self.listView_2 = QListView(self.Online)
        self.listView_2.setObjectName(u"listView_2")
        self.listView_2.setGeometry(QRect(0, 0, 211, 201))
        self.tabWidget.addTab(self.Online, "")
        self.Star = QWidget()
        self.Star.setObjectName(u"Star")
        self.listView = QListView(self.Star)
        self.listView.setObjectName(u"listView")
        self.listView.setGeometry(QRect(0, 1, 211, 201))
        self.tabWidget.addTab(self.Star, "")
        self.ToDo_nextclass = QFrame(self.centralwidget)
        self.ToDo_nextclass.setObjectName(u"ToDo_nextclass")
        self.ToDo_nextclass.setGeometry(QRect(560, 90, 221, 221))
        self.ToDo_nextclass.setStyleSheet(u"border-color: rgb(8, 3, 59);\n"
"background-color: rgb(3, 1, 21);")
        self.ToDo_nextclass.setFrameShape(QFrame.Shape.StyledPanel)
        self.ToDo_nextclass.setFrameShadow(QFrame.Shadow.Raised)
        self.stackedWidget = QStackedWidget(self.ToDo_nextclass)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(10, 10, 211, 201))
        self.stackedWidget.setStyleSheet(u"border-color: rgb(8, 3, 59);\n"
"background-color: rgb(3, 1, 21);")
        self.TODO = QWidget()
        self.TODO.setObjectName(u"TODO")
        self.List = QListView(self.TODO)
        self.List.setObjectName(u"List")
        self.List.setGeometry(QRect(-10, 20, 221, 191))
        self.Tabname = QPlainTextEdit(self.TODO)
        self.Tabname.setObjectName(u"Tabname")
        self.Tabname.setGeometry(QRect(0, 0, 181, 21))
        self.EnterTODO = QLineEdit(self.TODO)
        self.EnterTODO.setObjectName(u"EnterTODO")
        self.EnterTODO.setGeometry(QRect(0, 170, 211, 31))
        self.pushButton = QPushButton(self.TODO)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(130, 140, 75, 24))
        self.stackedWidget.addWidget(self.TODO)
        self.Nextclass = QWidget()
        self.Nextclass.setObjectName(u"Nextclass")
        self.listWidget = QListWidget(self.Nextclass)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(-10, 20, 221, 191))
        self.plainTextEdit = QPlainTextEdit(self.Nextclass)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(0, -10, 181, 31))
        self.EnterTODO_2 = QLineEdit(self.Nextclass)
        self.EnterTODO_2.setObjectName(u"EnterTODO_2")
        self.EnterTODO_2.setGeometry(QRect(0, 170, 211, 31))
        self.pushButton_2 = QPushButton(self.Nextclass)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(130, 140, 75, 24))
        self.stackedWidget.addWidget(self.Nextclass)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(1)


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
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">CLASS NAME</p>\n"
"<p align=\"right\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.Sendbutton.setText(QCoreApplication.translate("MainWindow", u"Send", None))
#if QT_CONFIG(whatsthis)
        self.friendlist.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>This is block to show friend list (all student in this class</p><p>It has 3 section</p><p>1. Online</p><p>2. Oflline</p><p>3. Star</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.All), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Online), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Star), QCoreApplication.translate("MainWindow", u"Page", None))
#if QT_CONFIG(whatsthis)
        self.ToDo_nextclass.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>This is ui bli in student classroom which show</p><p>1. ToDo list</p><p>     a. Done list button = submitted task in this class with date of submittion and status if teacher seen it or not</p><p>     b. Check list of pending task in this class with due dates</p><p>3.  Next Classes</p><p>     a. list Next lectures and their time with link to join</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.Tabname.setPlainText(QCoreApplication.translate("MainWindow", u"TODO list", None))
        self.EnterTODO.setText(QCoreApplication.translate("MainWindow", u"Create TODO", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Create", None))
        self.plainTextEdit.setPlainText(QCoreApplication.translate("MainWindow", u"NEXT CLASSES", None))
        self.EnterTODO_2.setText(QCoreApplication.translate("MainWindow", u"Create class", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Create", None))
    # retranslateUi

