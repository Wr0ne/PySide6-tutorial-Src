import sys   #Demo6_13.py
from PySide6.QtWidgets import QApplication,QWidget
from PySide6.QtGui import QPainter,QPixmap,QPainterPath,QBrush
from PySide6.QtCore import QRectF,Qt

class MyWindow(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.resize(600,500)
        self.__pixmap=QPixmap("d:\\python\\pic.png")
    def paintEvent(self,event):
        painter=QPainter(self)
        painter.drawPixmap(self.rect(),self.__pixmap)  #绘制图片

        rect = QRectF(0, 0, self.width(), self.height())  #获取窗口的矩形
        path=QPainterPath()  #绘图路径
        path.addRect(rect)  #添加矩形
        path.addEllipse(rect)  #添加椭圆
        path.setFillRule(Qt.OddEvenFill)  #设置填充方式
        brush = QBrush(Qt.SolidPattern)  #画刷
        brush.setColor(Qt.black)
        painter.setBrush(brush)  # 设置画刷

        painter.setCompositionMode(QPainter.CompositionMode_SourceOver) #设置图像合成方式
        painter.drawPath(path)
if __name__ == '__main__':
    app=QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
