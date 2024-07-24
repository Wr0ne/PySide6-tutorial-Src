import sys,os  #Demo3_12.py
from PySide6.QtWidgets import (QApplication,QPlainTextEdit,QLabel,QMainWindow,
QDockWidget,QMdiArea,QMdiSubWindow,QSlider,QFontComboBox,QComboBox,
QVBoxLayout,QWidget,QFileDialog)
from PySide6.QtGui import QIcon,QColor,QPalette
from PySide6.QtCore import Qt

class MySubWindow(QMdiSubWindow):  #建立子窗口类
    def __init__(self,parent=None):
        super().__init__(parent)
        self.plainText = QPlainTextEdit(self)
        self.setWidget(self.plainText)  #在子窗口上添加控件
        self.setOption(QMdiSubWindow.RubberBandResize)
class MyMdiWindow(QMainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setWindowTitle("MdiMainWindow")
        self.setupUi()
        self.subNewWindow_count=0  #用于记录新建窗口的数量
    def setupUi(self):
        self.mdiArea = QMdiArea(self)  #创建多文档区
        self.mdiArea.setTabsClosable(True)
        self.setCentralWidget(self.mdiArea)  #将多文档区设置成中心控件
        menuBar = self.menuBar()  #创建菜单栏
        file_menu = menuBar.addMenu("文件(&F)")  #创建菜单
        self.act_new = file_menu.addAction(QIcon("D:\\python\\new.png"),"新建(&N)")
        self.act_open = file_menu.addAction(QIcon("D:\\python\\open.png"), "打开(&O)")
        self.act_save = file_menu.addAction(QIcon("D:\\python\\save.png"), "保存(&S)")
        self.act_saveAs=file_menu.addAction(QIcon("D:\\python\\saveAs.png"),"另存为(&A)")
        self.act_exit = file_menu.addAction(QIcon("D:\\python\\exit.png"), "退出(&T)")
        edit_menu = menuBar.addMenu("编辑(&E)")  #创建菜单
        self.act_copy = edit_menu.addAction(QIcon("D:\\python\\copy.png"),"复制(&C)")
        self.act_paste = edit_menu.addAction(QIcon("D:\\python\\paste.png"), "粘贴(&V)")
        self.act_cut = edit_menu.addAction(QIcon("D:\\python\\cut.png"), "剪切(&X)")
        window_menu = menuBar.addMenu("窗口(&W)")  #创建菜单
        self.act_subWindowView = window_menu.addAction("子窗口形式(&S)")
        self.act_tabWindowView = window_menu.addAction("Tab窗口形式(&T)")
        window_menu.addSeparator()
        self.act_cascade = window_menu.addAction("层叠窗口")
        self.act_tile = window_menu.addAction("平铺窗口")

        file_toolBar = self.addToolBar("文件")  #创建工具栏
        file_toolBar.addAction(self.act_new)  #工具栏上添加动作
        file_toolBar.addAction(self.act_open)  #工具栏上添加动作
        file_toolBar.addAction(self.act_save)  #工具栏上添加动作
        file_toolBar.addAction(self.act_saveAs)  # 工具栏上添加动作
        edit_toolBar = self.addToolBar("编辑")  #创建工具栏
        edit_toolBar.addAction(self.act_copy)  #工具栏上添加动作
        edit_toolBar.addAction(self.act_paste)  #工具栏上添加动作
        edit_toolBar.addAction(self.act_cut)  #工具栏上添加动作

        self.statusBar = self.statusBar()  #创建状态栏
        label = QLabel("版本号:1.0")
        self.statusBar.addPermanentWidget(label)

        self.dock_font = QDockWidget("字体",self)  #创建停靠控件
        self.addDockWidget(Qt.LeftDockWidgetArea,self.dock_font) #主窗口添加停靠控件
        fw = QWidget()  #创建悬停控件上的控件
        self.dock_font.setWidget(fw)  #设置悬停控件上的控件
        fv = QVBoxLayout(fw)  #在控件上添加布局

        self.fontComboBox=QFontComboBox()
        self.fontComboBox.setMaximumWidth(100)
        self.sizeComboBox=QComboBox()
        for i in range(5,50):
            self.sizeComboBox.addItem(str(i))
        fv.addWidget(self.fontComboBox)  #布局中添加控件
        fv.addWidget(self.sizeComboBox)  #布局中添加控件

        self.dock_color = QDockWidget("颜色",self)  #创建悬停控件
        self.addDockWidget(Qt.LeftDockWidgetArea,self.dock_color)#添加悬停控件
        self.dock_color.setFeatures(QDockWidget.NoDockWidgetFeatures) #设置特征
        self.tabifyDockWidget(self.dock_font,self.dock_color) #把两个悬停层叠

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
        self.act_new.triggered.connect(self.act_new_triggered) #信号与槽的关联
        self.act_open.triggered.connect(self.act_open_triggered) #信号与槽的关联
        self.act_save.triggered.connect(self.act_save_triggered) #信号与槽的关联
        self.act_saveAs.triggered.connect(self.act_saveAs_triggered) #信号与槽的关联
        self.act_subWindowView.triggered.connect(self.act_subWindowView_triggered)
        self.act_tabWindowView.triggered.connect(self.act_tabWindowView_triggered)
        self.act_cascade.triggered.connect(self.mdiArea.cascadeSubWindows)
        self.act_tile.triggered.connect(self.mdiArea.tileSubWindows) #信号与槽关联
        self.mdiArea.subWindowActivated.connect(self.mdiArea_subWindow_activated)
    def mdiArea_subWindow_activated(self):  #自定义子窗口激活槽函数
        font=self.mdiArea.currentSubWindow().plainText.font()
        self.sizeComboBox.setCurrentText(str(font.pointSize()))
        self.fontComboBox.setCurrentText(font.family())
        # 信号与槽的连接
        self.act_copy.triggered.connect(self.mdiArea.currentSubWindow().plainText.copy)
        self.act_cut.triggered.connect(self.mdiArea.currentSubWindow().plainText.cut)
        self.act_paste.triggered.connect(self.mdiArea.currentSubWindow().plainText.paste)
        self.fontComboBox.currentTextChanged.connect(self.font_name_changed)
        self.sizeComboBox.currentTextChanged.connect(self.font_size_changed)
        self.red_slider.valueChanged.connect(self.color_slider_changed)
        self.green_slider.valueChanged.connect(self.color_slider_changed)
        self.blue_slider.valueChanged.connect(self.color_slider_changed)
    def font_name_changed(self,name):  #自定义滑块槽函数
        if self.mdiArea.currentSubWindow() != None:
            font = self.mdiArea.currentSubWindow().plainText.font()
            font.setFamily(name)
            self.mdiArea.currentSubWindow().plainText.setFont(font)
    def font_size_changed(self,size):  #自定义滑块槽函数
        if self.mdiArea.currentSubWindow() != None:
            font = self.mdiArea.currentSubWindow().plainText.font()
            font.setPointSize(int(size))
            self.mdiArea.currentSubWindow().plainText.setFont(font)
    def color_slider_changed(self,value):  #自定义滑块槽函数
        if self.mdiArea.currentSubWindow() != None:
            color = QColor(self.red_slider.value(), self.green_slider.value(),
self.blue_slider.value())
            palette = self.mdiArea.currentSubWindow().plainText.palette()
            palette.setColor(QPalette.Text,color)
            self.mdiArea.currentSubWindow().plainText.setPalette(palette)
    def act_new_triggered(self):  #自定义新建文档槽函数
        subWindow = MySubWindow()   #创建子窗口
        self.mdiArea.addSubWindow(subWindow)
        subWindow.show()
        self.subNewWindow_count=self.subNewWindow_count+1
        subWindow.setWindowTitle("新建文档"+str(self.subNewWindow_count))
        self.fontComboBox.setCurrentText("宋体")
        self.sizeComboBox.setCurrentText("15")
        self.statusBar.showMessage("当前文档："+
self.mdiArea.currentSubWindow().windowTitle())
    def act_open_triggered(self):  #自定义打开文档槽函数
        filename,filter = QFileDialog.getOpenFileName(self,"打开文件","d:\\","文本(*.txt)")
        if os.path.exists(filename):
            try:
                fp = open(filename,"r",encoding="UTF-8")
                string = fp.readlines()
                if len(self.mdiArea.subWindowList())==0:
                    currentSub=self.mdiArea.addSubWindow(MySubWindow()) #子窗口
                else:
                    if self.mdiArea.currentSubWindow().plainText.toPlainText()=="":
                        currentSub=self.mdiArea.currentSubWindow()
                    else:
                        currentSub = self.mdiArea.addSubWindow(MySubWindow())
                for i in string:
                    currentSub.plainText.appendPlainText(i)
                currentSub.show()
                currentSub.setWindowTitle(os.path.basename(filename))
                currentSub.setWindowFilePath(filename)
                fp.close()
                self.statusBar.showMessage("当前文档："+
self.mdiArea.currentSubWindow().windowTitle())
            except:
                self.statusBar.showMessage("打开文件出错，选择“UTF-8”编码文件")
    def act_save_triggered(self):  #自定义存盘槽函数
        if self.mdiArea.currentSubWindow() != None:
            currentSub = self.mdiArea.currentSubWindow()
            string = currentSub.plainText.toPlainText()
            if currentSub.windowFilePath() != "":
                fp = open(currentSub.windowFilePath(), "w", encoding="UTF-8")
                fp.writelines(string)
                fp.close()
                return
            self.act_saveAs_triggered()
            self.statusBar.showMessage("当前文档："+
                                   self.mdiArea.currentSubWindow().windowTitle())
    def act_saveAs_triggered(self):  #自定义另存为槽函数
        if self.mdiArea.currentSubWindow() != None:
            filename, filter = QFileDialog.getSaveFileName(self, "保存文件","d:\\", 
"文本文件(*.txt)")
            currentSub = self.mdiArea.currentSubWindow()
            string = currentSub.plainText.toPlainText()
            if filename != "":
                fp = open(filename, "w", encoding="UTF-8")
                fp.writelines(string)
                fp.close()
                currentSub.setWindowTitle(os.path.basename(filename))
                currentSub.setWindowFilePath(filename)
                self.statusBar.showMessage("当前文档：" +
                     self.mdiArea.currentSubWindow().windowTitle())
    def act_subWindowView_triggered(self):  #自定义子窗口样式显示槽函数
        self.mdiArea.setViewMode(QMdiArea.SubWindowView)
        self.act_cascade.setEnabled(True)
        self.act_tile.setEnabled(True)
    def act_tabWindowView_triggered(self):  #自定义Tab显示槽函数
        self.mdiArea.setViewMode(QMdiArea.TabbedView)
        self.act_cascade.setEnabled(False)
        self.act_tile.setEnabled(False)
if __name__ == '__main__':
    app=QApplication(sys.argv)
    window = MyMdiWindow()
    window.show()
    sys.exit(app.exec())
