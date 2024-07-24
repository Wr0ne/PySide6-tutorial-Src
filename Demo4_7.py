import sys  #Demo4_7.py
from PySide6.QtWidgets import QApplication, QWidget,QPushButton,QHBoxLayout
from PySide6.QtCore import Qt

class MyWidget(QWidget):
    def __init__(self,parent = None):
        super().__init__(parent)
        self.ID_1 = self.startTimer(500,Qt.PreciseTimer)  #启动第1个定时器
        self.ID_2 = self.startTimer(1000,Qt.CoarseTimer)  #启动第2个定时器
        btn_1 = QPushButton("停止第1个定时器", self)
        btn_2 = QPushButton("停止第2个定时器", self)
        btn_1.clicked.connect(self.killTimer_1)
        btn_2.clicked.connect(self.killTimer_2)

        h=QHBoxLayout(self)
        h.addWidget(btn_1)
        h.addWidget(btn_2)
    def timerEvent(self, event):  #定时器事件
        print("我是第"+str(event.timerId())+"个定时器。")
    def killTimer_1(self):
        if self.ID_1:
            self.killTimer(self.ID_1)  #停止第1个定时器
    def killTimer_2(self):
        if self.ID_2:
            self.killTimer(self.ID_2)  #停止第2个定时器
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWidget()
    myWindow.show()
    sys.exit(app.exec())
