import sys  #Demo8_5.py
from PySide6.QtWidgets import QApplication,QWidget,QVBoxLayout,QGraphicsLinearLayout
from PySide6 import QtCharts

class MyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.resize(800, 600)
        V = QVBoxLayout(self)
        chartView = QtCharts.QChartView(self)  #创建图表视图控件
        V.addWidget(chartView)
        chart = QtCharts.QChart()
        chartView.setChart(chart)
        linearGraphicsLayout = QGraphicsLinearLayout(chart)
        self.chart1 = QtCharts.QChart()  #创建图表
        self.chart2 = QtCharts.QChart()  # 创建图表
        self.chart3 = QtCharts.QChart()  # 创建图表
        linearGraphicsLayout.addItem(self.chart1)
        linearGraphicsLayout.addItem(self.chart2)
        linearGraphicsLayout.addItem(self.chart3)
        self.chart1.setTitle("XXXXX公司2021年季度销售业绩")  # 设置图表标题
        self.chart2.setTitle("XXXXX公司2021年季度销售业绩")  # 设置图表标题
        self.chart3.setTitle("XXXXX公司2021年季度销售业绩")  # 设置图表标题

        set1 = QtCharts.QBarSet("一组销售额")  # 创建数据项
        set1.append([12, 34, 23, 45])  # 添加数据
        set2 = QtCharts.QBarSet("二组销售额")  # 创建数据项
        set2.append([24, 33, 42, 41])  # 添加数据
        set3 = QtCharts.QBarSet("三组销售额")  # 创建数据项
        set3.append([21, 44, 23, 40])  # 添加数据

        self.barSeries = QtCharts.QBarSeries()  #创建数据序列
        self.barSeries.append([set1, set2, set3])  #添加数据项
        self.chart1.addSeries(self.barSeries)    #图表中添加数据序列

        self.stackedBarSeries = QtCharts.QStackedBarSeries()  #创建数据序列
        self.stackedBarSeries.append([set1, set2, set3])  #添加数据项
        self.chart2.addSeries(self.stackedBarSeries)  #图表中添加数据序列

        self.percentBarSeries = QtCharts.QPercentBarSeries()  #创建数据序列
        self.percentBarSeries.append([set1, set2, set3])  #添加数据项
        self.chart3.addSeries(self.percentBarSeries)  #图表中添加数据序列

        self.barCategoryAxis1 = QtCharts.QBarCategoryAxis()  #创建坐标轴
        self.barCategoryAxis1.append(["第一季度","第二季度","第三季度","第四季度"])
        self.barCategoryAxis2 = QtCharts.QBarCategoryAxis()  #创建坐标轴
        self.barCategoryAxis2.append(["第一季度","第二季度","第三季度","第四季度"])
        self.barCategoryAxis3 = QtCharts.QBarCategoryAxis()  #创建坐标轴
        self.barCategoryAxis3.append(["第一季度","第二季度","第三季度","第四季度"])

        self.chart1.setAxisX(self.barCategoryAxis1, self.barSeries)  #图表设置X轴
        self.chart2.setAxisX(self.barCategoryAxis2, self.stackedBarSeries) #图表设置X轴
        self.chart3.setAxisX(self.barCategoryAxis3, self.percentBarSeries) #图表设置X轴
        self.valueAxis1 = QtCharts.QValueAxis()  #创建坐标轴
        self.valueAxis1.setRange(0, 50)  #设置坐标轴的数值范围
        self.chart1.setAxisY(self.valueAxis1, self.barSeries)  #图表设置Y轴
        self.valueAxis2 = QtCharts.QValueAxis()  # 创建坐标轴
        self.valueAxis2.setRange(0, 150)  # 设置坐标轴的数值范围
        self.chart2.setAxisY(self.valueAxis2, self.stackedBarSeries)  #图表设置Y轴
        self.valueAxis3 = QtCharts.QValueAxis()  # 创建坐标轴
        self.valueAxis3.setRange(0, 100)  # 设置坐标轴的数值范围
        self.chart3.setAxisY(self.valueAxis3, self.percentBarSeries)  #图表设置Y轴

        self.barSeries.setLabelsVisible(True)  #设置数据标签可见
        self.barSeries.setLabelsFormat("@value万")  #设置标签格式
        self.barSeries.setLabelsPosition(self.barSeries.LabelsInsideEnd)#设置标签位置
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
