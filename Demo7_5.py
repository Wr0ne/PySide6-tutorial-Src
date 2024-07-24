import sys,math,struct   #Demo7_5.py
from PySide6.QtWidgets import QApplication,QMainWindow,QPlainTextEdit
from PySide6.QtCore import QDataStream,QBuffer

class MyWindow(QMainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.resize(800,600)
        self.setupUI()  #界面
        self.buffer=QBuffer()  #创建缓存
    def setupUI(self):  #界面建立
        self.plainText = QPlainTextEdit()
        self.setCentralWidget(self.plainText)
        self.status=self.statusBar()
        self.menubar = self.menuBar()  # 菜单栏
        self.file=self.menubar.addMenu('文件')  #文件菜单
        action_dataCreate=self.file.addAction('生成数据')  #动作
        action_dataCreate.triggered.connect(self.dataCreate_triggered)  #动作与槽的连接
        action_dataRead = self.file.addAction('读取数据')  #动作
        action_dataRead.triggered.connect(self.dataRead_triggered)  #动作与槽的连接
        self.file.addSeparator()
        action_close = self.file.addAction('关闭')
        action_close.triggered.connect(self.close)
    def dataCreate_triggered(self):
        try:
            if self.buffer.open(QBuffer.WriteOnly.WriteOnly | QBuffer.Truncate): #打开缓存
                writer=QDataStream(self.buffer)  #创建数据流
                writer.setVersion(QDataStream.Qt_6_2)
                writer.setByteOrder(QDataStream.BigEndian)
                writer.writeQString("x(度)")  #写入字符串
                writer.writeQString("sin(x)")  #写入字符串
                writer.writeQString("cos(x)")  #写入字符串
                writer.writeQString("sin(x)+cos(x)")  #写入字符串
                for i in range(360):
                    r=i/180*math.pi
                    writer.writeInt16(i)   #int
                    writer.writeDouble(math.sin(r))  #sin
                    writer.writeDouble(math.cos(r))   #cos
                    writer.writeDouble(math.sin(r)+math.cos(r)) #sin+cos
        except:
            self.status.showMessage("写数据失败！")
        else:
            self.status.showMessage("写数据成功！")
        self.buffer.close()
    def dataRead_triggered(self):
        template="{:^10}{:^20.13}{:^20.13}{:^20.13}"
        try:
            if self.buffer.open(QBuffer.ReadOnly):  #打开缓存
                reader = QDataStream(self.buffer)
                reader.setVersion(QDataStream.Qt_6_2)
                reader.setByteOrder(QDataStream.BigEndian)
                self.plainText.clear()
                str1 = reader.readQString()  # 读取字符串
                str2 = reader.readQString()  # 读取字符串
                str3 = reader.readQString()  # 读取字符串
                str4 = reader.readQString()  # 读取字符串
                string = template.format(str1, str2, str3, str4)
                self.plainText.appendPlainText(string)
                while not reader.atEnd():
                    deg = reader.readInt16()  # 读取整数
                    sin = reader.readDouble()  # 读取浮点数
                    cos = reader.readDouble()  # 读取浮点数
                    sin_cos = reader.readDouble()  # 读取浮点数
                    string = template.format(deg, sin, cos, sin_cos)
                    self.plainText.appendPlainText(string)
        except:
            self.status.showMessage("读数据失败！")
        else:
            self.status.showMessage("读数据成功！")
        self.buffer.close()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
