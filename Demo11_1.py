import sys  # Demo11_1.py
from PySide6.QtWidgets import QApplication,QWidget,QComboBox,QPushButton,QCheckBox,\
                              QLineEdit,QSpinBox,QFormLayout
from PySide6.QtPrintSupport import QPrinter,QPrinterInfo
from PySide6.QtGui import QPen,QPainter,QPageSize,QPageLayout
from PySide6.QtCore import QPointF,QPoint
from math import cos,sin,pi

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
    def btn_printer_clicked(self):  #槽函数
        self.printer.setOutputFileName(None)
        if self.checkBox.isChecked():
            self.printer.setOutputFileName(self.line_file.text()) #设置打印到文件中
        if self.printer.isValid():
            self.painter = QPainter()
            if self.painter.begin(self.printer):
                pen = QPen()  #钢笔
                pen.setWidth(3)  #线条宽度
                self.painter.setPen(pen)  #设置钢笔
                x = self.printer.paperRect(QPrinter.DevicePixel).width()/2 #中心x坐标
                y = self.printer.paperRect(QPrinter.DevicePixel).height()/2 #中心y坐标
                r = min(self.printer.pageRect(QPrinter.DevicePixel).width()/2,
                  self.printer.paperRect(QPrinter.DevicePixel).height()/2)#外接圆半径
                p1=QPointF(r*cos(-90*pi/180)+x,r*sin(-90*pi/180)+y)
                p2=QPointF(r*cos(-18*pi/180)+x,r*sin(-18*pi/180)+y)
                p3=QPointF(r*cos(54*pi/180)+x,r*sin(54*pi/180)+y)
                p4=QPointF(r*cos(126*pi/180)+x,r*sin(126*pi/180)+y)
                p5=QPointF(r*cos(198*pi/180)+x,r*sin(198*pi/180)+y)
                pageCopies = self.spin_copies.value()
                for i in range(1,pageCopies+1):
                    self.painter.drawPolyline([p1, p3, p5, p2, p4, p1])  #绘制五角星
                    print("正在提交第{}页，共{}页。".format(i,pageCopies))
                    if i != pageCopies:
                        self.printer.newPage()
                self.painter.end()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyWidget()
    win.show()
    sys.exit(app.exec())
