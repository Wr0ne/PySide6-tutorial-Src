import sys  #Demo3_20.py
from PySide6.QtWidgets import  QApplication,QWidget,QVBoxLayout,QStyleFactory,\
                            QPushButton,QComboBox,QSpinBox
class MyWindow(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setupUi()
    def setupUi(self):
        v=QVBoxLayout(self)
        self.comb=QComboBox()
        self.spinBox=QSpinBox()
        self.pushButton=QPushButton("Close")
        v.addWidget(self.comb)
        v.addWidget(self.spinBox)
        v.addWidget(self.pushButton)
        self.comb.addItems(QStyleFactory.keys())  #将系统支持的风格名称添加到下拉列表中
        self.pushButton.clicked.connect(self.close)
class MyApplication(QApplication):
    def __init__(self,argv):
        super().__init__(argv)
        window=MyWindow()   #创建窗口
        style=QStyleFactory.create(window.comb.currentText())  #创建风格
        self.setStyle(style)  #设置初始风格
        window.comb.currentTextChanged.connect(self.reSetStyle)  #信号与槽的连接
        window.show()
        sys.exit(self.exec())
    def reSetStyle(self,new_style):  #槽函数
        style = QStyleFactory.create(new_style)  #创建新风格
        self.setStyle(style)   #设置新风格
        print("当前风格是:", new_style)  #输出当前的风格
if __name__ == '__main__':
    app = MyApplication(sys.argv)
