import sys  #Demo2_23.py
from PySide6.QtWidgets import QApplication,QWidget,QLabel,QHBoxLayout,QScrollArea
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

class MyWindow(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setupUi()
    def setupUi(self):  #建立界面上的控件
        self.scroArea = QScrollArea(self)
        label = QLabel(self.scroArea)
        pix = QPixmap("d:\\python\\pic.jpg")
        label.resize(pix.width(), pix.height())  #设置标签的宽度和高度
        label.setPixmap(pix)
        self.scroArea.setWidget(label)  #设置可滚动显示的控件
        self.scroArea.setAlignment(Qt.AlignCenter)  #设置对齐方式
        self.scroArea.ensureVisible(150,100)  #设置可见点
        self.scroArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded) #设置显示策略
        self.scroArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)  #设置显示策略

        self.h = QHBoxLayout(self)  #布局
        self.h.addWidget(self.scroArea)
if __name__ == '__main__':
    app=QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
