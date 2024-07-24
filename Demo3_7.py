import sys  #Demo3_7.py
from PySide6.QtWidgets import (QApplication,QMenuBar,QWidgetAction,QPushButton,
                QSlider,QHBoxLayout,QWidget)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt,QSize

class MyAction(QWidgetAction):    #创建继承自QWidgetAction的类
    def createWidget(self,parent):  #重写createWidget()函数
        self.widget = QWidget(parent)
        self.setDefaultWidget(self.widget)
        self.button = QPushButton()
        self.button.setFlat(True)
        self.button.setIcon(QPixmap("d:\\python\\speaker_on.png"))
        self.button.setIconSize(QSize(30,30))
        self.slide = QSlider(Qt.Horizontal)
        self.slide.setFixedWidth(200)

        H = QHBoxLayout(self.widget)
        H.addWidget(self.button)
        H.addWidget(self.slide)

        self.mute = False

        self.button.clicked.connect(self.mute_requested)  #信号与槽函数的连接
    def mute_requested(self):  #槽函数
        self.mute = not self.mute
        if self.mute:
            self.button.setIcon(QPixmap("d:\\python\\speaker_off.png"))
            self.slide.setEnabled(False)
        else:
            self.button.setIcon(QPixmap("d:\\python\\speaker_on.png"))
            self.slide.setEnabled(True)
class MyWindow(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setWindowTitle("QWidgetAction应用实例")
        self.setupUi()
    def setupUi(self):
        menuBar = QMenuBar(self)
        self.menuVolume = menuBar.addMenu("音量控制")
        self.actVolume = MyAction(self.menuVolume)  #自定义动作的实例
        self.menuVolume.addAction(self.actVolume)   #自定义动作加入到菜单中
if __name__ == '__main__':
    app=QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
