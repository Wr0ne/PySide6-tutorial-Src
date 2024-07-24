import sys   #Demo2_21.py
from PySide6.QtWidgets import QApplication,QWidget,QSplitter, QLabel, QHBoxLayout
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap

class MyWindow(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.widget_setupUi()
    def widget_setupUi(self):  #建立主程序界面
        label_1 = QLabel()
        label_2 = QLabel()
        label_3 = QLabel()
        label_1.setPixmap(QPixmap('d:/python/pic.png'))
        label_2.setPixmap(QPixmap('d:/python/pic.png'))
        label_3.setPixmap(QPixmap('d:/python/pic.png'))
        splitter_H = QSplitter(Qt.Horizontal)
        splitter_V = QSplitter(Qt.Vertical)
        h = QHBoxLayout(self)
        h.addWidget(splitter_H)
        splitter_H.addWidget(label_1)
        splitter_H.addWidget(splitter_V)
        splitter_V.addWidget(label_2)
        splitter_V.addWidget(label_3)
if __name__ == '__main__':
    app=QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
