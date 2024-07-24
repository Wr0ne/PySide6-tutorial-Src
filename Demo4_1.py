import sys  #Demo4_1.py
from PySide6.QtWidgets import  QApplication,QWidget,QLineEdit
from PySide6.QtCore import Qt

class MyWindow(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.resize(500,500)
        self.lineEdit=QLineEdit(self)
        self.lineEdit.setGeometry(0,0,500,30)
    def mousePressEvent(self, event):  #重写处理mousePress事件的函数
        template1 ="单击点的窗口坐标是x:{} y:{}"
        template2 = "单击点的屏幕坐标是x:{} y:{}"
        if event.button() == Qt.LeftButton:  #button()获取左键或右键
            string = template1.format(event.x(),event.y()) #x()和y()获取窗口坐标
            self.lineEdit.setText(string)
        if event.button() == Qt.RightButton:
            #globalX()和globalY()获取全局坐标
            string = template2.format(event.globalX(), event.globalY())
            self.lineEdit.setText(string)
if __name__ == '__main__':
    app=QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
