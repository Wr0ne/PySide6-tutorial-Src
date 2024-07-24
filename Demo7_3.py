import sys,math   #Demo7_3.py
from PySide6.QtWidgets import QApplication,QMainWindow,QPlainTextEdit,QFileDialog
from PySide6.QtCore import QFile,QDataStream

class MyWindow(QMainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.resize(800,600)
        self.setupUI()  #界面
        self.fileName = "d:\\sin_cos.bin"  #"d:/sin_cos.bin" 写入的文件
    def setupUI(self):  #界面建立
        self.plainText = QPlainTextEdit()
        self.setCentralWidget(self.plainText)
        self.status=self.statusBar()
        self.menubar = self.menuBar()  # 菜单栏
        self.file=self.menubar.addMenu('文件')  #文件菜单
        action_binCreate=self.file.addAction('生成文件')  #动作
        action_binCreate.triggered.connect(self.binCreate_triggered) #动作与槽的连接
        action_binOpen = self.file.addAction('打开文件')
        action_binOpen.triggered.connect(self.binOpen_triggered)
        self.file.addSeparator()
        action_close = self.file.addAction('关闭')
        action_close.triggered.connect(self.close)
    def binCreate_triggered(self):
        file=QFile(self.fileName)
        try:
            if file.open(QFile.WriteOnly | QFile.Truncate): #打开文件
                writer=QDataStream(file)  #创建数据流
                writer.setVersion(QDataStream.Qt_6_2)
                writer.setByteOrder(QDataStream.BigEndian)
                writer.writeQString("version:Qt_6_2")
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
            self.status.showMessage("打开文件失败！")
        else:
            self.status.showMessage("写入文件成功！")
        file.close()
    def binOpen_triggered(self):
        (fileName, fil) = QFileDialog.getOpenFileName(self, caption="打开二进制文件",
                     dir="d:\\",filter="二进制文件(*.bin);;所有文件(*.*)")
        file = QFile(fileName)
        template="{:^16}{:^16.10}{:^16.10}{:^16.10}"
        try:
            if file.open(QFile.ReadOnly):  #打开文件
                reader = QDataStream(file)
                reader.setVersion(QDataStream.Qt_6_2)
                reader.setByteOrder(QDataStream.BigEndian)
                if reader.readQString()=="version:Qt_6_2":
                    self.plainText.clear()
                    str1 = reader.readQString()  #读取字符串
                    str2 = reader.readQString()  #读取字符串
                    str3 = reader.readQString()  #读取字符串
                    str4 = reader.readQString()  #读取字符串
                    string=template.format(str1,str2,str3,str4)
                    self.plainText.appendPlainText(string)
                    while not reader.atEnd():
                        deg = reader.readInt16()  #读取整数
                        sin = reader.readDouble() #读取浮点数
                        cos = reader.readDouble()  #读取浮点数
                        sin_cos = reader.readDouble()  #读取浮点数
                        string=template.format(deg,sin,cos,sin_cos)
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
