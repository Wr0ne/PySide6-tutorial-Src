import sys  # Demo11_5.py
from PySide6.QtWidgets import QApplication,QWidget,QTextEdit,QMenuBar,QVBoxLayout
from PySide6.QtPrintSupport import QPrintPreviewDialog,QPrintDialog,QPrinter,QPrinterInfo
from PySide6.QtCore import Qt

class MyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.showMaximized()
        menuBar = QMenuBar()
        fileMenu = menuBar.addMenu("文件(&F)")
        openAction = fileMenu.addAction("打开")
        openAction.triggered.connect(self.openAction_triggered)  #信号与槽连接
        previewAction = fileMenu.addAction("打印预览")
        previewAction.triggered.connect(self.previewAction_triggered) #信号与槽连接
        printAction = fileMenu.addAction("打印")
        printAction.triggered.connect(self.printAction_triggered)  #信号与槽连接
        fileMenu.addSeparator()
        fileMenu.addAction("退出").triggered.connect(self.close) #信号与槽连接
        self.textEdit = QTextEdit()
        V = QVBoxLayout(self)
        V.addWidget(menuBar)
        V.addWidget(self.textEdit)
        self.printer = QPrinter(QPrinterInfo.defaultPrinter()) #创建默认的打印机
    def openAction_triggered(self):  #槽函数
        #在此添加打开文件代码，将内容读取到QTextEdit中,这里以简单文本代替
        font = self.textEdit.font()
        font.setPointSize(30)
        self.textEdit.setFont(font)
        for i in range(100):
            self.textEdit.append("北京诺思多维科技有限公司")
    def previewAction_triggered(self):  #槽函数
        previewDialog = QPrintPreviewDialog(self.printer, self, flags=  #打印预览对话框
                    Qt.WindowMinimizeButtonHint | Qt.WindowMaximizeButtonHint | 
                    Qt.WindowCloseButtonHint)
        previewDialog.paintRequested.connect(self.preview_paintRequested) #信号与槽连接
        previewDialog.exec()
        self.printer = previewDialog.printer()
    def preview_paintRequested(self,printer): #槽函数
        self.textEdit.print_(printer)  #预览QTextEdit控件中的内容
    def printAction_triggered(self):  #槽函数
        printDialog = QPrintDialog(self.printer)
        printDialog.accepted.connect(self.printDialog_accepted) #信号与槽连接
        printDialog.exec()
    def printDialog_accepted(self,printer):  #槽函数
        self.textEdit.print_(printer)  #打印QTextEdit控件中的内容
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyWidget()
    win.show()
    sys.exit(app.exec())
