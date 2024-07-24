import sys  #Demo2_13.py
from PySide6.QtWidgets import (QApplication,QWidget,QTextEdit,QLabel,QScrollBar,QSlider,
                             QVBoxLayout,QHBoxLayout,QGroupBox,QGridLayout)
from PySide6.QtGui import QFont,QColor
from PySide6.QtCore import Qt

class MyWindow(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setWindowTitle("滑块例子")
        self.resize(500, 400)
        self.setupUi()  #调用函数，建立界面上的控件
        self.text_color()  #初始化文本输入框的文字颜色
        self.background_color()   #初始化文本输入框的文字背景色
        self.textEdit.append("北京诺思多维科技有限公司！")
    def setupUi(self):  #建立界面上的控件
        self.groupBox_1 = QGroupBox("设置字体颜色",self)  #容器控件
        self.groupBox_1.setMinimumWidth(200)
        self.label_r1 = QLabel("红：", self.groupBox_1)
        self.label_g1 = QLabel("绿：", self.groupBox_1)
        self.label_b1 = QLabel("蓝：", self.groupBox_1)
        self.scrollBar_r = QScrollBar(Qt.Horizontal,self.groupBox_1)
        self.scrollBar_r.setMinimumWidth(180)
        self.scrollBar_r.setRange(0,255)
        self.scrollBar_g = QScrollBar(Qt.Horizontal,self.groupBox_1)
        self.scrollBar_g.setRange(0, 255)
        self.scrollBar_b = QScrollBar(Qt.Horizontal,self.groupBox_1)
        self.scrollBar_b.setRange(0, 255)

        self.gridLayout_1 = QGridLayout(self.groupBox_1)  #格栅布局
        self.gridLayout_1.addWidget(self.label_r1,0,0)
        self.gridLayout_1.addWidget(self.scrollBar_r, 0, 1)
        self.gridLayout_1.addWidget(self.label_g1,1,0)
        self.gridLayout_1.addWidget(self.scrollBar_g, 1, 1)
        self.gridLayout_1.addWidget(self.label_b1,2,0)
        self.gridLayout_1.addWidget(self.scrollBar_b, 2, 1)

        self.groupBox_2 = QGroupBox("设置背景颜色",self)  #容器控件
        self.label_r2 = QLabel("红：", self.groupBox_2)
        self.label_g2 = QLabel("绿：", self.groupBox_2)
        self.label_b2 = QLabel("蓝：", self.groupBox_2)
        self.slider_r = QSlider(Qt.Horizontal,self.groupBox_1)
        self.slider_r.setRange(0,255)
        self.slider_r.setValue(200)
        self.slider_g = QSlider(Qt.Horizontal,self.groupBox_1)
        self.slider_g.setRange(0, 255)
        self.slider_g.setValue(200)
        self.slider_b = QSlider(Qt.Horizontal,self.groupBox_1)
        self.slider_b.setRange(0, 255)
        self.slider_b.setValue(200)

        self.gridLayout_2 = QGridLayout(self.groupBox_2)  #格栅布局
        self.gridLayout_2.addWidget(self.label_r2,0,0)
        self.gridLayout_2.addWidget(self.slider_r, 0, 1)
        self.gridLayout_2.addWidget(self.label_g2,1,0)
        self.gridLayout_2.addWidget(self.slider_g, 1, 1)
        self.gridLayout_2.addWidget(self.label_b2,2,0)
        self.gridLayout_2.addWidget(self.slider_b, 2, 1)

        self.hboxlayout = QHBoxLayout()   #水平布局
        self.hboxlayout.addWidget(self.groupBox_1)
        self.hboxlayout.addWidget(self.groupBox_2)

        font = QFont("黑体",pointSize=20)
        self.textEdit = QTextEdit("初始文字")
        self.textEdit.setFont(font)

        self.vboxlayout = QVBoxLayout(self)  #竖直布局
        self.vboxlayout.addLayout(self.hboxlayout)
        self.vboxlayout.addWidget(self.textEdit)

        self.scrollBar_r.valueChanged.connect(self.text_color)  #信号与槽的关联
        self.scrollBar_g.valueChanged.connect(self.text_color)  #信号与槽的关联
        self.scrollBar_b.valueChanged.connect(self.text_color)  #信号与槽的关联
        self.slider_r.valueChanged.connect(self.background_color)  #信号与槽的关联
        self.slider_g.valueChanged.connect(self.background_color)  #信号与槽的关联
        self.slider_b.valueChanged.connect(self.background_color)  #信号与槽的关联
    def text_color(self):  #文字颜色
        color = QColor(self.scrollBar_r.value(),self.scrollBar_g.value(),self.scrollBar_b.value())
        self.textEdit.setTextColor(color)  #设置文字颜色
    def background_color(self):  #文字背景色
        color = QColor(self.slider_r.value(),self.slider_g.value(),self.slider_b.value())
        self.textEdit.setTextBackgroundColor(color)  #设置文字背景颜色
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
