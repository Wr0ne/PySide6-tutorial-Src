import sys   #Demo6_5.py
from PySide6.QtWidgets import QApplication,QWidget
from PySide6.QtGui import QPen,QPainter,QBrush
from PySide6.QtCore import QPointF,Qt
from math import cos,sin,pi
class MyWindow(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.resize(600,500)
    def paintEvent(self,event):
        painter = QPainter(self)
        pen = QPen()   #钢笔
        pen.setWidth(2)  #线条宽度
        painter.setPen(pen)  #设置钢笔
        bush = QBrush(Qt.SolidPattern)
        painter.setBrush(bush)
        r=100   #五角星的外接圆半径
        x=self.width()/4
        y=self.height()/2
        p1=QPointF(r* cos(-90*pi/180)+x,r*sin(-90*pi/180)+y)
        p2=QPointF(r*cos(-18*pi/180)+x,r*sin(-18*pi/180)+y)
        p3=QPointF(r*cos(54*pi/180)+x,r*sin(54*pi/180)+y)
        p4=QPointF(r*cos(126*pi/180)+x,r*sin(126*pi/180)+y)
        p5=QPointF(r*cos(198*pi/180)+x,r*sin(198*pi/180)+y)

        painter.drawPolygon([p1,p3,p5,p2,p4],Qt.OddEvenFill)  #绘制多边形
        offset = QPointF(self.width()/2,0)
        painter.drawPolygon([p1+offset,p3+offset,p5+offset,p2+offset,p4+offset],Qt.WindingFill)
if __name__ == '__main__':
    app=QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
