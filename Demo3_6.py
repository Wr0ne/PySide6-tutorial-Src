import sys  #Demo3_6.py
from PySide6.QtWidgets import (QApplication,QMenuBar,QMenu,QPlainTextEdit,
                             QVBoxLayout,QWidget,QFileDialog,QMessageBox)
from PySide6.QtGui import QIcon,QAction,QActionGroup
class MyWindow(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setWindowTitle("QAction应用实例")
        self.setupUi()
    def setupUi(self):
        menuBar = QMenuBar()  #创建菜单栏
        self.plainText = QPlainTextEdit() #创建文本编辑器
        font = self.plainText.font()
        font.setFamily('宋体')
        font.setPointSize(15)
        self.plainText.setFont(font)
        vlayout = QVBoxLayout(self)  #创建竖直布局
        vlayout.addWidget(menuBar)
        vlayout.addWidget(self.plainText)

        self.actNew=QAction(QIcon("d:\\python\\new.png"),"新建(&N)",self) #创建动作
        self.actOpen=QAction(QIcon("d:\\python\\open.png"),"打开(&O)",self) #创建动作
        self.actQuit=QAction(QIcon("d:\\python\\exit.png"),"退出(&Q)",self) #创建动作
        self.actNew.setShortcut("Ctrl+N")   #定义快捷键
        self.actOpen.setShortcut("Ctrl+O")  #定义快捷键
        self.actQuit.setShortcut("Ctrl+Q")   #定义快捷键

        menuFile = QMenu("文件(&F)",self)  #创建菜单
        menuBar.addMenu(menuFile)      #菜单栏中添加菜单
        menuFile.addAction(self.actNew)    #菜单中添加动作
        menuFile.addAction(self.actOpen)   #菜单中添加动作
        menuFile.addSeparator()           #菜单中添加分隔条
        menuFile.addAction(self.actQuit)    #菜单中添加动作

        menuFont = menuBar.addMenu("字体(&T)")  #菜单栏中添加菜单
        self.actSong = menuFont.addAction("宋体")  #菜单中添加动作
        self.actHei = menuFont.addAction("黑体")   #菜单中添加动作
        self.actHua = menuFont.addAction("幼圆")   #菜单中添加动作
        self.actSong.setCheckable(True)   #将动作设置成可勾选
        self.actSong.setChecked(True)     #将动作设置成可勾选
        self.actHei.setCheckable(True)    #将动作设置成可勾选
        self.actHua.setCheckable(True)    #将动作设置成可勾选

        group = QActionGroup(self)    #建立动作组
        group.setExclusive(True)      #设置动作组内的动作具有互斥性
        group.addAction(self.actSong)  #动作组内添加动作 
        group.addAction(self.actHei)
        group.addAction(self.actHua)
        menuFont.addSeparator()

        self.actBold = menuFont.addAction("粗体")    #菜单中添加动作
        self.actItalic = menuFont.addAction("斜体")    #菜单中添加动作
        self.actUnderLine = menuFont.addAction("下划线")  #菜单中添加动作
        self.actBold.setCheckable(True)       #将动作设置成可勾选
        self.actItalic.setCheckable(True)       #将动作设置成可勾选
        self.actUnderLine.setCheckable(True)   #将动作设置成可勾选

        self.actNew.triggered.connect(self.actNew_triggered) #信号与槽函数的连接
        self.actOpen.triggered.connect(self.actOpen_triggered)
        self.actQuit.triggered.connect(self.actQuit_triggered)
        self.actSong.triggered.connect(self.actSong_triggered)
        self.actHei.triggered.connect(self.actHei_triggered)
        self.actHua.triggered.connect(self.actHua_triggered)
        self.actBold.toggled.connect(self.actBold_toggled)
        self.actItalic.toggled.connect(self.actItalic_toggled)
        self.actUnderLine.toggled.connect(self.actUnderLine_toggled)
    def actNew_triggered(self):    #动作的槽函数
        self.plainText.clear()
    def actOpen_triggered(self):   #动作的槽函数
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
    def actQuit_triggered(self):   #动作的槽函数
        self.close()
    def actSong_triggered(self):
        font = self.plainText.font();font.setFamily('宋体')
        self.plainText.setFont(font)
    def actHei_triggered(self):   #动作的槽函数
        font = self.plainText.font();font.setFamily('黑体')
        self.plainText.setFont(font)
    def actHua_triggered(self):    #动作的槽函数
        font = self.plainText.font();font.setFamily('华文彩云')
        self.plainText.setFont(font)
    def actBold_toggled(self,checked):    #动作的槽函数
        font = self.plainText.font();font.setBold(checked)
        self.plainText.setFont(font)
    def actItalic_toggled(self,checked):   #动作的槽函数
        font = self.plainText.font();font.setItalic(checked)
        self.plainText.setFont(font)
    def actUnderLine_toggled(self,checked): #动作的槽函数
        font = self.plainText.font();font.setUnderline(checked)
        self.plainText.setFont(font)
if __name__ == '__main__':
    app=QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
