import sys,os   #Demo3_9.py
from PySide6.QtWidgets import (QApplication,QMenuBar,QPlainTextEdit,QComboBox,
            QFontComboBox,QToolBar,QVBoxLayout,QWidget,QFileDialog,QToolButton)
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt
class MyWindow(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setWindowTitle("QMenu and QToolBar")
        self.setupUi()
    def setupUi(self):
        menuBar = QMenuBar()  #创建菜单栏
        toolBar = QToolBar()  #创建工具栏
        toolBar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon) #设置工具栏上按钮的样式
        self.plainText = QPlainTextEdit() #创建文本编辑器
        vlayout = QVBoxLayout(self)  #创建竖直布局
        vlayout.addWidget(menuBar)
        vlayout.addWidget(toolBar)
        vlayout.addWidget(self.plainText)
        #工具栏上添加动作
        act_new = toolBar.addAction(QIcon("D:\\python\\new.png"),"新建(&N)")  #添加动作
        act_open= toolBar.addAction(QIcon("D:\\python\\open.png"), "打开(&O)")  #添加动作
        act_save = toolBar.addAction(QIcon("D:\\python\\save.png"), "保存(&S)")  #添加动作
        toolBar.addSeparator()  #分隔条
        act_copy = toolBar.addAction(QIcon("D:\\python\\copy.png"),"复制(&C)") #添加动作
        act_paste = toolBar.addAction(QIcon("D:\\python\\paste.png"), "粘贴(&V)") #添加动作
        act_cut = toolBar.addAction(QIcon("D:\\python\\cut.png"), "剪切(&X)")  #添加动作
        toolBar.addSeparator()  #分隔条

        self.fontComboBox = QFontComboBox(self)  #字体下拉列表
        self.fontComboBox.setFixedWidth(100)
        toolBar.addWidget(self.fontComboBox)  #工具栏上添加字体下拉列表
        self.plainText.setFont(self.fontComboBox.currentFont())  #设置字体
        self.fontComboBox.currentFontChanged.connect(self.plainText.setFont) #信号与槽连接

        self.comboBox = QComboBox(self)  #下拉列表
        for i in range(5,50):
            self.comboBox.addItem(str(i))
        self.comboBox.setCurrentText("15")
        toolBar.addWidget(self.comboBox) #工具栏上添加下拉列表
        self.comboBox.currentTextChanged.connect(self.comboBox_text_changed) #信号与槽连接

        menu_file = menuBar.addMenu("文件(&F)")  #菜单栏中添加菜单
        menu_file.addAction(act_new)  #菜单中添加动作
        menu_file.addAction(act_open)  #菜单中添加动作
        menu_file.addAction(act_save)  #菜单中添加动作
        menu_file.addSeparator()  #菜单中添加分隔条
        act_exit = menu_file.addAction(QIcon("D:\\python\\exit.png"), "退出(&E)") #添加动作

        menu_edit = menuBar.addMenu("编辑(&E)")  #菜单栏中添加菜单
        menu_edit.addAction(act_copy)  #菜单中添加动作
        menu_edit.addAction(act_paste)  #菜单中添加动作
        menu_edit.addAction(act_cut)  #菜单中添加动作

        act_new.triggered.connect(self.act_new_triggered)  #信号与自定义槽的连接
        act_open.triggered.connect(self.act_open_triggered) #信号与自定义槽的连接
        act_save.triggered.connect(self.act_save_triggered) #信号与自定义槽的连接
        act_exit.triggered.connect(self.close)  #信号与窗口槽的连接
        act_copy.triggered.connect(self.plainText.copy)  #信号与控件的槽的连接
        act_cut.triggered.connect(self.plainText.cut)  #信号与控件的槽的连接
        act_paste.triggered.connect(self.plainText.paste) #信号与控件的槽的连接

        toolButton = QToolButton(self)  #工具按钮
        toolButton.setMenu(menu_file)  #为工具按钮添加菜单
        toolButton.setArrowType(Qt.DownArrow)
        toolButton.setPopupMode(QToolButton.InstantPopup) #设置工具按钮的样式
        toolBar.addWidget(toolButton)  #工具栏中添加工具按钮
    def comboBox_text_changed(self,text): #下拉列表的槽函数
        font  = self.plainText.font()
        font.setPointSize(int(text))
        self.plainText.setFont(font)
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
        self.comboBox_text_changed(self.comboBox.currentText())
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
if __name__ == '__main__':
    app=QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
