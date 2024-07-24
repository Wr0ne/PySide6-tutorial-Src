import sys  #Demo2_18.py
from PySide6.QtWidgets import (QApplication,QWidget,QPushButton,QLCDNumber,QDateEdit,
QTimeEdit, QDateTimeEdit,QCalendarWidget,QVBoxLayout,QHBoxLayout)
from PySide6.QtCore import QTimer,QDateTime,Qt

class MyWindow(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setWindowTitle("Date and Time")
        self. resize(500,400)
        self.setupUI()  #调用函数，建立界面控件

        self.dateTime = QDateTime.currentDateTime()  #记录时间的属性
        self.calendarWidget.setSelectedDate(self.dateTime.date())
        self.timeEidt.setTime(self.dateTime.time())
        self.dateEdit.setDate(self.dateTime.date())
        self.datetimeEdit.setDateTime(self.dateTime)

        self.timer = QTimer(self)  #定时器
        self.timer.setInterval(10)  #每10毫秒发送一次信号
        self.timer.setTimerType(Qt.PreciseTimer)
        self.timer.start()
        self.lcdWidget.display(self.dateTime.toString("yyyy:MM:dd hh:mm:ss"))

        self.timer.timeout.connect(self.time_add)  #信号与槽的关联
        self.calendarWidget.clicked.connect(self.calendarWidget_clicked) #信号与槽关联
        self.timeEidt.timeChanged.connect(self.timeEdit_changed)  #信号与槽关联
        self.dateEdit.dateChanged.connect(self.dateEdit_changed)  #信号与槽关联
        self.datetimeEdit.dateTimeChanged.connect(self.datetimeEdit_changed) #信号与槽关联
        self.pushButton.clicked.connect(self.pushButton_clicked)  #信号与槽关联
    def setupUI(self):  #建立界面
        self.timeEidt = QTimeEdit()
        self.timeEidt.setDisplayFormat("hh:mm:ss")
        self.dateEdit = QDateEdit()
        self.dateEdit.setDisplayFormat("yyyy/MM/dd")
        self.datetimeEdit = QDateTimeEdit()
        self.datetimeEdit.setDisplayFormat("yyyy/MM/dd hh:mm:ss")
        self.pushButton = QPushButton("当前时间")
        font = self.timeEidt.font()
        font.setPointSize(15)
        self.timeEidt.setFont(font)
        self.dateEdit.setFont(font)
        self.datetimeEdit.setFont(font)
        self.pushButton.setFont((font))

        vLayout = QVBoxLayout()
        vLayout.addWidget(self.timeEidt)
        vLayout.addWidget(self.dateEdit)
        vLayout.addWidget(self.datetimeEdit)
        vLayout.addWidget(self.pushButton)

        self.calendarWidget = QCalendarWidget()
        self.calendarWidget.setFont(font)
        hLayout = QHBoxLayout()
        hLayout.addLayout(vLayout)
        hLayout.addWidget(self.calendarWidget)

        self.lcdWidget = QLCDNumber(20)
        vertLayout = QVBoxLayout(self)
        vertLayout.addWidget(self.lcdWidget,stretch=1)
        vertLayout.addLayout(hLayout)
    def time_add(self):  #槽函数
        self.dateTime.setTime(self.dateTime.addMSecs(10).time())
        self.lcdWidget.display(self.dateTime.toString("yyyy:MM:dd hh:mm:ss"))
    def calendarWidget_clicked(self,d):  #槽函数
        self.dateTime.setDate(d)
        self.dateEdit.setDate(self.dateTime.date())
        self.datetimeEdit.setDate(self.dateTime.date())
    def timeEdit_changed(self,t):  #槽函数
        self.dateTime.setTime(t)
        self.datetimeEdit.setTime(self.dateTime.time())
    def dateEdit_changed(self,d):  #槽函数
        self.dateTime.setDate(d)
        self.calendarWidget.setSelectedDate(self.dateTime.date())
        self.datetimeEdit.setDate(self.dateTime.date())
    def datetimeEdit_changed(self,dt):  #槽函数
        self.dateTime.setDate(dt.date())
        self.dateTime.setTime((dt.time()))
        self.calendarWidget.setSelectedDate(self.dateTime.date())
        self.dateEdit.setDate(self.dateTime.date())
        self.timeEidt.setTime(self.dateTime.time())
    def pushButton_clicked(self):  #槽函数
        self.timeEidt.setTime(QDateTime.currentDateTime().time())
        self.dateEdit.setDate(QDateTime.currentDateTime().date())
if __name__ == '__main__':
    app=QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
