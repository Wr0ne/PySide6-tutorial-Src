import sys   #Demo2_7.py
from PySide6.QtWidgets import QApplication,QWidget,QPushButton
from PySide6.QtGui import QPixmap,QIcon

class MyWidget(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        pix =QPixmap()
        pix.load("d:\\python\\welcome.png")
        icon =QIcon(pix)
        self.setWindowIcon(icon)   #设置窗口图标
        btn = QPushButton(self)
        btn.setIcon(icon)  #设置按钮图标
if __name__ == '__main__':
    app=QApplication(sys.argv)
    #pix = QPixmap(":/icons/pic/student.png")
    #icon = QIcon(pix)
    #app.setWindowIcon(icon)   #设置应用程序图标
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
