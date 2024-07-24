import sys,os  #Demo3_10.py
from PySide6.QtWidgets import (QApplication,QPlainTextEdit,QLabel, QToolBar,
            QVBoxLayout,QWidget,QFileDialog,QStatusBar)
from PySide6.QtGui import QIcon

class MyWindow(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setWindowTitle("QStatusBar and QToolBar")
        self.setupUi()
    def setupUi(self):
        toolBar = QToolBar()            #创建工具栏
        self.plainText = QPlainTextEdit()  #创建文本编辑器
        self.statusBar = QStatusBar(self)   #创建状态栏
        vlayout = QVBoxLayout(self)     #创建竖直布局
        vlayout.addWidget(toolBar)
        vlayout.addWidget(self.plainText)
        vlayout.addWidget(self.statusBar)
        #工具栏上添加动作
        act_new = toolBar.addAction(QIcon("D:\\python\\new.png"),"新建(&N)")  #添加动作
        act_open= toolBar.addAction(QIcon("D:\\python\\open.png"), "打开(&O)")  #添加动作
        act_save = toolBar.addAction(QIcon("D:\\python\\save.png"), "保存(&S)")  #添加动作
        toolBar.addSeparator()  #分隔条
        act_copy = toolBar.addAction(QIcon("D:\\python\\copy.png"),"复制(&C)")  #添加动作
        act_paste = toolBar.addAction(QIcon("D:\\python\\paste.png"), "粘贴(&V)")  #添加动作
        act_cut = toolBar.addAction(QIcon("D:\\python\\cut.png"), "剪切(&X)")  #添加动作

        act_new.triggered.connect(self.act_new_triggered)   #信号与自定义槽的关联
        act_open.triggered.connect(self.act_open_triggered)  #信号与自定义槽的关联
        act_save.triggered.connect(self.act_save_triggered)   #信号与自定义槽的关联
        act_copy.triggered.connect(self.plainText.copy)      #信号与控件的槽的关联
        act_cut.triggered.connect(self.plainText.cut)         #信号与控件的槽的关联
        act_paste.triggered.connect(self.plainText.paste)      #信号与控件的槽的关联
        act_new.hovered.connect(self.act_new_hovered)     #信号与控件的槽的关联
        act_open.hovered.connect(self.act_open_hovered)    #信号与控件的槽的关联
        act_save.hovered.connect(self.act_save_hovered)    #信号与控件的槽的关联
        act_copy.hovered.connect(self.act_copy_hovered)    #信号与控件的槽的关联
        act_paste.hovered.connect(self.act_paste_hovered)    #信号与控件的槽的关联
        act_cut.hovered.connect(self.act_cut_hovered)  #信号与控件的槽的关联

        label = QLabel("版本号:1.0",self)
        self.statusBar.addPermanentWidget(label)
    def act_new_triggered(self):  #自定义槽函数
        self.plainText.clear()
    def act_open_triggered(self):  #自定义槽函数
        filename,filter = QFileDialog.getOpenFileName(self,"打开文件","d:\\","文本文件(*.txt)")
        if os.path.exists(filename):
            self.plainText.clear()
            fp = open(filename,"r",encoding="UTF-8")
            string = fp.readlines()
            for i in string:
                i = i.strip()
                self.plainText.appendPlainText(i)
            fp.close()
    def act_save_triggered(self):  #自定义槽函数
        filename,filter = QFileDialog.getSaveFileName(self,"打开文件","d:\\","文本文件(*.txt)")
        string = self.plainText.toPlainText()
        if filename != "":
            if os.path.exists(filename):
                fp=open(filename,"wa",encoding="UTF-8")
                fp.writelines(string)
                fp.close()
            else:
                fp = open(filename, "w", encoding="UTF-8")
                fp.writelines(string)
                fp.close()
    def act_new_hovered(self):  #自定义槽函数
        self.statusBar.showMessage("新建文档",5000)
    def act_open_hovered(self):  #自定义槽函数
        self.statusBar.showMessage("打开文档",5000)
    def act_save_hovered(self):  #自定义槽函数
        self.statusBar.showMessage("保存文档",5000)
    def act_copy_hovered(self):  #自定义槽函数
        self.statusBar.showMessage("复制选中的内容",5000)
    def act_paste_hovered(self):  #自定义槽函数
        self.statusBar.showMessage("在光标位置处粘贴",5000)
    def act_cut_hovered(self):   #自定义槽函数
        self.statusBar.showMessage("剪切选中的内容",5000)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
