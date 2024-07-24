import sys  # Demo11_3.py
from PySide6.QtWidgets import QApplication,QWidget,QPushButton
from PySide6.QtGui import QPainter,QPageSize,QPdfWriter
from PySide6.QtCore import QPointF
from math import sin,cos,pi
class MyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        btn_printer = QPushButton('Pdf 打印',self)
        btn_printer.clicked.connect(self.btn_printer_clicked)  #信号与槽连接
    def btn_printer_clicked(self):  #槽函数
        pdfWriter = QPdfWriter("d:/mystrars.pdf") #创建pdf文档生成器,设置文件名
        pageSize = QPageSize(QPageSize.A4)  #纸张尺寸
        pdfWriter.setPageSize(pageSize)     #设置纸张尺寸
        pdfWriter.setPdfVersion(QPdfWriter.PdfVersion_1_6)  #设置版本号
        painter = QPainter()
        if painter.begin(pdfWriter):
            size = pageSize.size(QPageSize.Millimeter)
            x = size.width()*20  #绘图区中心x坐标
            y = size.height()*20 #绘图区中心y坐标
            r = min(x/2,y/2)     #五角星的外接圆半径
            p1=QPointF(r*cos(-90* pi/180)+x,r* sin(-90* pi/180)+y)
            p2=QPointF(r*cos(-18* pi/180)+x,r* sin(-18* pi/180)+y)
            p3=QPointF(r*cos(54* pi/180)+x,r* sin(54* pi/180)+y)
            p4=QPointF(r*cos(126* pi/180)+x,r* sin(126* pi/180)+y)
            p5=QPointF(r*cos(198* pi/180)+x,r* sin(198* pi/180)+y)
            pageCopies = 3  #页数
            for i in range(1,pageCopies+1):
                    painter.drawPolyline([p1, p3, p5, p2, p4, p1])  #绘制五角星
                    print("正在打印第{}页，共{}页。".format(i,pageCopies))
                    if i != pageCopies:
                        pdfWriter.newPage()
            painter.end()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyWidget()
    win.show()
    sys.exit(app.exec())
