import sys,math   #Demo6_12.py
from PySide6.QtWidgets import QApplication,QWidget
from PySide6.QtGui import QPainter
from PySide6.QtCore import QPointF,QRect

class MyWindow(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.resize(600,500)
    def paintEvent(self,event):
        painter = QPainter(self)
        rect = QRect(int(self.width()/2)-200,int(self.height()/2)-100,400,200)
        painter.drawRect(rect)
        painter.setViewport(rect)
        painter.setWindow(-100,100,200,-200)
        r=100   #五角星的外接圆半径
        points = list()
        for i in range(5):
            x=r*math.cos((90+144*i)*math.pi/180)
            y=r*math.sin((90+144*i)*math.pi/180)
            points.append(QPointF(x,y))
        painter.drawPolygon(points)  #在视口中心绘制多边形

        painter.resetTransform() #重置变换
        painter.setViewport(0,0,self.width(),self.height()) #整个窗口是视口
        painter.setWindow(0,self.height(),self.width(),-self.height()) #窗口左下角为原点
        painter.drawPolygon(points)  # 在窗口左下角绘制多边形
if __name__ == '__main__':
    app=QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
