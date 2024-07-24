import sys   #Demo9_3.py
from PySide6.QtWidgets import QApplication,QHBoxLayout,QFileDialog,QWidget,QLabel
from PySide6.QtCore import Qt
from PySide6.QtGui import QMovie

class MyLabel(QLabel):
    def __init__(self,parent=None):
        super().__init__(parent)
    def mouseDoubleClickEvent(self,event):
        fileName, fil = QFileDialog.getOpenFileName(self, caption="选择动画文件",
            dir="d:\\",filter="动画文件(*.gif *.webp);;所有文件(*.*)")
        movie = QMovie(fileName)
        movie.setBackgroundColor(Qt.gray)
        if movie.isValid():
            self.setMovie(movie)
            movie.start()
class MyWindow(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.resize(800,600)
        self.setupUi()
    def  setupUi(self):  #界面
        self.label = MyLabel()
        self.label.setText("双击我，打开动画文件，播放动画！")
        self.label.setAlignment(Qt.AlignCenter)
        H = QHBoxLayout(self)
        H.addWidget(self.label)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
