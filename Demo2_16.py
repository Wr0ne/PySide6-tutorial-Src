import sys  #Demo2_16.py
from PySide6.QtWidgets import QApplication,QWidget,QPushButton
from PySide6.QtGui import QPainter,QPixmap,QBitmap
from PySide6.QtCore import QRect,QTimer

class MyWindow (QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setWindowTitle("定时器")
        path = "d:\\python\\pic.png"
        self.pix = QPixmap(path)
        self.bit = QBitmap(path)
        self.rect = QRect(0, 0, self.pix.width(),self.pix.height())
        self.resize(self.rect.size())

        self.timer_1 = QTimer(self)  #第1个定时器
        self.timer_1.setInterval(2000)  #第1个定时器的时间间隔
        self.timer_1.timeout.connect(self.timer_1_slot)  #第1个定时器信号与槽函数的连接
        self.timer_1.start()  #启动第1个定时器
        self.status = True  #指示变量
        self.timer_2 = QTimer(self)  #第2个定时器
        self.timer_2.setInterval(1000)  #第2个定时器的时间间隔
        self.timer_2.timeout.connect(self.pushButton_enable) #第2个定时器信号与槽函数的连接
        self.duration = 9  #按钮激活时间
        self.pushButton = QPushButton("单击发送验证码",self)
        self.pushButton.setGeometry(10,10,200,30)
        self.pushButton.clicked.connect(self.timer_2_start) #按钮单击信号与槽函数的连接
    def timer_1_slot(self):
        self.status = not self.status
        self.update()  #更新窗口，会触发paintEvent()，调用paintEvent()函数
    def paintEvent(self, event):  #paintEvent事件
        painter = QPainter(self)
        if self.status:
            painter.drawPixmap(self.rect,self.pix)
        else:
            painter.drawPixmap(self.rect, self.bit)
    def timer_2_start(self):  #按钮的槽函数
        self.timer_2.start()
        self.pushButton.setEnabled(False)
        self.pushButton.setText(str(self.duration +1)+"后可重新发送验证码")
    def pushButton_enable(self):
        if self.duration >0 :
            self.pushButton.setText(str(self.duration)+"后可重新发送验证码")
            self.duration = self.duration - 1
        else:
            self.pushButton.setEnabled(True)
            self.pushButton.setText("单击发送验证码")
            self.timer_2.stop()  #停止定时器
            self.duration = 9
if __name__ == '__main__':
    app=QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
