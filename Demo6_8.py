import sys,os   #Demo6_8.py
from PySide6.QtWidgets import QApplication,QWidget,QGraphicsWidget
from PySide6.QtGui import QPainter,QPixmap,QPainterPath,QBrush
from PySide6.QtCore import QRectF,Qt

class MyWindow(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.resize(600,500)
        self.__pixmap=QPixmap("d:\\python\\pic.png")
    def paintEvent(self,event):
        painter=QPainter()  #未确定绘图设备
        rect = QRectF(0, 0, self.__pixmap.width(), self.__pixmap.height())  #获取图片的矩形
        path=QPainterPath()  #绘图路径
        path.addRect(rect)  #添加矩形
        path.addEllipse(rect)  #添加椭圆
        path.setFillRule(Qt.OddEvenFill)  #设置填充方式
        brush = QBrush(Qt.SolidPattern)  #画刷
        brush.setColor(Qt.black)  #画刷颜色

        painter.begin(self.__pixmap)  # 以QPixmap作为绘图设备
        painter.setBrush(brush)  # 设置画刷
        painter.setRenderHint(QPainter.Antialiasing)  #抗锯齿
        painter.drawPath(path)  #在QPixmap上绘图
        painter.end()  #结束绘图
        if not os.path.exists("d:\\python\\new.png"):
            self.__pixmap.save("d:\\python\\new.png")  #保存图像

        painter.begin(self)  #以窗口作为位图设备
        painter.drawPixmap(self.rect(), self.__pixmap)  #在窗口上绘制图像
        painter.end()  #结束绘图
if __name__ == '__main__':
    app=QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
