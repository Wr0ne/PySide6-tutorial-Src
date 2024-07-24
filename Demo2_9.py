import sys  #Demo2_9.py
from PySide6.QtWidgets import QApplication,QWidget,QLabel
from PySide6.QtGui import QPixmap,QFont
from PySide6.QtCore import QRect,Qt,QSize

class MyWidget(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setFixedSize(QSize(600,400))
        w = self.width()  #窗口的宽度
        h = self.height()  #窗口高度

        self.label1 = QLabel(self)
        self.label2 = QLabel(self)
        self.label3 = QLabel(self)
        self.label4 = QLabel(self)

        self.label1.setGeometry(QRect(0, 0, w,h))
        self.label1.setPixmap(QPixmap("d:\\python\\pic.png"))

        self.label2.setGeometry(QRect(int(w/2)-150,150,300,30))
        font = QFont("黑体",pointSize = 20)
        self.label2.setFont(font)
        self.label2.setText("<A href='http://www.mysmth.net/'>欢迎来到我的世界!</A>")
        self.label2.setToolTip("我喜欢的网站 www.mysmth.net")  #设置提示信息
        self.label2.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        self.label2.linkHovered.connect(self.hover)  #定义信号与槽的链接
        self.label2.linkActivated.connect(self.activated)  #定义信号与槽的链接

        self.label3.setGeometry(QRect(int(w/2),h-50,int(w/2),50))
        font = QFont("楷体",pointSize = 20)
        self.label3.setFont(font)
        self.label3.setText(">>进入我喜欢的<A href='http://www.mysmth.net/'>网站</A>")
        self.label3.setOpenExternalLinks(True)
    def hover(self,link):  #鼠标经过超链接的关联函数
        print("欢迎来到我的世界！")
    def activated(self,link):  #单击超链接的关联函数
        rect = self.label3.geometry()
        rect.setY(rect.y()-50)
        self.label4.setGeometry(rect)
        self.label4.setText("单击此链接，进入网站"+link)
if __name__ == '__main__':
    app=QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
