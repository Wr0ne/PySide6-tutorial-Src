import sys,os  #Demo3_4.py
from PySide6.QtWidgets import (QApplication,QMenuBar,QPlainTextEdit,
                        QVBoxLayout,QWidget,QFileDialog,QMessageBox)
class MyWindow(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setWindowTitle("QMenuBar应用实例")
        self.setupUi()
    def setupUi(self):
        self.menuBar = QMenuBar()  #创建菜单栏
        self.plainText = QPlainTextEdit() #创建文本编辑器
        vlayout = QVBoxLayout(self)  #创建竖直布局
        vlayout.addWidget(self.menuBar)
        vlayout.addWidget(self.plainText)

        self.fileMenu = self.menuBar.addMenu('文件(&F)') #菜单栏中添加菜单
        self.editMenu = self.menuBar.addMenu('编辑(&E)') #菜单栏中添加菜单
        self.menuBar.addSeparator()  #菜单栏中添加分隔条
        self.actNew = self.menuBar.addAction('新建(&N)') #菜单栏中添加动作
        self.actOpen = self.menuBar.addAction('打开(&O)') #菜单栏中添加动作
        self.actQuit = self.menuBar.addAction('退出(&Q)') #菜单栏中添加动作

        self.menuBar.triggered.connect(self.action_triggered) #菜单栏信号与槽函数的连接
    def action_triggered(self,action):  #菜单栏的槽函数
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
                QMessageBox.critical(self, "打开文件失败", "请选择合适的文件！")
        elif action == self.actQuit:  #退出动作
            self.close()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
