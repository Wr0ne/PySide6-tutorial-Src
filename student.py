# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'student.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
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
        Form.resize(453, 292)
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(30, 50, 191, 151))
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
        self.groupBox_2.setGeometry(QRect(240, 50, 191, 151))
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
        self.btnCalculate.setGeometry(QRect(150, 240, 75, 23))
        self.btnSave = QPushButton(Form)
        self.btnSave.setObjectName(u"btnSave")
        self.btnSave.setGeometry(QRect(260, 240, 75, 23))

        self.retranslateUi(Form)

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
    # retranslateUi

