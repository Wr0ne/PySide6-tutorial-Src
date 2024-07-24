import sys  #Demo3_15.py
from PySide6.QtWidgets import (QApplication,QWidget,QMenuBar,QPlainTextEdit,QVBoxLayout,
                            QFileDialog)
class MyWindow(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setWindowTitle("打开文件")
        self.setGeometry(100,100,600,500)
        self.fileDialog = QFileDialog(self)
        self.widget_setupUi()
    def widget_setupUi(self):  #建立主程序界面
        menuBar = QMenuBar(self)  #定义菜单栏
        file_menu = menuBar.addMenu("File")  #定义文件菜单
        action_currentChanged = file_menu.addAction("currentChaged信号")
        action_directoryEntered = file_menu.addAction("directoryEntered信号")
        action_fileSelected = file_menu.addAction("fileSelected信号")
        action_filesSelected = file_menu.addAction("filesSelected信号")
        action_filterSelected = file_menu.addAction("filterSelected信号")
        file_menu.addSeparator()
        action_getExistingDirectory = file_menu.addAction("getExistingDirectory")
        action_getOpenFileName = file_menu.addAction("getOpenFileName")
        action_getOpenFileNames = file_menu.addAction("getOpenFileNames")
        action_getSaveFileName = file_menu.addAction("getSaveFileName")
        file_menu.addSeparator()
        action_open = file_menu.addAction("open...")
        action_saveAs = file_menu.addAction("saveAs...")

        self.plainText = QPlainTextEdit(self)  #显示数据控件
        self.plainText.appendPlainText("北京诺思多维科技有限公司")
        v= QVBoxLayout(self)  #主程序界面的布局
        v.addWidget(menuBar)
        v.addWidget(self.plainText)

        action_currentChanged.triggered.connect(self.action_currentChanged_triggered)
        action_directoryEntered.triggered.connect(self.action_directoryEntered_triggered)
        action_fileSelected.triggered.connect(self.action_fileSelected_triggered)
        action_filesSelected.triggered.connect(self.action_filesSelected_triggered)
        action_filterSelected.triggered.connect(self.action_filterSelected_triggered)
        action_getExistingDirectory.triggered.connect(self.action_getExistingDirectory_triggered)
        action_getOpenFileName.triggered.connect(self.action_getOpenFileName_triggered)
        action_getOpenFileNames.triggered.connect(self.action_getOpenFileNames_triggered)
        action_getSaveFileName.triggered.connect(self.action_getSaveFileName_triggered)
        action_open.triggered.connect(self.action_open_triggered)
        action_saveAs.triggered.connect(self.action_saveAs_triggered)
    def action_currentChanged_triggered(self): #信号测试
        self.fileDialog.setFileMode(QFileDialog.ExistingFiles)
        self.fileDialog.setDirectory("d:\\")
        self.fileDialog.setNameFilter("text(*.txt);;Picture(*.png *.bmp);;所有文件(*.*)")
        self.fileDialog.currentChanged.connect(self.output)
        self.fileDialog.exec()
        self.fileDialog.currentChanged.disconnect(self.output)
    def action_directoryEntered_triggered(self): #信号测试
        self.fileDialog.directoryEntered.connect(self.output)
        self.fileDialog.exec()
        self.fileDialog.directoryEntered.disconnect(self.output)
    def action_fileSelected_triggered(self): #信号测试
        self.fileDialog.fileSelected.connect(self.output)
        self.fileDialog.exec()
        self.fileDialog.fileSelected.disconnect(self.output)
    def action_filesSelected_triggered(self): #信号测试
        self.fileDialog.setFileMode(QFileDialog.ExistingFiles)
        self.fileDialog.filesSelected.connect(self.output)
        self.fileDialog.exec()
        self.fileDialog.filesSelected.disconnect(self.output)
        self.fileDialog.setFileMode(QFileDialog.AnyFile)
    def action_filterSelected_triggered(self): #信号测试
        self.fileDialog.setNameFilter("text(*.txt);;image(*.png *.bmp);;所有文件(*.*)")
        self.fileDialog.filterSelected.connect(self.output)
        self.fileDialog.exec()
        self.fileDialog.filterSelected.disconnect(self.output)
    def action_getExistingDirectory_triggered(self): #get函数测试
        dir = QFileDialog.getExistingDirectory(self,caption="选择路径",dir="d:\\")
        self.output(dir)
    def action_getOpenFileName_triggered(self):  #get函数测试
        (fileName,filter)=QFileDialog.getOpenFileName(self,caption="打开文件",dir="d:\\",
            filter="image(*.png *.bmp);;text(*.txt);;所有文件(*.*)",selectedFilter="text(*.txt)")
        self.output((fileName,filter))
    def action_getOpenFileNames_triggered(self): #get函数测试
        (fileNames,filter)=QFileDialog.getOpenFileNames(self,caption="打开文件",dir= "d:\\",
           filter="image(*.png *.bmp);;text(*.txt);;所有文件(*.*)",selectedFilter="text(*.txt)")
        self.output((fileNames,filter))
    def action_getSaveFileName_triggered(self): #get函数测试
        (fileName,filter)=QFileDialog.getSaveFileName(self,caption="打开文件",dir="d:\\",
            filter="image(*.png *.bmp);;text(*.txt);;所有文件(*.*)",selectedFilter="text(*.txt)")
        self.output((fileName,filter))
    def output(self,file): #输出结果函数
        if type(file) == str:
            self.plainText.appendPlainText(file)
        if type(file) == tuple:
            for i in file:
                if type(i) == str:
                    self.plainText.appendPlainText(i)
                if type(i) == list:
                    for j in i:
                        self.plainText.appendPlainText(j)
    def action_open_triggered(self): #打开UTF-8格式的txt文件，读取内容
        self.fileDialog.setAcceptMode(QFileDialog.AcceptOpen)
        self.fileDialog.setFileMode(QFileDialog.ExistingFile)
        self.fileDialog.setNameFilter("文本文件(*.txt)")
        if self.fileDialog.exec():
            fp=open(self.fileDialog.selectedFiles()[0],'r',encoding='UTF-8')
            string = fp.readlines()
            for i in string:
                self.plainText.appendPlainText(i)
            fp.close()
    def action_saveAs_triggered(self):  #保存到新文件中
        string = self.plainText.toPlainText()
        if string != "":
            name,fil=QFileDialog.getSaveFileName(self,"另存文件","d:\\","文本文件(*.txt)")
            if name != "":
                fp = open(name,'a+',encoding='UTF-8')
                fp.writelines(string)
                fp.close()
if __name__ == '__main__':
    app=QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
