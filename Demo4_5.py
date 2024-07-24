import sys  #Demo4_5.py
from PySide6.QtWidgets import QApplication,QWidget,QPushButton,QFrame,QHBoxLayout
from PySide6.QtGui import QDrag
from PySide6.QtCore import QMimeData,Qt

class MyPushButton(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
    def mousePressEvent(self, event):  #按键事件
        if event.button() == Qt.LeftButton:
            self.drag = QDrag(self)
            self.drag.setHotSpot(event.pos())
            mime = QMimeData()
            self.drag.setMimeData(mime)
            self.drag.exec()
class MyFame(QFrame):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.setFrameShape(QFrame.Box)
        self.btn_1 = MyPushButton(self)
        self.btn_1.setText("push button 1")
        self.btn_1.move(100,100)
        self.btn_2 = MyPushButton(self)
        self.btn_2.setText("push button 2")
        self.btn_2.move(200,200)
    def dragEnterEvent(self,event):
        self.child = self.childAt(event.pos())  #获取指定位置的控件
        event.accept()
    def dragMoveEvent(self,event):
        if self.child:
            self.child.move(event.pos()-self.child.drag.hotSpot())
    def dropEvent(self,event):
        if self.child:
            self.child.move(event.pos() - self.child.drag.hotSpot())
class MyWindow(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setupUi()
        self.resize(600,400)
        self.setAcceptDrops(True)
    def setupUi(self):
        self.frame_1= MyFame(self)
        self.frame_2 =MyFame(self)
        H = QHBoxLayout(self)
        H.addWidget(self.frame_1)
        H.addWidget(self.frame_2)
if __name__ == '__main__':
    app=QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
