import sys   #Demo6_6.py
from PySide6.QtWidgets import QApplication,QWidget
from PySide6.QtGui import QPen,QPainter,QPainterPath,QBrush
from PySide6.QtCore import QPointF,Qt

class MyWindow(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.resize(600,500)
    def paintEvent(self,event):
        path = QPainterPath()  #路径
        self.center = QPointF(self.width() / 2, self.height() / 2)
        r = min(self.width(),self.height())/3  #外面大圆的半径
        r1 = r/7  #内部小圆的半径
        path.moveTo(self.center.x(), self.center.y() - r)
        path.arcTo(self.center.x() - r, self.center.y() - r, 2 * r, 2 * r, 90, 360)  #外部大圆
        path.arcTo(self.center.x() - r, self.center.y() - r, 2 * r, 2 * r, 90, -180)  #反向半圆

        path.moveTo(self.center.x(), self.center.y() + r)
        path.arcTo(self.center.x() - r / 2, self.center.y(), r, r, -90, 180)  #内部半圆
        path.arcTo(self.center.x()-r/2,self.center.y()-r/2-r/2,r,r,270,-180)  #内部半圆

        path.moveTo(self.center.x() + r1, self.center.y() - r / 2)
        path.arcTo(self.center.x()-r1,self.center.y()-r/2-r1,2*r1,2*r1,0,360)  #内部小圆
        path.moveTo(self.center.x() + r1, self.center.y() + r / 2)
        path.arcTo(self.center.x()-r1,self.center.y()+r/2-r1,2*r1,2*r1,0,-360)  #内部小圆

        path.setFillRule(Qt.WindingFill)  #填充方式

        painter=QPainter(self)
        pen=QPen()
        pen.setWidth(5)
        pen.setColor(Qt.black)
        painter.setPen(pen)

        brush=QBrush(Qt.SolidPattern)
        painter.setBrush(brush)  #设置画刷
        painter.drawPath(path)   #设置绘制路径
        super().paintEvent(event)
if __name__ == '__main__':
    app=QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
