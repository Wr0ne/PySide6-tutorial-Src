import sys,math   #Demo6_2.py
from PySide6.QtWidgets import QApplication,QWidget
from PySide6.QtGui import QPen,QPainter,QPixmap
from PySide6.QtCore import QPointF,Qt

class MyWindow(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.resize(600,500)
    def paintEvent(self,event):
        painter=QPainter(self)
        pix=QPixmap(r"d:\python\pic.jpg")  #图像
        pen=QPen(pix,40)   #含有背景图像的钢笔，线宽是40
        pen.setStyle(Qt.DashLine)
        pen.setJoinStyle(Qt.MiterJoin)
        painter.setPen(pen)  #设置钢笔

        p1 = QPointF(50,50)
        p2 = QPointF(self.width()-50,50)
        p3 = QPointF(50,self.height()-50)
        p4 = QPointF(self.width()-50,self.height()-50)
        painter.drawPolyline([p1,p2,p3,p4])  #绘制折线
if __name__ == '__main__':
    app=QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
