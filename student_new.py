# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'student_new.ui'
##
## Created by: Qt User Interface Compiler version 6.1.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(455, 261)
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(40, 80, 191, 141))
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 30, 54, 16))
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 70, 54, 16))
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 110, 54, 16))
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.chinese = QSpinBox(self.groupBox)
        self.chinese.setObjectName(u"chinese")
        self.chinese.setGeometry(QRect(80, 30, 91, 22))
        self.math = QSpinBox(self.groupBox)
        self.math.setObjectName(u"math")
        self.math.setGeometry(QRect(80, 70, 91, 22))
        self.english = QSpinBox(self.groupBox)
        self.english.setObjectName(u"english")
        self.english.setGeometry(QRect(80, 110, 91, 22))
        self.groupBox_2 = QGroupBox(Form)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(250, 80, 191, 141))
        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 50, 54, 16))
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 90, 54, 16))
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.total = QLineEdit(self.groupBox_2)
        self.total.setObjectName(u"total")
        self.total.setGeometry(QRect(70, 50, 91, 20))
        self.total.setReadOnly(True)
        self.average = QLineEdit(self.groupBox_2)
        self.average.setObjectName(u"average")
        self.average.setGeometry(QRect(70, 90, 91, 20))
        self.average.setReadOnly(True)
        self.btnCalculate = QPushButton(Form)
        self.btnCalculate.setObjectName(u"btnCalculate")
        self.btnCalculate.setGeometry(QRect(80, 230, 75, 23))
        self.btnSave = QPushButton(Form)
        self.btnSave.setObjectName(u"btnSave")
        self.btnSave.setGeometry(QRect(200, 230, 75, 23))
        self.btnClose = QPushButton(Form)
        self.btnClose.setObjectName(u"btnClose")
        self.btnClose.setGeometry(QRect(310, 230, 75, 24))
        self.groupBox_3 = QGroupBox(Form)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(40, 10, 401, 61))
        self.label_6 = QLabel(self.groupBox_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 30, 55, 16))
        self.label_7 = QLabel(self.groupBox_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(220, 30, 31, 16))
        self.name = QLineEdit(self.groupBox_3)
        self.name.setObjectName(u"name")
        self.name.setGeometry(QRect(60, 30, 131, 22))
        self.number = QSpinBox(self.groupBox_3)
        self.number.setObjectName(u"number")
        self.number.setGeometry(QRect(260, 30, 131, 21))
        self.number.setMaximum(1000)

        self.retranslateUi(Form)
        self.btnClose.clicked.connect(Form.close)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u5b66\u751f\u6210\u7ee9", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u8bed  \u6587", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u6570  \u5b66", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u82f1  \u8bed", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"\u6210\u7ee9\u7edf\u8ba1", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u603b\u6210\u7ee9", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u5e73\u5747\u5206", None))
        self.btnCalculate.setText(QCoreApplication.translate("Form", u" \u8ba1   \u7b97", None))
        self.btnSave.setText(QCoreApplication.translate("Form", u"\u4fdd   \u5b58", None))
        self.btnClose.setText(QCoreApplication.translate("Form", u"\u5173 \u95ed", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Form", u"\u5b66\u751f\u57fa\u672c\u4fe1\u606f", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u59d3\u540d", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"\u5b66\u53f7", None))
    # retranslateUi

