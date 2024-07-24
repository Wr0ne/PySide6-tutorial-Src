import sys   #Demo7_1.py
from PySide6.QtWidgets import QApplication,QMainWindow,QPlainTextEdit,QFileDialog
from PySide6.QtCore import QFile,QByteArray

class MyWindow(QMainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.resize(800,600)
        self.setupUI()  #界面
    def setupUI(self):  #界面建立
        self.plainText = QPlainTextEdit()
        self.setCentralWidget(self.plainText)
        self.status=self.statusBar()
        self.menubar = self.menuBar()  # 菜单栏
        self.file=self.menubar.addMenu('文件')  #文件菜单
        action_textOpen=self.file.addAction('打开文本文件')  #动作
        action_textOpen.triggered.connect(self.textOpen_triggered)  #动作与槽的连接
        action_dataOpen = self.file.addAction('打开十六进制文件')
        action_dataOpen.triggered.connect(self.dataOpen_triggered)
        self.file.addSeparator()
        action_textWrite = self.file.addAction('保存到新文本文件中')
        action_textWrite.triggered.connect(self.textWrite_triggered)
        action_dataWrite = self.file.addAction('保存到十六进制文件')
        action_dataWrite.triggered.connect(self.dataWrite_triggered)
        self.file.addSeparator()
        action_close = self.file.addAction('关闭')
        action_close.triggered.connect(self.close)
    def textOpen_triggered(self):
        (fileName,fil)=QFileDialog.getOpenFileName(self,caption="打开文本文件",
                   filter="text(*.txt);;python(*.py);;所有文件(*.*)")
        file=QFile(fileName)
        if file.exists():
            file.open(QFile.ReadOnly | QFile.Text)  #打开文件
            self.plainText.clear()
            try:
                while not file.atEnd():
                    string=file.readLine()  #按行读取
                    string=str(string,encoding='utf-8')  #转成字符串
                    self.plainText.appendPlainText(string.rstrip('\n'))
            except:
                self.status.showMessage("打开文件失败！")
            else:
                self.status.showMessage("打开文件成功！")
        file.close()
    def textWrite_triggered(self):
        (fileName,fil)=QFileDialog.getSaveFileName(self,caption="另存为",
                    filter="text(*.txt);;python(*.py);;所有文件(*.*)")
        string=self.plainText.toPlainText()
        if fileName != "" and string != "":
            ba = QByteArray(string)
            file = QFile(fileName)
            try:
                file.open(QFile.WriteOnly | QFile.Text)  #打开文件
                file.write(ba)  #写入文件
            except:
                self.status.showMessage("文件保存失败！")
            else:
                self.status.showMessage("文件保存成功！")
            file.close()
    def dataOpen_triggered(self):
        (fileName, fil) = QFileDialog.getOpenFileName(self, caption="打开Hex文件",
                     filter="Hex文件(*.hex);;所有文件(*.*)")
        file = QFile(fileName)
        if file.exists():
            file.open(QFile.ReadOnly)  #打开文件
            self.plainText.clear()
            try:
                while not file.atEnd():
                    string = file.readLine()  #按行读取数据
                    string = QByteArray.fromHex(string)  #从十六进制数据中解码
                    string = str(string,encoding="utf-8")  #从字节转成字符串
                    self.plainText.appendPlainText(string)
            except:
                self.status.showMessage("打开文件失败！")
            else:
                self.status.showMessage("打开文件成功！")
        file.close()
    def dataWrite_triggered(self):
        (fileName, fil) = QFileDialog.getSaveFileName(self, caption="另存为",
                    filter="Hex文件(*.hex);;所有文件(*.*)")
        string = self.plainText.toPlainText()
        if fileName != "" and string != "":
            ba = QByteArray(string)
            hex_ba=ba.toHex()  #转成十六进制
            file = QFile(fileName)
            try:
                file.open(QFile.WriteOnly) #打开文件
                file.write(hex_ba)  #写入数据
            except:
                self.status.showMessage("文件保存失败！")
            else:
                self.status.showMessage("文件保存成功！")
            file.close()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
