import sys  #Demo2_14.py
from PySide6.QtWidgets import QApplication,QWidget,QProgressBar,QPushButton,QVBoxLayout
from PySide6.QtCore import Qt,QTimer

class MyWindow(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setWindowTitle("进度条实例")
        self.resize(500, 200)
        self.setupUi()  #调用函数，建立界面上的控件
        self.total_time = 0  #该属性记录时间
    def setupUi(self):  #建立界面上的控件
        self.progressBar_1 = QProgressBar()  #创建第1个进度条
        self.progressBar_1.setRange(0, 10000)  #设置进度条的最小值和最大值
        self.progressBar_2 = QProgressBar()  #创建第2个进度条
        self.progressBar_2.setRange(0, 10000)  #设置进度条的最小值和最大值
        self.progressBar_2.setInvertedAppearance(True)  #外观反转
        self.progressBar_2.setAlignment(Qt.AlignCenter)
        self.progressBar_2.setFormat("当前进度：%p%")
        self.progressBar_3 = QProgressBar()  #创建第3个进度条
        self.progressBar_3.setRange(0, 0)  #设置进度条的最小值和最大值相等
        self.btn_start = QPushButton('Start')  #创建按钮
        v = QVBoxLayout(self)  #竖直布局
        v.addWidget(self.progressBar_1)  #在布局中添加进度条
        v.addWidget(self.progressBar_2)  #在布局中添加进度条
        v.addWidget(self.progressBar_3)  #在布局中添加进度条
        v.addWidget(self.btn_start)  #在布局中添加按钮
        self.timer = QTimer(self)  #创建定时器
        self.timer.setInterval(10)  #设置定时器每隔10毫秒发送一次timeout信号

        self.btn_start.clicked.connect(self.btn_start_clicked) #按钮单击信号与槽函数连接
        self.timer.timeout.connect(self.timer_timeout) #定时器timeout信号与槽函数连接
    def btn_start_clicked(self):   #按钮的槽函数
        if self.btn_start.text() == 'Start':
            self.timer.start()
            self.btn_start.setText('Stop')
        elif self.btn_start.text() == 'Stop':
            self.timer.stop()
            self.btn_start.setText('Start')
    def timer_timeout(self):  #定时器的槽函数
        self.total_time = self.total_time + 10
        if self.total_time > 10000:  #进度条的最大值是10000
            self.total_time = 0
        self.progressBar_1.setValue(self.total_time)  #设置进度条的值
        self.progressBar_2.setValue(self.total_time)  #设置进度条的值
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
