import sys  #Demo2_8.py
from PySide6.QtWidgets import QApplication,QWidget
from PySide6.QtGui import QPainter,QPixmap,QBitmap,QCursor
from PySide6.QtCore import QRect,Qt

class SetCursor(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        bit = QBitmap(32,32)  #创建32*32的位图
        bit_mask = QBitmap(32,32)  #创建32*32的位图
        bit.fill(Qt.black)   #设置填充颜色
        bit_mask.fill(Qt.white)   #设置填充颜色
        self.setCursor(QCursor(bit,bit_mask))   #设置光标
    def paintEvent(self, event):
        pix = QPixmap()
        rect = QRect(0,0,self.width(),self.height())
        pix.load("d:\\python\\pic.png")

        painter = QPainter(self)
        painter.drawPixmap(rect,pix)
if __name__ == '__main__':
    app=QApplication(sys.argv)
    window = SetCursor()
    window.show()    
    sys.exit(app.exec())
