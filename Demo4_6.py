import sys  #Demo4_6.py
from PySide6.QtWidgets import QApplication,QWidget,QFileDialog,QMenu
from PySide6.QtGui import QPixmap,QPainter

class MyWindow(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True) #设置可接受拖放事件
        self.resize(600,400)
        self.pixmap = QPixmap()  #创建QPixmap图像
    def contextMenuEvent(self,event) :
        contextMenu = QMenu(self)
        contextMenu.addAction("打开(&O)").triggered.connect(self.actionOpen_triggered) #槽连接
        contextMenu.addSeparator()
        contextMenu.addAction("退出(&E)").triggered.connect(self.close)  # 动作与槽连接
        contextMenu.exec(event.globalPos())
    def paintEvent(self,event): #窗口绘制处理函数，当窗口刷新时调用该函数
        painter = QPainter(self)  # 绘图
        painter.drawPixmap(self.rect(),self.pixmap)
    def mouseDoubleClickEvent(self, event): #双击鼠标事件的处理函数
        self.actionOpen_triggered()
    def actionOpen_triggered(self):  #打开文件的动作
        fileDialog = QFileDialog(self)
        fileDialog.setNameFilter("图像文件(*.png *.jpeg *.jpg)")
        fileDialog.setFileMode(QFileDialog.ExistingFile)
        if fileDialog.exec():
            self.pixmap.load(fileDialog.selectedFiles()[0])
            self.update()
if __name__ == '__main__':
    app=QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
