import sys   #Demo5_10.py
from PySide6.QtWidgets import (QApplication,QWidget,QFrame,QSplitter,QListView,
                             QHBoxLayout,QFileSystemModel,QTreeView)
from PySide6.QtGui import QPainter,QPixmap
from PySide6.QtCore import Qt
class MyFrame(QFrame): #为能显示图片，重写QFrame的paintEvent()事件
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFrameShape(self.Box)
        self.resize(600,500)
        self.setFrameShape(QFrame.Box)
        self.__path = ""  #用于记录图片文件
    def setPath(self,path): #获取图片文件
        self.__path = path
    def paintEvent(self, event): # paintEvent()事件
        painter = QPainter(self)
        pixmap = QPixmap(self.__path)
        painter.drawPixmap(self.rect(), pixmap)
        super().paintEvent(event)
class MyWindow(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setWindowTitle("图片浏览器")
        self.resize(800,600)
        self.setup_Ui()
    def setup_Ui(self):
        self.fileSystem = QFileSystemModel(self)  #建立文件系统模型
        rootIndex = self.fileSystem.setRootPath("c:\\")  #设置根路径
        self.treeView = QTreeView()   #建立树视图控件
        self.treeView.setModel(self.fileSystem)  #设置模型
        self.listView = QListView()  #建立列表视图模型
        self.listView.setModel(self.fileSystem)  #设置模型
        self.listView.setRootIndex(rootIndex)  #设置路径
        splitter_h = QSplitter(Qt.Horizontal)  #建立分割器
        splitter_v = QSplitter(Qt.Vertical)  #建立分割器
        splitter_h.addWidget(self.treeView)  #在分割器中添加控件
        splitter_h.addWidget(splitter_v)  #在分割器中添加分割器
        self.frame = MyFrame()  #建立框架控件
        splitter_v.addWidget(self.listView)  #添加控件
        splitter_v.addWidget(self.frame)  #添加控件
        h = QHBoxLayout(self)  #窗口中的布局
        h.addWidget(splitter_h)

        self.treeView.clicked.connect(self.view_clicked)  #信号与槽的连接
        self.listView.clicked.connect(self.view_clicked)  #信号与槽的连接
    def view_clicked(self,index):  #树视图控件或列表视图控件的单击槽函数
        if self.fileSystem.isDir(index):  #如果是文件夹，展开文件
            self.listView.setRootIndex(index)
            self.treeView.expand(index)
            self.treeView.setCurrentIndex(index)
        else:
            self.frame.setPath(self.fileSystem.filePath(index)) #如果是文件，传递文件名
            self.frame.update()  #刷新屏幕，绘制图片
if __name__ == '__main__':
    app=QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
