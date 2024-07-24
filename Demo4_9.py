import sys  #Demo4_9.py
from PySide6.QtWidgets import QApplication,QWidget,QPushButton,QFrame,QHBoxLayout
from PySide6.QtGui import QDrag
from PySide6.QtCore import QMimeData,Qt,QEvent,QCoreApplication

class MyEvent(QEvent):   #自定义事件
    #myID = QEvent.registerEventType(2000)
    def __init__(self,position,object_name=None):
        super().__init__(QEvent.User)
        #super().__init__(MyEvent.myID)
        self.__pos = position   #位置属性，可对数据做其他处理
        self.__name = object_name  #名称属性
    def get_pos(self):  #自定义事件的方法
        return self.__pos
    def get_name(self):   #自定义事件的方法
        return self.__name
class MyPushButton(QPushButton):
    def __init__(self,name=None,parent=None,window=None):
        super().__init__(parent)
        self.setText(name)
        self.window1=window
    def mousePressEvent(self, event):  #按键事件
        if event.button() == Qt.LeftButton:
            self.drag = QDrag(self)
            self.drag.setHotSpot(event.pos())
            mime = QMimeData()
            self.drag.setMimeData(mime)
            self.drag.exec()
    def moveEvent(self, event):
        self.__customEvent = MyEvent(event.pos(), self.objectName()) #自定义事件的实例
        QCoreApplication.sendEvent(self.window(), self.__customEvent)  #发送事件
class MyFrame(QFrame):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.setFrameShape(QFrame.Box)
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
        self.btn1 = MyPushButton("PushButton 1",self.frame_1,window=self)  #定义第1个按钮
        self.btn1.setObjectName("button1")  #按钮的名称
        self.btn2 = MyPushButton("PushButton 2",self.frame_1,window=self)  #定义第2个按钮
        self.btn2.setObjectName("button2")  #按钮的名称
        self.btn3 = MyPushButton("PushButton 3", self.frame_2,window=self)  # 定义第3个按钮
        self.btn3.setObjectName("button3")  #按钮的名称
        self.btn4 = MyPushButton("PushButton 4", self.frame_2,window=self)  # 定义第4个按钮
        self.btn4.setObjectName("button4")  #按钮的名称
    def customEvent(self,event) :  #自定义事件的处理函数
        if event.type() == MyEvent.User:
        #if event.type() == MyEvent.myID:
            if event.get_name() == "button1":
                self.btn3.move(event.get_pos())
            if event.get_name() == "button2":
                self.btn4.move(event.get_pos())
            if event.get_name() == "button3":
                self.btn1.move(event.get_pos())
            if event.get_name() == "button4":
                self.btn2.move(event.get_pos())
if __name__ == '__main__':
    app=QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
