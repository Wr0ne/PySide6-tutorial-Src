import sys  #Demo3_2.py
from PySide6.QtWidgets import QApplication,QPushButton,QLabel

class MyWindow(QLabel):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setWindowTitle("QLabel")
        self.resize(250, 100)
        label = QLabel("我是QLablel")
        label.setParent(self) # setParent()方法
        label.setGeometry(80, 20, 100, 30)
        btn=QPushButton("我是QPushButton", self)
        btn.setGeometry(60, 50, 100, 30)
if __name__ == '__main__':
    app=QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
