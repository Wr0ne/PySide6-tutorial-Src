import sys  #Demo3_5.py
from PySide6.QtWidgets import (QApplication,QMenuBar,QPlainTextEdit,
                       QVBoxLayout,QWidget,QFileDialog,QMessageBox)
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt

class MyWindow(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setWindowTitle("QMenu应用实例")
        self.setupUi()
    def setupUi(self):
        self.menuBar = QMenuBar()   #创建菜单栏
        self.plainText = QPlainTextEdit() #创建多行纯文本控件
        self.plainText.setContextMenuPolicy(Qt.CustomContextMenu) #设置自定义快捷菜单
        vlayout = QVBoxLayout(self)   #创建竖直布局
        vlayout.addWidget(self.menuBar)
        vlayout.addWidget(self.plainText)

        self.menuFile = self.menuBar.addMenu('文件(&F)')  #创建文件菜单
        self.actNew=self.menuFile.addAction(QIcon("d:\\python\\new.png"),'新建(&N)') 
        self.actOpen=self.menuFile.addAction(QIcon("d:\\python\\open.png"),'打开(&O)') 
        self.menuFile.addSeparator()  #菜单中添加分隔条
        self.actQuit=self.menuFile.addAction(QIcon("d:\\python\\exit.png"),'退出(&Q)') 

        self.menuEdit = self.menuBar.addMenu('编辑(&E)')  #创建编辑菜单
        self.menuEdit.setTearOffEnabled(True)        #将编辑菜单设置成可撕扯菜单
        self.actCopy = self.menuEdit.addAction('复制(&C)')  #菜单中添加动作
        self.actCut = self.menuEdit.addAction('剪切(&X)')   #菜单中添加动作
        self.actPaste = self.menuEdit.addAction('粘贴(&V)')  #菜单中添加动作
        self.actCopy.setEnabled(False)
        self.actCut.setEnabled(False)
        self.actPaste.setEnabled(False)

        self.menuFile.triggered.connect(self.menuFile_triggered) #信号与槽函数连接
        self.menuFile.hovered.connect(self.menuFile_hovered)  #信号与槽函数连接
        self.menuEdit.triggered.connect(self.menuEdit_triggered) #编信号与槽函数连接
        self.plainText.copyAvailable.connect(self.plainText_copyAvailable)#信号与槽函数连接
        self.plainText.customContextMenuRequested.connect(self.plainText_contextMenu)
    def menuFile_triggered(self, action):  #文件菜单的槽函数
        if action == self.actNew:  #新建动作
            self.plainText.clear()
        elif action == self.actOpen:  #打开动作
            filename,filter=QFileDialog.getOpenFileName(self,"打开","d:\\","文本文件(*.txt)")
            try:
                fp = open(filename, "r", encoding="UTF-8")
                string = fp.readlines()
                self.plainText.clear()
                for i in string:
                    i = i.strip()
                    self.plainText.appendPlainText(i)
                fp.close()
            except:
                QMessageBox.critical(self,"打开文件失败","请选择合适的文件！")
        elif action == self.actQuit:  #退出动作
            self.close()
    def menuFile_hovered(self,action):  #文件菜单的槽函数
        self.menuFile.setDefaultAction(action)
    def plainText_copyAvailable(self, available):   #纯文本控件的槽函数
        self.actCopy.setEnabled(available)
        self.actCut.setEnabled(available)
    def menuEdit_triggered(self, action):   #编辑菜单的槽函数
        if action == self.actCopy:   #复制动作
            self.plainText.copy()
            self.actPaste.setEnabled(True)
        elif action == self.actCut:   #剪切动作
            self.plainText.cut()
            self.actPaste.setEnabled(True)
        elif action == self.actPaste:  #粘贴动作
            self.plainText.paste()
            self.actPaste.setEnabled(False)
    def plainText_contextMenu(self,point):  #纯文本控件的快捷菜单槽函数
        point = self.plainText.mapToGlobal(point)  #将坐标映射成屏幕坐标系下的坐标
        self.menuEdit.popup(point)  #弹出菜单
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
