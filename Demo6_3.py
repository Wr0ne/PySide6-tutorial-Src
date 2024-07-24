import sys   #Demo6_3.py
from PySide6.QtWidgets import QApplication,QWidget
from PySide6.QtGui import QPen,QPainter,QBrush
from PySide6.QtCore import Qt,QPointF,QRectF

class MyWindow(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
    def paintEvent(self,event):
        painter=QPainter(self)
        pen=QPen()   #钢笔
        pen.setColor(Qt.blue)
        pen.setWidth(5)  #线条宽度
        painter.setPen(pen)  #设置钢笔

        brush=QBrush(Qt.red,Qt.DiagCrossPattern)  #画刷，同时设置颜色和风格
        painter.setBrush(brush)  #设置画刷
        p1=QPointF(self.width()/4,self.height()/4)
        p2=QPointF(3*self.width()/4,3*self.height()/4)
        painter.drawRect(QRectF(p1,p2))  #绘制矩形
if __name__ == '__main__':
    app=QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
