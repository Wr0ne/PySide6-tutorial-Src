import sys,os   #Demo7_4.py
from PySide6.QtWidgets import QApplication,QMainWindow,QPlainTextEdit,\
                    QFileDialog,QMessageBox,QFontDialog,QColorDialog
from PySide6.QtCore import QFile,QTextStream,QDataStream,QStringConverter
from PySide6.QtGui import QPalette

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
        action_new=self.file.addAction("新建")
        action_new.triggered.connect(self.plainText.clear)
        action_open=self.file.addAction('打开文件')  #动作，打开二进制文件或文本文件
        action_open.triggered.connect(self.open_triggered)  #动作与槽的连接
        self.action_save= self.file.addAction('保存文件')  #动作，保存二进制文件或文本文件
        self.action_save.triggered.connect(self.save_triggered) #动作与槽的连接
        self.action_save.setEnabled(False)
        self.file.addSeparator()
        action_close = self.file.addAction('关闭')
        action_close.triggered.connect(self.close)
        self.setting=self.menubar.addMenu("设置")
        action_color = self.setting.addAction("设置颜色")
        action_color.triggered.connect(self.color_triggered)
        action_font = self.setting.addAction("设置字体")
        action_font.triggered.connect(self.font_triggered)
        self.plainText.textChanged.connect(self.plainText_textChaneged)
    def open_triggered(self):
        (fileName,fil)=QFileDialog.getOpenFileName(self,caption="打开文件",dir="d:\\",
           filter="二进制文件(*.bin);;文本文件(*.txt);;python文件(*.py);;所有文件(*.*)")
        if not os.path.isfile(fileName):
            return
        name,extension = os.path.splitext(fileName)  #获取文件名和扩展名
        file = QFile(fileName)
        try:
            if file.open(QFile.ReadOnly):  #打开文件
                if extension==".bin":  #根据扩展名识别二进制文件
                    reader = QDataStream(file)
                    reader.setVersion(QDataStream.Qt_6_2)  #设置版本
                    reader.setByteOrder(QDataStream.BigEndian)
                    version=reader.readQString() #读取版本号
                    if version != "version:Qt_6_2":
                        QMessageBox.information(self,"错误","版本不匹配。")
                        return
                    palette=reader.readQVariant()  #读取调色板信息
                    font=reader.readQVariant()  #读取字体信息

                    self.plainText.setPalette(palette)  #设置调色板
                    self.plainText.setFont(font)  #设置字体
                    if not file.atEnd():
                        string = reader.readQString()  #读取文本
                        self.plainText.clear()
                        self.plainText.appendPlainText(string)
                if extension==".txt" or extension==".py": #根据扩展名识别txt或py文件
                    file.setTextModeEnabled(True)
                    reader = QTextStream(file)
                    reader.setEncoding(QStringConverter.Utf8)
                    reader.setAutoDetectUnicode(True)
                    string = reader.readAll()  # 读取所有数据
                    self.plainText.clear()
                    self.plainText.appendPlainText(string)
        except:
            self.status.showMessage("文件打开失败！")
        else:
            self.status.showMessage("文件打开成功！")
        file.close()
    def save_triggered(self):
        (fileName,fil)=QFileDialog.getSaveFileName(self,caption="保存文件",dir="d:\\",
          filter="二进制文件(*.bin);;文本文件(*.txt);;python文件(*.py);;所有文件(*.*)")
        if fileName == "":
            return
        name, extension = os.path.splitext(fileName)  #获取文件名和扩展名
        file = QFile(fileName)
        try:
            if file.open(QFile.WriteOnly|QFile.Truncate):  # 打开文件
                if extension == ".bin":  # 根据扩展名识别二进制文件
                    writer = QDataStream(file)  # 创建数据流
                    writer.setVersion(QDataStream.Qt_6_2)  #设置版本
                    writer.setByteOrder(QDataStream.BigEndian)
                    writer.writeQString("version:Qt_6_2")  #写入版本
                    palette=self.plainText.palette()
                    font=self.plainText.font()
                    string=self.plainText.toPlainText()
                    writer.writeQVariant(palette)  #写入调色板
                    writer.writeQVariant(font)  #写入字体
                    writer.writeQString(string)  #写入内容
            if extension == ".txt" or extension == ".py":  # 根据扩展名识别txt或py文件
                    reader = QTextStream(file)
                    reader.setEncoding(QStringConverter.Utf8)
                    string = self.plainText.toPlainText()
                    reader << string  #写入内容
        except:
            self.status.showMessage("文件保存失败！")
        else:
            self.status.showMessage("文件保存成功！")
        file.close()
    def font_triggered(self):  #槽函数，设置字体
        font=self.plainText.font()
        ok,font=QFontDialog.getFont(font,parent=self,title="选择字体")
        if ok:
            self.plainText.setFont(font)
    def color_triggered(self):  #槽函数，设置颜色
        color=self.plainText.palette().color(QPalette.Text)
        colorDialog=QColorDialog(color,parent=self)
        if colorDialog.exec():
            color=colorDialog.selectedColor()
            palette=self.plainText.palette()
            palette.setColor(QPalette.Text,color)
            self.plainText.setPalette(palette)
    def plainText_textChaneged(self): #槽函数，判断保存动作是否需要激活或失效
        if self.plainText.toPlainText() == "":
            self.action_save.setEnabled(False)
        else:
            self.action_save.setEnabled(True)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
