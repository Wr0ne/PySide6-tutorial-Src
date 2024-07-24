import sys  # Demo11_2.py
from PySide6.QtWidgets import QApplication,QWidget,QComboBox,QPushButton,QCheckBox,\
                              QLineEdit,QSpinBox,QFormLayout
from PySide6.QtPrintSupport import QPrinter,QPrinterInfo
from PySide6.QtGui import QPainter,QPageSize,QPageLayout
from PySide6.QtCore import QPoint

class MyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.comboBox = QComboBox()
        self.comboBox.currentTextChanged.connect(self.comboBox_currentText)#信号与槽
        self.spin_copies = QSpinBox()
        self.spin_copies.setRange(1,100)
        self.checkBox = QCheckBox('输出到文件')
        self.checkBox.clicked.connect(self.checkBox_clicked)
        self.line_file = QLineEdit()
        self.line_file.setText('d:/stars.pdf')
        self.line_file.setEnabled(self.checkBox.isChecked())
        self.btn_printer = QPushButton('打印')
        self.btn_printer.clicked.connect(self.btn_printer_clicked)  #信号与槽连接
        formLayout = QFormLayout(self)
        formLayout.addRow("选择打印机：", self.comboBox)
        formLayout.addRow("设置打印份数：", self.spin_copies)
        formLayout.addRow(self.checkBox, self.line_file)
        formLayout.addRow(self.btn_printer)

        printerNames = QPrinterInfo.availablePrinterNames()
        self.comboBox.addItems(printerNames)
        self.comboBox.setCurrentText(QPrinterInfo.defaultPrinterName())
    def comboBox_currentText(self,text):  #槽函数
        printInfo = QPrinterInfo.printerInfo(text)
        self.printer = QPrinter(printInfo)  #打印机
        self.printer.setPageOrientation(QPageLayout.Portrait)
        self.printer.setFullPage(False)
        self.printer.setPageSize(QPageSize.A4)
        self.printer.setColorMode(QPrinter.GrayScale)
    def checkBox_clicked(self,checked):  #槽函数
            self.line_file.setEnabled(checked)

    def btn_printer_clicked(self):  # 槽函数
        self.printer.setOutputFileName(None)
        if self.checkBox.isChecked():
            self.printer.setOutputFileName(self.line_file.text())  # 设置打印到文件中
        if self.printer.isValid():
            self.painter = QPainter()
            if self.painter.begin(self.printer):
                self.render(self.painter, QPoint(200, 0))
                self.painter.end()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyWidget()
    win.show()
    sys.exit(app.exec())
