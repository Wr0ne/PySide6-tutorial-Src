import sys  #Demo4_2.py
from PySide6.QtWidgets import  QApplication,QWidget,QLineEdit
from PySide6.QtCore import QEvent,Qt

class MyWindow(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.resize(500,500)
        self.lineEdit=QLineEdit(self)
        self.lineEdit.setGeometry(0,0,500,30)
    def event(self, even):  #重写event函数
        if even.type() == QEvent.MouseButtonPress:  #按键的情况
            template1 = "单击点的窗口坐标是x:{} y:{}"
            template2 = "单击点的屏幕坐标是x:{} y:{}"
            if even.button() == Qt.LeftButton:   #按左键的情况
                string = template1.format(even.x(), even.y()) 
                self.lineEdit.setText(string)
                return True
            elif even.button() == Qt.RightButton:  #按右键的情况
                string = template2.format(even.globalX(), even.globalY())
                self.lineEdit.setText(string)
                return True
            else:  #按中键的情况
                return True
        else:   #对于不是按鼠标键的事件，交给QWidget来处理
            finished = super().event(even)  #super()函数调用父类函数
            return finished
if __name__ == '__main__':
    app=QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
