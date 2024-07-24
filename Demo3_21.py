import sys  #Demo3_21.py
from PySide6.QtWidgets import (QApplication,QWidget,QPushButton,QComboBox,QTextEdit,
QCheckBox,QRadioButton,QVBoxLayout,QHBoxLayout,QMenu,QFileDialog,QMenuBar,QStatusBar)
from PySide6.QtGui import QAction
from PySide6.QtCore import Qt
from qt_material import  apply_stylesheet,list_themes

class MyWindow(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setWindowTitle("样式例子")
        self.resize(500, 400)
        self.setupUi()  #调用函数，建立界面上的控件
        self.pushMenu() #调用函数，为pushButton创建菜单
    def setupUi(self):  #建立界面上的控件
        menuBar = QMenuBar()
        themesMenu = menuBar.addMenu('主题')
        themesMenu.triggered.connect(self.themesMunu_triggered)
        themes = list_themes()  #获取主题列表
        for theme in themes:
            themesMenu.addAction(theme)  #添加动作，主题名称是动作的名称
        self.btn_open = QPushButton("打开文件(&O)")
        self.btn_font = QPushButton("选择字体",self)
        self.btn_font.setShortcut("Ctrl+ALt+F")   #设置按钮的快捷键
        self.checkBox_bold = QCheckBox("粗体(&B)",self)
        self.checkBox_italic = QCheckBox("斜体(&I)",self)
        self.checkBox_underline = QCheckBox("下画线(&U)",self)
        self.radioButton_left = QRadioButton("左对齐(&L)",self)
        self.radioButton_center =QRadioButton("居中(&M)",self)
        self.radioButton_right = QRadioButton("右对齐(&R)",self)
        self.comboBox = QComboBox(self)
        for i in range(4,30,2):
            self.comboBox.addItem(str(i))
        self.comboBox.setEditable(True)
        self.comboBox.setFixedWidth(100)
        self.comboBox.setCurrentText("选择字体尺寸")
        self.plainText = QTextEdit("很高兴认识你，Nice to meet you!",self)

        self.btn_open.clicked.connect(self.btn_open_clicked)  #信号与槽的连接
        self.checkBox_bold.toggled.connect(self.bold)        #信号与槽的连接
        self.checkBox_italic.toggled.connect(self.italic)        #信号与槽的连接
        self.checkBox_underline.toggled.connect(self.underline)  #信号与槽的连接
        self.radioButton_left.toggled.connect(self.left)       #信号与槽的连接
        self.radioButton_center.toggled.connect(self.center)   #信号与槽的连接
        self.radioButton_right.toggled.connect(self.right)      #信号与槽的连接
        self.comboBox.currentTextChanged.connect(self.font_size) #信号与槽的连接

        H = QHBoxLayout()  #水平布局控件
        H.addWidget(self.btn_open)
        H.addWidget(self.btn_font)
        H.addWidget(self.checkBox_bold)
        H.addWidget(self.checkBox_italic)
        H.addWidget(self.checkBox_underline)
        H.addWidget(self.radioButton_left)
        H.addWidget(self.radioButton_center)
        H.addWidget(self.radioButton_right)
        H.addWidget(self.comboBox)

        self.statusBar = QStatusBar()

        V = QVBoxLayout(self)  #竖直布局控件
        V.addWidget(menuBar)
        V.addWidget(self.plainText)
        V.addLayout(H)
        V.addWidget(self.statusBar)
    def pushMenu(self):   #按钮中添加菜单
        self.action_song = QAction("宋体")   #定义动作
        self.action_hei = QAction("黑体")   #定义动作
        self.action_kai = QAction("楷体")   #定义动作
        self.action_hua = QAction("华文彩云")   #定义动作

        self.menu = QMenu(self)  # 定义菜单
        self.menu.addAction(self.action_song)  # 菜单中添加动作
        self.menu.addAction(self.action_hei)  # 菜单中添加动作
        self.menu.addAction(self.action_kai)  # 菜单中添加动作
        self.menu.addAction(self.action_hua)  # 菜单中添加动作

        self.btn_font.setMenu(self.menu)  # 按钮中添加菜单

        self.action_song.triggered.connect(self.family_song)  #动作与函数的连接
        self.action_hei.triggered.connect(self.family_hei)   #动作与函数的连接
        self.action_kai.triggered.connect(self.family_kai)   #动作与函数的连接
        self.action_hua.triggered.connect(self.family_hua)   #动作与函数的连接
    def themesMunu_triggered(self,action):
        apply_stylesheet(self,theme=action.text())  #为窗口设置主题
        self.statusBar.showMessage("当前主题："+ action.text())
    def btn_open_clicked(self):
        fileName, filter = QFileDialog.getOpenFileName(filter= #打开文件对话框，获取文件名
                        '文本文件(*.txt *.py );;所有文件(*.*)')
        if fileName:
            fp = open(fileName,mode='r',encoding='UTF-8')
            lines= fp.readlines()
            for line in lines:
                self.plainText.append(line)
            fp.close()
    def bold(self,checked):   #粗体
        font = self.plainText.font()
        font.setBold(checked)
        self.plainText.setFont(font)
    def italic(self,checked):  #斜体
        font = self.plainText.font()
        font.setItalic(checked)
        self.plainText.setFont(font)
    def underline(self,checked):  #下画线
        font = self.plainText.font()
        font.setUnderline(checked)
        self.plainText.setFont(font)
    def left(self,checked):  #左对齐
        if checked:
            self.plainText.setAlignment(Qt.AlignLeft)
    def center(self,checked):  #居中
        if checked:
            self.plainText.setAlignment(Qt.AlignCenter)
    def right(self,checked):  #右对齐
        if checked:
            self.plainText.setAlignment(Qt.AlignRight)
    def font_size(self,text):  #字体大小
        font = self.plainText.font()
        font.setPointSize(int(text))
        self.plainText.setFont(font)
    def family_song(self):  #宋体字
        font = self.plainText.font()
        font.setFamily("宋体")
        self.plainText.setFont(font)
        self.btn_font.setText("宋体")
    def family_hei(self):  #黑体字
        font = self.plainText.font()
        font.setFamily("黑体")
        self.plainText.setFont(font)
        self.btn_font.setText("黑体")
    def family_kai(self):  #楷体字
        font = self.plainText.font()
        font.setFamily("楷体")
        self.plainText.setFont(font)
        self.btn_font.setText("楷体")
    def family_hua(self):  #华文彩云字
        font = self.plainText.font()
        font.setFamily("华文彩云")
        self.plainText.setFont(font)
        self.btn_font.setText("华文彩云")
if __name__ == '__main__':
    app = QApplication(sys.argv)
    apply_stylesheet(app, theme='dark_teal.xml')  #为整个应用程序设置主题
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
