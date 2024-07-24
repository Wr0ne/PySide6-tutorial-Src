import sys   #Demo5_8.py
from PySide6.QtWidgets import QApplication,QWidget,QListView,QHBoxLayout
from PySide6.QtCore import QStringListModel

class MyWindow(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setupUi()
    def setupUi(self):
        self.listModel=QStringListModel(self) #数据模型
        self.listModel.setStringList(['语文','数学','物理','化学'])  #数据模型中添加数据

        self.listView1 = QListView()   #视图控件
        self.listView2 = QListView()   #视图控件

        self.listView1.setModel(self.listModel)  #给视图控件设置数据模型
        self.listView2.setModel(self.listModel)  #给视图控件设置数据模型
        h=QHBoxLayout(self)  #水平布局
        h.addWidget(self.listView1)
        h.addWidget(self.listView2)
if __name__ == '__main__':
    app=QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
