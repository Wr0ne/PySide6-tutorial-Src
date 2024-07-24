import sys,os  #Demo3_11.py
from PySide6.QtWidgets import (QApplication,QPlainTextEdit,QLabel,QMainWindow,QDockWidget,
                   QSlider,QFontComboBox,QComboBox,QVBoxLayout,QWidget,QFileDialog)
from PySide6.QtGui import QIcon,QColor,QPalette
from PySide6.QtCore import Qt

class MyWindow(QMainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setWindowTitle("QMainWindow")
        self.setupUi()
    def setupUi(self):
        self.plainText = QPlainTextEdit(self)
        self.setCentralWidget(self.plainText)  #设置中心控件
        menuBar = self.menuBar()  #创建菜单栏
        file_menu = menuBar.addMenu("文件(&F)")  #创建菜单
        act_new = file_menu.addAction(QIcon("D:\\python\\new.png"),"新建(&N)") #添加动作
        act_open = file_menu.addAction(QIcon("D:\\python\\open.png"), "打开(&O)") #添加动作
        act_save = file_menu.addAction(QIcon("D:\\python\\save.png"), "保存(&S)") #添加动作
        file_menu.addSeparator()
        act_exit = file_menu.addAction(QIcon("D:\\python\\exit.png"), "退出(&T)") #添加动作
        edit_menu = menuBar.addMenu("编辑(&E)")  #创建菜单
        act_copy = edit_menu.addAction(QIcon("D:\\python\\copy.png"),"复制(&C)") #添加动作
        act_paste = edit_menu.addAction(QIcon("D:\\python\\paste.png"), "粘贴(&V)") #添加动作
        act_cut = edit_menu.addAction(QIcon("D:\\python\\cut.png"), "剪切(&X)") #添加动作

        file_toolBar = self.addToolBar("文件")  #创建工具栏
        file_toolBar.addAction(act_new)  #工具栏上添加动作
        file_toolBar.addAction(act_open)  #工具栏上添加动作
        file_toolBar.addAction(act_save)  #工具栏上添加动作
        file_toolBar.addSeparator()
        file_toolBar.addAction(act_exit)  #工具栏上添加动作
        self.addToolBarBreak(Qt.TopToolBarArea)  #添加断点
        edit_toolBar = self.addToolBar("编辑")  #创建工具栏
        edit_toolBar.addAction(act_copy)  #工具栏上添加动作
        edit_toolBar.addAction(act_paste)  #工具栏上添加动作
        edit_toolBar.addAction(act_cut)  #工具栏上添加动作

        self.statusBar = self.statusBar()  #创建状态栏
        label = QLabel("版本号:1.0")
        self.statusBar.addPermanentWidget(label)

        act_new.triggered.connect(self.act_new_triggered)  #信号与自定义槽的关联
        act_open.triggered.connect(self.act_open_triggered)  #信号与自定义槽的关联
        act_save.triggered.connect(self.act_save_triggered)  #信号与自定义槽的关联
        act_copy.triggered.connect(self.plainText.copy)  #信号与控件的槽的关联
        act_cut.triggered.connect(self.plainText.cut)  #信号与控件的槽的关联
        act_paste.triggered.connect(self.plainText.paste)  #信号与控件的槽的关联
        act_new.hovered.connect(self.act_new_hovered)  #信号与控件的槽的关联
        act_open.hovered.connect(self.act_open_hovered)  #信号与控件的槽的关联
        act_save.hovered.connect(self.act_save_hovered)  #信号与控件的槽的关联
        act_copy.hovered.connect(self.act_copy_hovered)  #信号与控件的槽的关联
        act_paste.hovered.connect(self.act_paste_hovered)  #信号与控件的槽的关联
        act_cut.hovered.connect(self.act_cut_hovered)  #信号与控件的槽的关联

        self.dock_font = QDockWidget("字体",self)  #创建停靠控件
        self.addDockWidget(Qt.LeftDockWidgetArea,self.dock_font)  #主窗口中添加停靠控件
        self.dock_font.setFeatures(QDockWidget.NoDockWidgetFeatures)  #设置停靠控件的特征
        self.dock_font.setFeatures(QDockWidget.DockWidgetFloatable |
             QDockWidget.DockWidgetMovable | QDockWidget.DockWidgetFloatable)
        fw = QWidget()  #创建悬停控件上的控件
        self.dock_font.setWidget(fw)  #设置悬停控件上的控件
        fv = QVBoxLayout(fw)  #在控件上添加布局

        self.fontComboBox=QFontComboBox()
        self.sizeComboBox=QComboBox()
        for i in range(5,50):
            self.sizeComboBox.addItem(str(i))
        self.sizeComboBox.setCurrentText(str(self.plainText.font().pointSize()))
        fv.addWidget(self.fontComboBox)  #布局中添加控件
        fv.addWidget(self.sizeComboBox)  #布局中添加控件

        self.fontComboBox.currentTextChanged.connect(self.font_name_changed) #信号与槽的连接
        self.sizeComboBox.currentTextChanged.connect(self.font_size_changed)  #信号与槽的连接

        self.dock_color = QDockWidget("颜色",self)  #创建悬停控件
        self.addDockWidget(Qt.LeftDockWidgetArea,self.dock_color)  #主窗口中添加悬停控件
        self.dock_color.setFeatures(QDockWidget.NoDockWidgetFeatures) #设置悬停控件的特征
        self.dock_color.setFeatures(QDockWidget.DockWidgetFloatable |
             QDockWidget.DockWidgetMovable | QDockWidget.DockWidgetFloatable)
        self.tabifyDockWidget(self.dock_font,self.dock_color)  #把两个悬停层叠

        self.red_slider = QSlider(Qt.Horizontal)
        self.green_slider = QSlider(Qt.Horizontal)
        self.blue_slider = QSlider(Qt.Horizontal)
        self.red_slider.setRange(0,255)
        self.green_slider.setRange(0,255)
        self.blue_slider.setRange(0,255)
        cw=QWidget()  #创建悬停控件上的控件
        self.dock_color.setWidget(cw)  #设置悬停控件上的控件
        cv = QVBoxLayout(cw)
        cv.addWidget(self.red_slider)
        cv.addWidget(self.green_slider)
        cv.addWidget(self.blue_slider)
        self.red_slider.valueChanged.connect(self.color_slider_changed)  #信号与槽的连接
        self.green_slider.valueChanged.connect(self.color_slider_changed)  #信号与槽的连接
        self.blue_slider.valueChanged.connect(self.color_slider_changed)  #信号与槽的连接

        self.setAnimated(True)
        self.setCorner(Qt.TopLeftCorner,Qt.LeftDockWidgetArea)
        self.setDockNestingEnabled(True)
    def font_name_changed(self,name): #自定义槽函数
        font = self.plainText.font()
        font.setFamily(name)
        self.plainText.setFont(font)
    def font_size_changed(self,size): #自定义槽函数
        font = self.plainText.font()
        font.setPointSize(int(size))
        self.plainText.setFont(font)
    def color_slider_changed(self,value): #自定义槽函数
        color = QColor(self.red_slider.value(),self.green_slider.value(),self.blue_slider.value())
        palette = self.plainText.palette()
        palette.setColor(QPalette.Text,color)
        self.plainText.setPalette(palette)
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
        filename,filter = QFileDialog.getSaveFileName(self,"保存文件","d:\\","文本文件(*.txt)")
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
    def act_new_hovered(self): #自定义槽函数
        self.statusBar.showMessage("新建文档",5000)
    def act_open_hovered(self): #自定义槽函数
        self.statusBar.showMessage("打开文档",5000)
    def act_save_hovered(self): #自定义槽函数
        self.statusBar.showMessage("保存文档",5000)
    def act_copy_hovered(self): #自定义槽函数
        self.statusBar.showMessage("复制选中的内容",5000)
    def act_paste_hovered(self): #自定义槽函数
        self.statusBar.showMessage("在光标位置处粘贴",5000)
    def act_cut_hovered(self): #自定义槽函数
        self.statusBar.showMessage("剪切选中的内容",5000)
if __name__ == '__main__':
    app=QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
