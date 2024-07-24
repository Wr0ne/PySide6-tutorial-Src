import sys,math   #Demo6_11.py
from PySide6.QtWidgets import QApplication,QWidget
from PySide6.QtGui import QPainter,QTransform
from PySide6.QtCore import QPointF,Qt

class MyWindow(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.resize(600,500)
    def paintEvent(self,event):
        transform = QTransform()
        transform.translate(self.width()/2,self.height()/2) #原点平移到窗口中心位置
        transform.rotate(180, Qt.XAxis)  #沿着x轴旋转180°，y轴向上
        
        painter = QPainter(self)
        painter.setTransform(transform)  #设置变换
        r=100   #五角星的外接圆半径
        points = list()
        for i in range(5):
            x=r*math.cos((90+144*i)*math.pi/180)
            y=r*math.sin((90+144*i)*math.pi/180)
            points.append(QPointF(x,y))

        painter.drawPolygon(points)  #绘制多边形
if __name__ == '__main__':
    app=QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
