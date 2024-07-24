import sys,math   #Demo6_1.py
from PySide6.QtWidgets import QApplication,QWidget
from PySide6.QtGui import QPen,QPainter
from PySide6.QtCore import QPointF
from math import cos,sin,pi
class MyWindow(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.resize(600,500)
        self.painter= QPainter()
    def paintEvent(self,event):
        if self.painter.begin(self):
            font=self.painter.font()
            font.setPixelSize(20)
            self.painter.setFont(font)  #设置字体

            pen=QPen()   #钢笔
            pen.setWidth(5)  #线条宽度
            self.painter.setPen(pen)  #设置钢笔
            r=100   #五角星的外接圆半径
            x=self.width()/2
            y=self.height()/2
            p1=QPointF(r* cos(-90* pi/180)+x, r* sin(-90* pi/180)+y)
            p2=QPointF(r* cos(-18* pi/180)+x,r* sin(-18* pi/180)+y)
            p3=QPointF(r* cos(54* pi/180)+x,r* sin(54* pi/180)+y)
            p4=QPointF(r* cos(126* pi/180)+x,r* sin(126* pi/180)+y)
            p5=QPointF(r* cos(198* pi/180)+x,r* sin(198* pi/180)+y)

            self.painter.drawPolyline([p1,p3,p5,p2,p4,p1])  #绘制折线
            self.painter.drawText(p1,"  p1")  #绘制文字
            self.painter.drawText(p2, "  p2")
            self.painter.drawText(p3, "  p3")
            self.painter.drawText(p4, "  p4")
            self.painter.drawText(p5, "  p5")
            if self.painter.isActive():
                self.painter.end()
if __name__ == '__main__':
    app=QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
