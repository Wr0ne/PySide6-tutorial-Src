import sys  #Demo1_13.py
from PySide6.QtWidgets import QApplication,QWidget,QLabel,QPushButton
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap

class myWidget(QWidget):
    def __init__(self,parent = None):
        super().__init__(parent)
        self.setupUi()
        self.button.clicked.connect(self.bell_alert)

    def setupUi(self):
        self.setWindowTitle('Hello')
        self.resize(300, 150)

        self.label = QLabel(self)  #在窗口上创建标签
        self.label.setText('欢迎使用本书学习编程！')
        self.label.setGeometry(80, 50, 150, 20)

        self.button = QPushButton(self)
        self.button.setText("响铃与预警")
        self.button.setGeometry(90, 100, 100, 20)
    def bell_alert(self):
        QApplication.beep()  #程序发出响铃声
        QApplication.alert(win,duration=0)  #第2个窗口发出预警
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationDisplayName("欢迎程序")  #设置所有窗口标题栏上显示的名称
    app.setEffectEnabled(Qt.UI_AnimateCombo)
    app.setWindowIcon(QPixmap(r'd:\python\welcome.png'))  #为所有窗口设置图标
    win = QWidget()  #创建第1个窗口
    win.show()
    myWindow = myWidget()  #用myWidget()创建第2个窗口
    myWindow.show()
    sys.exit(app.exec())
