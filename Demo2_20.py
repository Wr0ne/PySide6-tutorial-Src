import sys  #Demo2_20.py
from PySide6.QtWidgets import  (QApplication,QWidget,QPushButton,QLineEdit,QGridLayout,QMessageBox)
from math import *

class myWindow(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setWindowTitle("格栅布局")
        self. resize(300,200)
        self.setupUI()  #调用函数，建立界面控件
    def setupUI(self):  #建立界面
        self.gridLayout = QGridLayout(self)  #格栅布局
        self.lineText = QLineEdit()
        self.gridLayout.addWidget(self.lineText,0,0,1,6)
        self.number_7 = QPushButton("7")
        self.gridLayout.addWidget(self.number_7, 1, 0)
        self.number_8 = QPushButton("8")
        self.gridLayout.addWidget(self.number_8, 1, 1)
        self.number_9 = QPushButton("9")
        self.gridLayout.addWidget(self.number_9, 1, 2)
        self.number_4 = QPushButton("4")
        self.gridLayout.addWidget(self.number_4, 2, 0)
        self.number_5 = QPushButton("5")
        self.gridLayout.addWidget(self.number_5, 2, 1)
        self.number_6 = QPushButton("6")
        self.gridLayout.addWidget(self.number_6, 2, 2)
        self.number_1 = QPushButton("1")
        self.gridLayout.addWidget(self.number_1, 3, 0)
        self.number_2 = QPushButton("2")
        self.gridLayout.addWidget(self.number_2, 3, 1)
        self.number_3 = QPushButton("3")
        self.gridLayout.addWidget(self.number_3, 3, 2)
        self.number_0 = QPushButton("0")
        self.gridLayout.addWidget(self.number_0, 4, 0,1,2)
        self.point = QPushButton(".")
        self.gridLayout.addWidget(self.point, 4, 2)

        self.plus = QPushButton("+")
        self.gridLayout.addWidget(self.plus, 1, 3)
        self.minus = QPushButton("-")
        self.gridLayout.addWidget(self.minus, 1, 4)
        self.multiple = QPushButton("*")
        self.gridLayout.addWidget(self.multiple, 2, 3)
        self.division = QPushButton("/")
        self.gridLayout.addWidget(self.division, 2, 4)

        self.sin = QPushButton("sin(x)")
        self.gridLayout.addWidget(self.sin, 3, 3)
        self.cos = QPushButton("cos(x)")
        self.gridLayout.addWidget(self.cos, 3, 4)
        self.power = QPushButton("幂(**)")
        self.gridLayout.addWidget(self.power, 4, 3)
        self.log = QPushButton("log10(x)")
        self.gridLayout.addWidget(self.log, 4, 4)
        self.bracket = QPushButton("()")
        self.gridLayout.addWidget(self.bracket, 1, 5)
        self.yushu = QPushButton("余数")
        self.gridLayout.addWidget(self.yushu, 2, 5)
        self.clear = QPushButton("清空")
        self.gridLayout.addWidget(self.clear, 3, 5)
        self.equal = QPushButton("=")
        self.gridLayout.addWidget(self.equal, 4, 5)
        self.number_0.clicked.connect(self.number_0_clicked) #以下是按钮信号与槽函数连接
        self.number_1.clicked.connect(self.number_1_clicked) #信号与槽函数连接
        self.number_2.clicked.connect(self.number_2_clicked) #信号与槽函数连接
        self.number_3.clicked.connect(self.number_3_clicked) #信号与槽函数连接
        self.number_4.clicked.connect(self.number_4_clicked) #信号与槽函数连接
        self.number_5.clicked.connect(self.number_5_clicked) #信号与槽函数连接
        self.number_6.clicked.connect(self.number_6_clicked) #信号与槽函数连接
        self.number_7.clicked.connect(self.number_7_clicked) #信号与槽函数连接
        self.number_8.clicked.connect(self.number_8_clicked) #信号与槽函数连接
        self.number_9.clicked.connect(self.number_9_clicked) #信号与槽函数连接
        self.point.clicked.connect(self.point_clicked) 
        self.plus.clicked.connect(self.plus_clicked)
        self.minus.clicked.connect(self.minus_clicked)
        self.multiple.clicked.connect(self.multiple_clicked)
        self.division.clicked.connect(self.division_clicked)
        self.sin.clicked.connect(self.sin_clicked)
        self.cos.clicked.connect(self.cos_clicked)
        self.power.clicked.connect(self.power_clicked)
        self.log.clicked.connect(self.log10_clicked)
        self.bracket.clicked.connect(self.bracket_clicked)
        self.yushu.clicked.connect(self.yushu_clikced)
        self.clear.clicked.connect(self.lineText.clear)
        self.equal.clicked.connect(self.equal_clicked)
    def number_0_clicked(self):  #以下是各个按钮的槽函数
        self.lineText.insert("0")
    def number_1_clicked(self):
        self.lineText.insert("1")
    def number_2_clicked(self):
        self.lineText.insert("2")
    def number_3_clicked(self):
        self.lineText.insert("3")
    def number_4_clicked(self):
        self.lineText.insert("4")
    def number_5_clicked(self):
        self.lineText.insert("5")
    def number_6_clicked(self):
        self.lineText.insert("6")
    def number_7_clicked(self):
        self.lineText.insert("7")
    def number_8_clicked(self):
        self.lineText.insert("8")
    def number_9_clicked(self):
        self.lineText.insert("9")
    def point_clicked(self):
        self.lineText.insert(".")
    def plus_clicked(self):
        self.lineText.insert("+")
    def minus_clicked(self):
        self.lineText.insert("-")
    def multiple_clicked(self):
        self.lineText.insert("*")
    def division_clicked(self):
        self.lineText.insert("/")
    def sin_clicked(self):
        self.lineText.insert("sin()")
        self.lineText.setFocus()
        self.lineText.cursorBackward(False, 1)
    def cos_clicked(self):
        self.lineText.insert("cos()")
        self.lineText.setFocus()
        self.lineText.cursorBackward(False, 1)
    def power_clicked(self):
        self.lineText.insert("**")
    def log10_clicked(self):
        self.lineText.insert("log10()")
        self.lineText.setFocus()
        self.lineText.cursorBackward(False, 1)
    def bracket_clicked(self):
        self.lineText.insert("()")
        self.lineText.setFocus()
        self.lineText.cursorBackward(False, 1)
    def yushu_clikced(self):
        self.lineText.insert("%")
    def equal_clicked(self):  #“=”按钮的槽函数
        try:
            value = eval(self.lineText.text())
            self.lineText.setText(self.lineText.text()+" = "+str(value))
        except:
            QMessageBox.information(self,"警告信息","输入的式子语法有问题，请检查")
if __name__ == '__main__':
    app=QApplication(sys.argv)
    window = myWindow()
    window.show()
    sys.exit(app.exec())
