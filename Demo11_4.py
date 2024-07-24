import sys  # Demo11_4.py
from PySide6.QtWidgets import QApplication,QWidget,QPushButton
from PySide6.QtPrintSupport import QPrinter,QPrintDialog
from PySide6.QtGui import QPen,QPainter
from PySide6.QtCore import QPointF
from math import sin,cos,pi

class MyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.btn_printer = QPushButton('打印',self)
        self.btn_printer.clicked.connect(self.btn_printer_clicked)  #信号与槽连接
        self.printDialog = QPrintDialog(self)
        self.printDialog.accepted.connect(self.printDialog_accepted) #信号与槽连接
    def btn_printer_clicked(self):  #槽函数
        self.printDialog.exec()
    def printDialog_accepted(self,printer):  #槽函数
        if printer.isValid():
            painter = QPainter()
            if painter.begin(printer):
                pen = QPen()  #钢笔
                pen.setWidth(3)  #线条宽度
                painter.setPen(pen)  #设置钢笔
                x = printer.paperRect(QPrinter.DevicePixel).width()/2 #中心x坐标
                y = printer.paperRect(QPrinter.DevicePixel).height()/2 #中心y坐标
                r = min(printer.pageRect(QPrinter.DevicePixel).width()/2,
                   printer.paperRect(QPrinter.DevicePixel).height()/2)#外接圆半径
                p1=QPointF(r*cos(-90*pi/180)+x,r*sin(-90*pi/180)+y)
                p2=QPointF(r*cos(-18*pi/180)+x,r*sin(-18*pi/180)+y)
                p3=QPointF(r*cos(54*pi/180)+x,r*sin(54*pi/180)+y)
                p4=QPointF(r*cos(126*pi/180)+x,r*sin(126*pi/180)+y)
                p5=QPointF(r*cos(198*pi/180)+x,r*sin(198*pi/180)+y)
                painter.drawPolyline([p1, p3, p5, p2, p4, p1])  #绘制五角星
                painter.end()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyWidget()
    win.show()
    sys.exit(app.exec())
