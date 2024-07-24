import sys  #Demo2_11.py
from PySide6.QtWidgets import (QApplication,QWidget,QPushButton,QHBoxLayout,
                             QVBoxLayout,QTextEdit)
from PySide6.QtGui import QTextImageFormat
from PySide6.QtWidgets import QFileDialog

class MyWidget(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setWindowTitle("文字处理")
        self.setupUi()
        self.btnOpen.clicked.connect(self.openText)  #信号与槽的连接
        self.btnInsert.clicked.connect(self.insertText)  #信号与槽的连接
        self.btnImage.clicked.connect(self.openImage)   #信号与槽的连接
        self.btnOutput.clicked.connect(self.sysOutput)  #信号与槽的连接
    def setupUi(self):  #建立界面上的控件
        self.textEdit = QTextEdit(self)
        self.btnOpen = QPushButton(self)
        self.btnOpen.setText("打开文本文件")
        self.btnInsert = QPushButton(self)
        self.btnInsert.setText("插入文本")
        self.btnImage = QPushButton(self)
        self.btnImage.setText("插入图像文件")
        self.btnOutput = QPushButton(self)
        self.btnOutput.setText("作为系统输出")

        self.horizontalLayout = QHBoxLayout()  #水平排列
        self.horizontalLayout.addWidget(self.btnOpen)
        self.horizontalLayout.addWidget(self.btnInsert)
        self.horizontalLayout.addWidget(self.btnImage)
        self.horizontalLayout.addWidget(self.btnOutput)
        self.verticalLayout = QVBoxLayout(self)  #竖直排列
        self.verticalLayout.addWidget(self.textEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
    def openText(self):  #按钮的槽函数
        name = ""
        name,filter=QFileDialog.getOpenFileName(self,"选择文件","d:\\","文本(*.txt)")
        print(name)
        if len(name)>0:
            fp = open(name,'r')
            strings = fp.readlines()
            for i in strings:
                i=i.strip("\n")
                self.textEdit.append(i)
            fp.close()
    def insertText(self):  #按钮的槽函数
        self.textEdit.setFontFamily('楷体')  #定义格式字体
        self.textEdit.setFontPointSize(20)    #定义格式字体大小
        self.textEdit.insertPlainText('Hello,Nice to meet you!')  #按格式插入字体
        self.textEdit.insertHtml("<a href='http://www.qq.com'> QQ</a>")  #插入html文本
    def openImage(self): #按钮的槽函数
        name,filter=QFileDialog.getOpenFileName(self, "选择文件", "d:\\", "图像(*.png *.jpg)")
        textCursor = self.textEdit.textCursor()
        pic = QTextImageFormat()
        pic.setName(name)  # 图片路径
        pic.setHeight(100)  # 图片高度
        pic.setWidth(100)  # 图片宽度
        textCursor.insertImage(pic)  # 插入图片
    def sysOutput(self):  #按钮的槽函数
        sys.stdout = self  #修改系统的标准输出
        sys.stderr = self  #修改系统的异常信息输出
        print("我是北京诺思多维科技有限公司，很高兴认识你！")
    def write(self,info):  #将系统标准输出改成窗口，需要定义一个write()函数
        info = info.strip("\r\n")
        self.textEdit.insertPlainText(info)
if __name__ == '__main__':
    app=QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
