import sys  #Demo2_17.py
from PySide6.QtWidgets import QApplication,QWidget,QLabel,QLCDNumber
from PySide6.QtCore import QTimer,QDateTime

class MyWindow(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setWindowTitle("LCD Number")
        self. resize(500,200)
        self.label = QLabel("距离2024年春节还有：",self)
        font = self.label.font()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setGeometry(100,50,300,50)
        self.lcdNumber = QLCDNumber(12,self)
        self.lcdNumber.setGeometry(100,100,300,50)
        self.sprintDay = QDateTime(2024,1,29,0,0,0)  #2024年春节时间
        self.timer = QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.change)
        self.timer.start()
    def change(self):
        self.current  = QDateTime.currentDateTime()  #获取系统的当前日期时间
        seconds = self.current.secsTo(self.sprintDay)  #计算到目的日期的秒数
        days = seconds//(3600*24)  #计算剩余天
        hours = (seconds-days*3600*24)//3600  #计算剩余小时
        minutes = (seconds-days*3600*24-hours*3600)//60  #计算剩余分钟
        seconds = seconds-days*3600*24-hours*3600-minutes*60  #计算剩余秒

        string = "{:03d}:{:02d}:{:02d}:{:02d}".format(days,hours,minutes,seconds)
        self.lcdNumber.display(string)
if __name__ == '__main__':
    app=QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
