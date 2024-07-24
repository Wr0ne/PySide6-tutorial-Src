import sys   #Demo6_7.py
from PySide6.QtWidgets import QApplication,QWidget
from PySide6.QtGui import QPen,QPainter,QLinearGradient,QBrush
from PySide6.QtCore import Qt,QRect,QTimer

class MyWindow(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.resize(1000,300)
        self.__text="北京诺思多维科技有限公司"
        self.__start=0
        self.__rect=QRect(0,0,self.width(),self.height())  #记录文字的绘图范围
        self.timer = QTimer(self)  #定时器
        self.timer.timeout.connect(self.timeout)
        self.timer.setInterval(10)
        self.timer.start()
    def paintEvent(self,event):
        painter = QPainter(self)
        font = painter.font()
        font.setFamily("黑体")
        font.setBold(True)
        font.setPointSize(50)
        painter.setFont(font)

        linear=QLinearGradient(self.__rect.topLeft(),self.__rect.bottomRight())  #字体渐变
        linear.setColorAt(0,Qt.red)
        linear.setColorAt(0.5,Qt.yellow)
        linear.setColorAt(1,Qt.green)

        linear2=QLinearGradient(self.__rect.left(),0,self.__rect.right(),0)  #背景渐变
        linear2.setColorAt(0.4, Qt.darkBlue)
        linear2.setColorAt(0.5, Qt.white)
        linear2.setColorAt(0.6, Qt.darkBlue)

        brush= QBrush(linear)  #字体画刷
        brush2=QBrush(linear2)  #背景画刷
        pen=QPen()   #钢笔
        pen.setBrush(brush)   #设置钢笔画刷
        painter.setPen(pen)
        painter.setBackgroundMode(Qt.OpaqueMode)  #背景模式不透明
        painter.setBackground(brush2)  #设置背景画刷
        painter.setBrushOrigin(self.__start,self.__rect.top())  #设置画刷的起始点
        self.__rect=painter.drawText(self.rect(),Qt.AlignCenter,self.__text) #绘制文字
    def timeout(self):  #定时器槽函数
        if self.__start > self.__rect.width()/2:
            self.__start= int(-self.__rect.width()/2)
        self.__start=self.__start + 5
        self.update()
if __name__ == '__main__':
    app=QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
