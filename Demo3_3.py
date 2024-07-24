import sys  #Demo3_3.py
from PySide6.QtWidgets import QApplication, QWidget, QLabel,QPushButton, \
                              QFrame, QVBoxLayout, QHBoxLayout
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont

class MyWindow(QWidget):
    def __init__(self,parent=None,f=Qt.Widget):
        super().__init__(parent,f=f)
        self.setStyleSheet('border:0px')
        self.setContentsMargins(0,0,0,0)
        self.resize(400,300)
        self.move(300,200)
        font=QFont()
        font.setPointSize(10)
        #下面创建自定义标题栏
        title = QLabel("欢迎来到我的世界")
        title.setFont(font)
        closeBtn = QPushButton("关闭")
        closeBtn.clicked.connect(self.close)
        closeBtn.setFixedSize(30,15)
        closeBtn.setFont(font)
        closeBtn.setContentsMargins(0,0,0,0)

        titleBar = QWidget()
        titleBar.setFixedHeight(13)
        H = QHBoxLayout(titleBar)
        H.setAlignment(Qt.AlignTop)
        H.setContentsMargins(0,0,0,0)
        H.setSpacing(0)

        H.addWidget(title)
        H.addWidget(closeBtn)
        workArea = QFrame()
        V = QVBoxLayout(self)
        V.setSpacing(0)
        V.addWidget(titleBar)
        V.addWidget(workArea)
        V.setContentsMargins(0,0,0,0)
        # add more... ，下面创建有父窗口的窗口，窗口类型是Qt.Window
        test_window = QWidget(parent=self, f=Qt.Window)
        test_window.setWindowTitle("Test Window")
        test_window.show()
        test_window.resize(300,100)
class WelcomeWindow(QWidget):
    def __init__(self,parent=None,f = Qt.Widget):
        super().__init__(parent,f)
        self.resize(300, 100)
        self.setupUi()
    def setupUi(self):
        label = QLabel("欢迎来到我的世界！")
        label.setParent(self)
        label.setGeometry(70, 30, 200, 30)
        font = label.font()
        font.setPointSize(15)
        label.setFont(font)
        btn = QPushButton("进入>>",self)
        btn.setGeometry(200,70,70,20)
        btn.clicked.connect(self.enter)  #信号与槽的连接
    def enter(self):
        self.win = MyWindow(f=Qt.FramelessWindowHint) #无边框窗口
        self.win.show()  #显示另外一个窗口
        self.close()
if __name__ == '__main__':
    app=QApplication(sys.argv)
    welcome = WelcomeWindow(parent=None,f=Qt.SplashScreen)  #欢迎窗口
    welcome.show()
    sys.exit(app.exec())
