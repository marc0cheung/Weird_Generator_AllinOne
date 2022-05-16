# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'BallsBurgerGeneratorumdqSP.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(587, 608)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.result_textbox = QPlainTextEdit(self.centralwidget)
        self.result_textbox.setObjectName(u"result_textbox")
        self.result_textbox.setGeometry(QRect(20, 30, 321, 551))
        self.result_textbox.setLayoutDirection(Qt.LeftToRight)
        self.result_textbox.setAutoFillBackground(True)
        self.result_textbox.setBackgroundVisible(False)
        self.uwant_label = QLabel(self.centralwidget)
        self.uwant_label.setObjectName(u"uwant_label")
        self.uwant_label.setGeometry(QRect(360, 110, 221, 61))
        font = QFont()
        font.setPointSize(15)
        self.uwant_label.setFont(font)
        self.usee_label = QLabel(self.centralwidget)
        self.usee_label.setObjectName(u"usee_label")
        self.usee_label.setGeometry(QRect(360, 210, 221, 61))
        self.usee_label.setFont(font)
        self.verb_label = QLabel(self.centralwidget)
        self.verb_label.setObjectName(u"verb_label")
        self.verb_label.setGeometry(QRect(360, 320, 221, 61))
        self.verb_label.setFont(font)
        self.uwant_input = QPlainTextEdit(self.centralwidget)
        self.uwant_input.setObjectName(u"uwant_input")
        self.uwant_input.setGeometry(QRect(360, 160, 211, 51))
        font1 = QFont()
        font1.setPointSize(12)
        self.uwant_input.setFont(font1)
        self.usee_input = QPlainTextEdit(self.centralwidget)
        self.usee_input.setObjectName(u"usee_input")
        self.usee_input.setGeometry(QRect(360, 270, 211, 51))
        self.usee_input.setFont(font1)
        self.verb_input = QPlainTextEdit(self.centralwidget)
        self.verb_input.setObjectName(u"verb_input")
        self.verb_input.setGeometry(QRect(360, 380, 211, 51))
        self.verb_input.setFont(font1)
        self.generate_btn = QPushButton(self.centralwidget)
        self.generate_btn.setObjectName(u"generate_btn")
        self.generate_btn.setGeometry(QRect(360, 460, 211, 31))
        self.exit_btn = QPushButton(self.centralwidget)
        self.exit_btn.setObjectName(u"exit_btn")
        self.exit_btn.setGeometry(QRect(360, 500, 211, 31))
        self.about_btn = QPushButton(self.centralwidget)
        self.about_btn.setObjectName(u"about_btn")
        self.about_btn.setGeometry(QRect(360, 540, 211, 31))
        self.lang_label = QLabel(self.centralwidget)
        self.lang_label.setObjectName(u"lang_label")
        self.lang_label.setGeometry(QRect(360, 10, 221, 61))
        self.lang_label.setFont(font)
        self.zhHK_btn = QRadioButton(self.centralwidget)
        self.zhHK_btn.setObjectName(u"zhHK_btn")
        self.zhHK_btn.setGeometry(QRect(360, 60, 211, 19))
        self.zhCN_btn = QRadioButton(self.centralwidget)
        self.zhCN_btn.setObjectName(u"zhCN_btn")
        self.zhCN_btn.setEnabled(True)
        self.zhCN_btn.setGeometry(QRect(360, 90, 211, 19))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"BallsBurger Generator", None))
        self.result_textbox.setPlainText(QCoreApplication.translate("MainWindow", u"\u8fd9\u91cc\u4f1a\u51fa\u73b0\u751f\u6210\u51fa\u6765\u7684\u6587\u672c\u3002", None))
        self.uwant_label.setText(QCoreApplication.translate("MainWindow", u"\u60f3\u8981\u4ec0\u4e48\uff1f", None))
        self.usee_label.setText(QCoreApplication.translate("MainWindow", u"\u4f1a\u770b\u5230\u4ec0\u4e48\uff1f", None))
        self.verb_label.setText(QCoreApplication.translate("MainWindow", u"\u7ed9\u4e00\u4e2a\u5bf9\u5e94\u7684\u52a8\u8bcd\uff1a", None))
        self.generate_btn.setText(QCoreApplication.translate("MainWindow", u"\u751f\u6210", None))
        self.exit_btn.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa", None))
        self.about_btn.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
        self.lang_label.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u8bed\u8a00\uff1f", None))
        self.zhHK_btn.setText(QCoreApplication.translate("MainWindow", u"Traditional Chinese", None))
        self.zhCN_btn.setText(QCoreApplication.translate("MainWindow", u"Simplifiedl Chinese", None))
    # retranslateUi

