import sys   #Demo7_2.py
from PySide6.QtWidgets import QApplication,QMainWindow,QPlainTextEdit,QFileDialog
from PySide6.QtCore import QFile,QTextStream,QStringConverter
from math import sin,cos,pi
class MyWindow(QMainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.resize(800,600)
        self.setupUI()  #界面
        self.fileName = "d:\\sin_cos.txt"  #"d:/sin_cos.txt" 写入的文件
    def setupUI(self):  #界面建立
        self.plainText = QPlainTextEdit()
        self.setCentralWidget(self.plainText)
        self.status=self.statusBar()
        self.menubar = self.menuBar()  # 菜单栏
        self.file=self.menubar.addMenu('文件')  #文件菜单
        action_textCreate=self.file.addAction('生成文件')  #动作
        action_textCreate.triggered.connect(self.textCreate_triggered) #动作与槽的连接
        action_textOpen = self.file.addAction('打开文件')
        action_textOpen.triggered.connect(self.textOpen_triggered)
        self.file.addSeparator()
        action_close = self.file.addAction('关闭')
        action_close.triggered.connect(self.close)
    def textCreate_triggered(self):
        file=QFile(self.fileName)
        try:
            if file.open(QFile.WriteOnly | QFile.Text | QFile.Truncate): #打开文件
                writer=QTextStream(file)  #创建文本流
                writer.setEncoding(QStringConverter.Utf8)  #设置编码
                writer.setFieldWidth(40)  #设置域宽
                writer.setFieldAlignment(QTextStream.AlignCenter)  #设置对齐方式
                writer.setRealNumberNotation(QTextStream.ScientificNotation)
                writer << "x(度)" << "sin(x)" <<"cos(x)" << "sin(x)+cos(x)"  #写入数据
                writer.setFieldWidth(0)  #设置域宽
                writer << "\n"  #写入回车换行
                writer.flush()
                for i in range(360):
                    r=i/180*pi
                    writer.setFieldWidth(40)
                    writer<<str(i)<<str(sin(r))<<str(cos(r))<<str(sin(r)+cos(r))
                    writer.setFieldWidth(0)
                    writer << "\n"
        except:
            self.status.showMessage("写入文件失败！")
        else:
            self.status.showMessage("写入文件成功！")
        file.close()
    def textOpen_triggered(self):
        (fileName, fil) = QFileDialog.getOpenFileName(self, caption="打开文本文件",
                     dir="d:\\",filter="文本文件(*.txt);;所有文件(*.*)")
        file = QFile(fileName)
        try:
            if file.open(QFile.ReadOnly | QFile.Text):  #打开文件
                self.plainText.clear()
                reader = QTextStream(file)
                reader.setEncoding(QStringConverter.Utf8)
                reader.setAutoDetectUnicode(True)
                string=reader.readAll()  #读取所有数据
                self.plainText.appendPlainText(string)
        except:
            self.status.showMessage("打开文件失败！")
        else:
            self.status.showMessage("打开文件成功！")
        file.close()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
