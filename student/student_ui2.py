# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'student class.ui'
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
from PySide6.QtWidgets import (QApplication,QCheckBox, QFrame, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QMenuBar, QPushButton,
    QScrollArea, QScrollBar, QSizePolicy, QStackedWidget,
    QStatusBar, QTabWidget, QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")

        #FRAME 1
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
        self.Class_info = QTextEdit(self.header)
        self.Class_info.setObjectName(u"Class_info")
        self.Class_info.setGeometry(QRect(540, 10, 231, 64))

        ##FRAME 2
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
        self.verticalScrollBar = QScrollBar(self.scrollAreaWidgetContents)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setGeometry(QRect(540, 0, 16, 371))
        self.verticalScrollBar.setOrientation(Qt.Orientation.Vertical)
        self.messagedisplay = QListWidget(self.scrollAreaWidgetContents)
        self.messagedisplay.setObjectName(u"messagedisplay")
        self.messagedisplay.setGeometry(QRect(0, 0, 541, 371))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        #FRAME 3
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

        #FRAME 4(a)
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
        self.tabWidget.setStyleSheet(u"")
        self.All = QWidget()
        self.All.setObjectName(u"All")
        self.All_display = QListWidget(self.All)
        self.All_display.setObjectName(u"All_display")
        self.All_display.setGeometry(QRect(0, 0, 221, 191))
        self.All_display.addItem("Alice")
        self.All_display.addItem("Charlie")
        self.All_display.addItem("BOB")
        self.All_display.addItem("Max")
        self.All_display.addItem("Mandy")
        self.tabWidget.addTab(self.All, "")

        #FRAME 4(b)
        self.Online = QWidget()
        self.Online.setObjectName(u"Online")
        self.Online_display = QListWidget(self.Online)
        self.Online_display.setObjectName(u"Online_display")
        self.Online_display.setGeometry(QRect(0, 0, 221, 191))
        self.Online_display.addItem("Alice")
        self.Online_display.addItem("Charlie")
        self.tabWidget.addTab(self.Online, "")

        #FRAME 4(c)
        self.Star = QWidget()
        self.Star.setObjectName(u"Star")
        self.star_display = QListWidget(self.Star)
        self.star_display.setObjectName(u"star_display")
        self.star_display.setGeometry(QRect(0, 0, 221, 191))
        self.star_display.addItem("BOB")
        self.star_display.addItem("Max")
        self.star_display.addItem("Mandy")
        self.tabWidget.addTab(self.Star, "")

        #FRAME 5
        self.ToDo_nextclass = QFrame(self.centralwidget)
        self.ToDo_nextclass.setObjectName(u"ToDo_nextclass")
        self.ToDo_nextclass.setGeometry(QRect(560, 90, 221, 221))
        self.ToDo_nextclass.setStyleSheet(u"border-color: rgb(8, 3, 59);\n"
"background-color: rgb(3, 1, 21);")
        self.ToDo_nextclass.setFrameShape(QFrame.Shape.StyledPanel)
        self.ToDo_nextclass.setFrameShadow(QFrame.Shadow.Raised)
        self.stackedWidget = QStackedWidget(self.ToDo_nextclass)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 10, 211, 201))
        self.stackedWidget.setStyleSheet(u"border-color: rgb(8, 3, 59);\n"
"background-color: rgb(3, 1, 21);")
        
        #FRAME 5(a)
        self.TODO = QWidget()
        self.TODO.setObjectName(u"TODO")
        self.textEdit_3 = QTextEdit(self.TODO)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setGeometry(QRect(0, 0, 181, 21))
        self.listWidget_2 = QListWidget(self.TODO)
        self.listWidget_2.setObjectName(u"listWidget_2")
        self.listWidget_2.setGeometry(QRect(-10, 20, 221, 192))
        # Add 3 todo items to the list - need to add functionaliuities
        self.listWidget_2.addItem("1. Complete Assignment 3")
        self.listWidget_2.addItem("2. Revise Chapter 4 for Math")
        self.listWidget_2.addItem("3. Upload Lab Report")
        self.stackedWidget.addWidget(self.TODO)

        #FRAME 5(b)
        self.Nextclass = QWidget()
        self.Nextclass.setObjectName(u"Nextclass")
        self.nextclass_title = QTextEdit(self.Nextclass)
        self.nextclass_title.setObjectName(u"nextclass_title")
        self.nextclass_title.setGeometry(QRect(0, 0, 181, 21))
        self.nextclass_listview = QListWidget(self.Nextclass)
        self.nextclass_listview.setObjectName(u"nextclass_listview")
        self.nextclass_listview.setGeometry(QRect(0, 20, 211, 191))
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
        self.stackedWidget.setCurrentIndex(0)


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
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-style:italic;\">STUDENT NAME</span></p></body></html>", None))
        self.Institutename.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">@Institute name</span></p></body></html>", None))
        self.Class_info.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">CLASS NAME</p>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">@Teacher name</p></body></html>", None))
        self.Sendbutton.setText(QCoreApplication.translate("MainWindow", u"Send", None))
#if QT_CONFIG(whatsthis)
        self.friendlist.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>This is block to show friend list (all student in this class</p><p>It has 3 section</p><p>1. Online</p><p>2. Oflline</p><p>3. Star</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(whatsthis)
        self.tabWidget.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Online</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.All), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Online), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Star), QCoreApplication.translate("MainWindow", u"Page", None))
#if QT_CONFIG(whatsthis)
        self.ToDo_nextclass.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>This is ui bli in student classroom which show</p><p>1. ToDo list</p><p>     a. Done list button = submitted task in this class with date of submittion and status if teacher seen it or not</p><p>     b. Check list of pending task in this class with due dates</p><p>3.  Next Classes</p><p>     a. list Next lectures and their time with link to join</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.textEdit_3.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">TODO list</p></body></html>", None))
        self.nextclass_title.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">NEXT CLASS</p></body></html>", None))
    # retranslateUi

