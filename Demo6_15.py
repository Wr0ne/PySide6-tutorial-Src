import sys,math   #Demo6_15.py
from PySide6.QtWidgets import (QApplication,QWidget,QGraphicsScene,
                             QGraphicsView,QVBoxLayout,QGraphicsItem)
from PySide6.QtCore import Qt,QRectF,QPointF
from PySide6.QtGui import QPolygonF,QPainterPath,QBrush

class axise(QGraphicsItem):  #坐标轴图项
    def __init__(self,width,height,parent=None):
        super().__init__(parent)
        self.__width=width
        self.__height=height
    def boundingRect(self):
        return QRectF(-5,-self.__height/2-20,self.__width+25,self.__height+40)
    def paint(self, painter,option,widget):
        pen=painter.pen()
        pen.setWidth(3)
        painter.setPen(pen)
        painter.drawLine(QPointF(0,0),QPointF(self.__width+20,0))  #横轴
        painter.drawLine(QPointF(0,-self.__height/2-20), QPointF(0,self.__height/2+20)) #纵轴

        brush=QBrush(Qt.SolidPattern)
        painter.setBrush(brush)
        path = QPainterPath()  #坐标轴箭头
        path.moveTo(QPointF(self.__width+20,0))
        path.lineTo(self.__width,5)
        path.lineTo(self.__width,-5)
        path.closeSubpath()
        path.moveTo(QPointF(0, -self.__height / 2 - 20))
        path.lineTo(5,-self.__height / 2)
        path.lineTo(-5,-self.__height / 2)
        path.closeSubpath()
        painter.drawPath(path)

        font=painter.font()
        font.setPixelSize(20)
        painter.setFont(font)
        painter.drawText(QPointF(self.__width,-20),"x轴")  #绘制文字
        painter.drawText(QPointF(20,-self.__height/2), "y轴")  #绘制文字
class sin_cos(QGraphicsItem):  #正弦和余弦图项
    def __init__(self,width,height,parent=None):
        super().__init__(parent)
        self.__width=width
        self.__height=height
    def boundingRect(self):
        return QRectF(-5,-self.__height/2-20,self.__width+25,self.__height+40)
    def paint(self, painter,option,widget):
        polygon_sin=QPolygonF()
        polygon_cos=QPolygonF()
        for i in range(360):
            x_value=i*self.__width/360
            sin_value=math.sin(i*math.pi/180)*(-1)*self.__height/2
            cos_value=math.cos(i*math.pi/180)*(-1)*self.__height/2

            polygon_sin.append(QPointF(x_value,sin_value))
            polygon_cos.append(QPointF(x_value,cos_value))
        painter.drawPolyline(polygon_sin)
        painter.drawPolyline(polygon_cos)
class MyWindow(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.resize(800,600)
        self.graphicsView=QGraphicsView()  #视图控件
        self.setupUI()
    def setupUI(self):
        v=QVBoxLayout(self)  #布局
        v.addWidget(self.graphicsView)
        w=500  #正弦曲线的宽度
        h=300  #正弦曲线的高度
        rectF=QRectF(-50,-50-h/2,w+100,h+100)  #场景的范围
        self.graphicsScene=QGraphicsScene(rectF)  #创建场景
        self.graphicsView.setScene(self.graphicsScene)  #视图窗口设置场景
        myItem_1=axise(w,h)  #自定义坐标轴图项
        myItem_2=sin_cos(w,h)  #自定义正弦和余弦图项
        myItem_2.setParentItem(myItem_1)  #设置图项的父子关系
        self.graphicsScene.addItem(myItem_1)  #添加自定义的图项
        rectangle=self.graphicsScene.addRect(rectF)  #添加矩形边框

        group=self.graphicsScene.createItemGroup([myItem_1,rectangle])  #创建组
        group.setFlag(QGraphicsItem.ItemIsMovable)  #设置组可以移动
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
