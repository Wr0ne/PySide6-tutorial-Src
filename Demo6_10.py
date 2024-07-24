import sys   #Demo6_10.py
from PySide6.QtWidgets import QApplication,QWidget,QSplitter,QHBoxLayout
from PySide6.QtGui import QPen,QPainter,QPainterPath,QBrush,QPalette,QTransform
from PySide6.QtCore import QPointF,Qt,QTimer

class myPainterTransform(QWidget):  #用坐标变换的方法创建太极图像
    def __init__(self,rotational=False,scaled=False,translational=False,sheared=False,parent=None):
        super().__init__(parent)
        palette=self.palette()
        palette.setColor(QPalette.Window,Qt.darkYellow)
        self.setPalette(palette)       #设置窗口背景
        self.setAutoFillBackground(True)
        self.__rotational=rotational      #获取输入的参数值
        self.__scaled=scaled            #获取输入的参数值
        self.__translational=translational  #获取输入的参数值
        self.__sheared=sheared         #获取输入的参数值

        self.__rotation=0    #旋转角度
        self.__scale=1       #缩放系数
        self.__translation=0  #平移量
        self.__sx=0         #错切系数
        self.__sy=0         #错切系数

        self.timer=QTimer(self)  #定时器
        self.timer.timeout.connect(self.timeout)
        self.timer.setInterval(10)
        self.timer.start()
    def paintEvent(self,event):
        self.center = QPointF(self.width() / 2, self.height() / 2)
        painter = QPainter(self)
        painter.translate(self.center)  #将坐标系移动到中心位置

        pen = QPen()
        pen.setWidth(3)
        pen.setColor(Qt.black)
        painter.setPen(pen)

        path = QPainterPath()  #路径
        r = min(self.width(),self.height())/3  #外部大圆的半径
        r1 = r/7  #内部小圆的半径
        path.moveTo(0,-r)
        path.arcTo(-r,-r, 2 * r, 2 * r, 90, 360) #外部大圆
        path.arcTo(-r,-r, 2 * r, 2 * r, 90, -180) #反向半圆

        path.moveTo(0,r)
        path.arcTo(-r / 2,0, r, r, -90, 180) #内部半圆
        path.arcTo(-r/2, -r, r, r, 270, -180)  #内部半圆

        path.moveTo( r1,- r / 2)
        path.arcTo( -r1, -r/2-r1,2*r1,2*r1,0,360) #内部小圆
        path.moveTo( r1, r / 2)
        path.arcTo( -r1, r/2-r1,2*r1,2*r1,0,-360) #内部小圆

        path.setFillRule(Qt.WindingFill)  #填充方式
        brush=QBrush(Qt.SolidPattern)
        painter.setBrush(brush)   #设置画刷

        painter.rotate(self.__rotation)  #坐标系旋转
        painter.scale(self.__scale,self.__scale)  #坐标系缩放
        painter.translate(self.__translation,0)  #坐标系平移
        if self.__sheared:
            painter.shear(self.__sx,self.__sy)

        painter.drawPath(path)  # 绘制路径
        super().paintEvent(event)
    def timeout(self):
        if self.__rotational:   #设置坐标系的旋转角度值参数
            if self.__rotation<-360:
                self.__rotation=0
            self.__rotation=self.__rotation-1
        if self.__scaled:  #设置坐标系的缩放比例参数
            if self.__scale>2:
                self.__scale=0.2
            self.__scale=self.__scale+0.005
        if self.__translational:  #设置坐标系的平移量参数
            if self.__translation>self.width()/2 + min(self.width(),self.height())/3:
                self.__translation=-self.width()/2-min(self.width(),self.height())/3
            self.__translation=self.__translation+1
        self.update()
    def setShearFactor(self,sx=0,sy=0):
        self.__sx=sx
        self.__sy=sy
class MyWindow(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setupUi()
        self.resize(800,600)
    def setupUi(self):
        h=QHBoxLayout(self)  #布局
        splitter_1=QSplitter(Qt.Horizontal)
        splitter_2=QSplitter(Qt.Vertical)
        splitter_3=QSplitter(Qt.Vertical)
        h.addWidget(splitter_1)
        splitter_1.addWidget(splitter_2)
        splitter_1.addWidget(splitter_3)

        taiji_1 = myPainterTransform(rotational=True)  #第1个太极图，能够旋转
        taiji_2 = myPainterTransform(scaled=True)  #第2个太极图，能够缩放
        taiji_3 = myPainterTransform(translational=True)  #第3个太极图，能够平动
        taiji_4 = myPainterTransform(sheared=True)  #第4个太极图，错切
        taiji_4.setShearFactor(0.4,0.2)  #设置错切系数
        splitter_2.addWidget(taiji_1);  splitter_2.addWidget(taiji_2)
        splitter_3.addWidget(taiji_3);  splitter_3.addWidget(taiji_4)
if __name__ == '__main__':
    app=QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
