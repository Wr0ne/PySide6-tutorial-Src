import sys  #Demo3_14.py
from PySide6.QtWidgets import (QApplication, QWidget, QMenuBar, QFontDialog,
                            QPlainTextEdit, QVBoxLayout)
class MyWindow(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setWindowTitle("字体设置")
        self.resize(500,400)
        self.font = QFontDialog(self)  #建立字体对话框对象
        self.font.move(500,300)

        self.widget_setupUi()  #调用函数，构建界面
    def widget_setupUi(self):  #建立主程序界面
        menuBar = QMenuBar(self)  #定义菜单栏
        font_menu = menuBar.addMenu("Font")  #定义字体菜单
        action_currentFont = font_menu.addAction("currentFont")  #添加动作
        action_fontSelected = font_menu.addAction("fontSelected")  #添加动作
        action_getFont = font_menu.addAction("getFont") #添加动作
        self.plainText = QPlainTextEdit(self)  #显示数据控件
        self.plainText.appendPlainText("北京诺思多维科技有限公司")
        v= QVBoxLayout(self)  #主程序界面的布局
        v.addWidget(menuBar)
        v.addWidget(self.plainText)

        action_currentFont.triggered.connect(self.action_currentFont_triggered)
        action_fontSelected.triggered.connect(self.action_fontSelected_triggered)
        action_getFont.triggered.connect(self.action_getFont_triggered) 
    def action_currentFont_triggered(self):  #自定义动作槽函数
        f = self.plainText.font()  #记录当前的字体
        self.font.setCurrentFont(f)  #设置对话框的初始字体
        self.font.currentFontChanged.connect(self.plainText.setFont)  #信号槽函数连接
        ok = self.font.exec()  #用exec显示对话框，返回0或1
        if not ok:
            self.font.setCurrentFont(f)
        self.font.currentFontChanged.disconnect(self.plainText.setFont)  #信号与槽断开连接
    def action_fontSelected_triggered(self):  #自定义动作槽函数
        f = self.plainText.font()
        self.font.setCurrentFont(f)
        self.font.fontSelected.connect(self.plainText.setFont)  #对话框信号与控件的槽连接
        self.font.exec()
        self.font.fontSelected.disconnect(self.plainText.setFont) #对话框信号与控件的槽连接
    def action_getFont_triggered(self):  #自定义动作槽函数
        f = self.plainText.font()
        (OK,font)=QFontDialog.getFont(f,self,title="选择字体")
        if OK:
            self.plainText.setFont(font)
if __name__ == '__main__':
    app=QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
