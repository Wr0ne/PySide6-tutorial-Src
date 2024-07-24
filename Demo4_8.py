import sys  #Demo4_8.py
from PySide6.QtWidgets import QApplication,QWidget,QPushButton,QFrame,QHBoxLayout
from PySide6.QtGui import QDrag
from PySide6.QtCore import QMimeData,Qt,QEvent

class MyPushButton(QPushButton):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setText("MyPushButton")
    def mousePressEvent(self, event):  #按键事件
        if event.button() == Qt.LeftButton:
            self.drag = QDrag(self)
            self.drag.setHotSpot(event.pos())
            mime = QMimeData()
            self.drag.setMimeData(mime)
            self.drag.exec()
class MyFrame(QFrame):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.setFrameShape(QFrame.Box)
        self.btn = MyPushButton(self)
    def dragEnterEvent(self,event):
        self.child = self.childAt(event.pos())  #获取指定位置的控件
        if self.child:
            event.accept()
        else:
            event.ignore()
    def dragMoveEvent(self,event):
        if self.child:
            self.child.move(event.pos() - self.child.drag.hotSpot())
class MyWindow(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setupUi()
        self.resize(600,400)
        self.setAcceptDrops(True)
    def setupUi(self):
        self.frame_1 = MyFrame(self)
        self.frame_2 = MyFrame(self)
        H = QHBoxLayout(self)
        H.addWidget(self.frame_1)
        H.addWidget(self.frame_2)

        self.frame_1.btn.installEventFilter(self)  #将btn的事件注册到窗口self上
        self.frame_2.btn.installEventFilter(self)  #将btn的事件注册到窗口self上
    def eventFilter(self,watched,event):  #事件过滤函数
        if watched == self.frame_1.btn and event.type()==QEvent.Move:
            self.frame_2.btn.move(event.pos())
            return True
        if watched == self.frame_2.btn and event.type()==QEvent.Move:
            self.frame_1.btn.move(event.pos())
            return True
        return super().eventFilter(watched,event)
if __name__ == '__main__':
    app=QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
