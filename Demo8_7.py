import sys  #Demo8_7.py
from PySide6.QtWidgets import QApplication,QWidget,QVBoxLayout,QMenuBar,QFileDialog
from PySide6.QtCharts import QChartView,QChart,QBoxPlotSeries,QBoxSet,\
                             QValueAxis,QBarCategoryAxis
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
    def action_open_triggered(self):
        fileName,fil=QFileDialog.getOpenFileName(self,"打开测试文件","d:/","Excel(*.xlsx)")
        if fileName and fil == "Excel(*.xlsx)":
            data = list()
            wb = load_workbook(fileName)
            ws = wb.active
            columns = ws.columns
            for column in columns:
                temp = list()
                for cell in column:
                    if type(cell.value) == float or type(cell.value) == int:
                        temp.append(cell.value)
                if len(temp) > 0:
                    data.append(temp)
            self.plot(data)
    def plot(self,data):  #绘制图表的函数
        boxplotSeries = QBoxPlotSeries(self)
        barCategoryAxis = QBarCategoryAxis()  # 创建坐标轴
        valueAxis = QValueAxis()  # 创建坐标轴
        for i in range(len(data)):
            boxSet = QBoxSet()
            boxSet.append(data[i])
            boxplotSeries.append(boxSet)
            barCategoryAxis.append(str(i+1))
        self.chart.removeAllSeries()
        self.chart.removeAxis(self.chart.axisX())
        self.chart.removeAxis(self.chart.axisY())
        self.chart.addSeries(boxplotSeries)
        self.chart.setAxisX(barCategoryAxis, boxplotSeries)  # 图表设置X轴
        self.chart.setAxisY(valueAxis, boxplotSeries)  # 图表设置Y轴
if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())
