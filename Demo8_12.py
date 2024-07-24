import sys  #Demo8_12.py
from PySide6.QtWidgets import QApplication,QWidget,QVBoxLayout,QMenuBar,QFileDialog
from PySide6.QtCharts import QChartView,QChart,QLineSeries,QValueAxis,QDateTimeAxis
from PySide6.QtCore import QDateTime
from openpyxl import load_workbook

class MyWindow(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setupUi()
    def setupUi(self):
        menuBar=QMenuBar()
        fileMenu=menuBar.addMenu("文件(&F)")
        fileMenu.addAction("打开(&O)").triggered.connect(self.action_open_triggered)
        fileMenu.addSeparator()
        fileMenu.addAction("退出(&E)").triggered.connect(self.close)
        chartView = QChartView()
        v=QVBoxLayout(self)
        v.addWidget(menuBar)
        v.addWidget(chartView)
        self.chart = QChart()
        chartView.setChart(self.chart)
    def action_open_triggered(self):  #打开Excel文档，读取数据
        fileName,fil=QFileDialog.getOpenFileName(self,"打开测试文件","d:/","Excel(*.xlsx)")
        if fileName and fil == "Excel(*.xlsx)":
            dateTimeList = list()  #时间列表
            valueList_1 = list()   #数值列表
            valueList_2 = list()   #数值列表
            wb = load_workbook(fileName)
            ws = wb.active
            for row in ws.rows:
                dateTimeList.append(QDateTime(row[0].value))  #添加时间数据
                valueList_1.append(row[1].value)  #添加数值数据
                valueList_2.append(row[2].value)  #添加数值数据
            self.plot(dateTimeList,valueList_1,valueList_2)  #调用绘制图表函数
    def plot(self,dateTimeList,valueList_1,valueList_2):  #绘制图表的函数
        lineSeries_1 = QLineSeries(self)  #第1个数据序列
        lineSeries_1.setName('价格1')
        lineSeries_2 = QLineSeries(self)  #第2个数据序列
        lineSeries_2.setName('价格2')
        for i in range(len(dateTimeList)):
            msec = float(dateTimeList[i].toMSecsSinceEpoch())  #换算成毫秒
            lineSeries_1.append(msec,valueList_1[i])  #第1个数据序列添加数据
            lineSeries_2.append(msec,valueList_2[i])  #第2个数据序列添加数据
        dateTimeAxis = QDateTimeAxis(self)  # 创建时间坐标轴
        dateTimeAxis.setRange(dateTimeList[0],dateTimeList[len(dateTimeList)-1])
        dateTimeAxis.setFormat('yyyy-MM-dd HH:mm')
        dateTimeAxis.setTickCount(8)
        valueAxis = QValueAxis(self)  #创建数值坐标轴

        self.chart.removeAllSeries()
        self.chart.removeAxis(self.chart.axisX())
        self.chart.removeAxis(self.chart.axisY())
        self.chart.addSeries(lineSeries_1)
        self.chart.addSeries(lineSeries_2)
        self.chart.setAxisX(dateTimeAxis, lineSeries_1)  # 图表设置X轴
        self.chart.setAxisY(valueAxis, lineSeries_1)  # 图表设置Y轴
        self.chart.setAxisX(dateTimeAxis, lineSeries_2)  # 图表设置X轴
        self.chart.setAxisY(valueAxis, lineSeries_2)  # 图表设置Y轴
if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())
