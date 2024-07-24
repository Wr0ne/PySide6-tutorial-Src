import sys   #Demo6_4.py
from PySide6.QtWidgets import QApplication,QWidget
from PySide6.QtGui import QPen,QPainter,QBrush,QLinearGradient,QRadialGradient,QConicalGradient
from PySide6.QtCore import Qt,QPointF,QRectF

class MyWindow(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.resize(800,400)
    def paintEvent(self,event):
        painter=QPainter(self)
        pen=QPen()   #钢笔
        pen.setColor(Qt.darkBlue)
        pen.setStyle(Qt.DashLine)
        pen.setWidth(5)  #线条宽度
        painter.setPen(pen)  #设置钢笔
        w=self.width()
        h=self.height()
        linear=QLinearGradient(QPointF(0,0),QPointF(w/8,0))  #线性渐变
        linear.setStops([(0,Qt.red),(0.3,Qt.yellow),(0.6,Qt.green),(1,Qt.blue)]) #设置颜色
        linear.setSpread(QLinearGradient.ReflectSpread)  #镜像扩展
        brush1=QBrush(linear)  #用线性渐变定义刷子
        painter.setBrush(brush1)
        painter.drawRect(QRectF(0,0,w/2,h/2))  #画矩形

        conical=QConicalGradient(QPointF(w/4*3,h/4),h/6)
        conical.setAngle(60)   #起始角度
        conical.setColorAt(0,Qt.red)
        conical.setColorAt(1,Qt.yellow)
        brush2=QBrush(conical)
        painter.setBrush(brush2)
        painter.drawRect(QRectF(w / 2, 0, w / 2, h / 2))

        radial1=QRadialGradient(QPointF(w/4,h/4*3),w/8,QPointF(w/4,h/4*3),w/15)
        radial1.setColorAt(0,Qt.red)
        radial1.setColorAt(0.5,Qt.yellow)
        radial1.setColorAt(1,Qt.blue)
        radial1.setSpread(QRadialGradient.RepeatSpread)
        brush3=QBrush(radial1)
        painter.setBrush(brush3)
        painter.drawRect(QRectF(0,h/2,w/2,h/2))

        radial2 = QRadialGradient(QPointF(w /4*3, h/4 * 3),w/6, QPointF(w /5*4,h/5 * 4), w/10)
        radial2.setColorAt(0, Qt.red)
        radial2.setColorAt(0.5, Qt.yellow)
        radial2.setColorAt(1, Qt.blue)
        radial2.setSpread(QRadialGradient.ReflectSpread)
        brush4 = QBrush(radial2)
        painter.setBrush(brush4)
        painter.drawRect(QRectF(w/2, h / 2, w / 2, h / 2))
if __name__ == '__main__':
    app=QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
