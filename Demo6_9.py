import sys,os   #Demo6_9.py
from PySide6.QtWidgets import QApplication,QWidget,QGraphicsWidget
from PySide6.QtGui import QPainter,QPixmap,QPainterPath,QBrush,QRegion
from PySide6.QtCore import QRect,Qt

class MyWindow(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.resize(600,500)
        self.__pixmap=QPixmap("d:\\python\\pic.png")
    def paintEvent(self,event):
        painter=QPainter(self)  #未确定绘图设备
        painter.setClipping(True)

        rect_1 = QRect(self.width()/20,self.height()/10,self.width()/10*4,self.height()/10*3)
        rect_2 = QRect(self.width()/20,self.height()/10*5,self.width()/10*4,self.height()/10*3)
        rect_3 = QRect(self.width()/20*11,self.height()/10,self.width()/10*4,self.height()/10*3)
        rect_4 = QRect(self.width()/20*11,self.height()/10*5,self.width()/10*4,self.height()/10*3)
        region_1 = QRegion(rect_1)  #矩形剪切区域
        region_2 = QRegion(rect_2)  #矩形剪切区域
        region_3 = QRegion(rect_3,t=QRegion.Ellipse)  #椭圆形剪切区域
        region_4 = QRegion(rect_4,t=QRegion.Ellipse)  #椭圆剪切区域

        region = region_1.united(region_2)  #剪切区域并运算
        region = region.united(region_3)    #剪切区域并运算
        region = region.united(region_4)    #剪切区域并运算

        painter.setClipRegion(region)
        painter.drawPixmap(self.rect(), self.__pixmap)  # 在窗口上绘制图像
if __name__ == '__main__':
    app=QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
