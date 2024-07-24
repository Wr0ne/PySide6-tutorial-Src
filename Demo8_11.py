import sys  #Demo8_11.py
from PySide6.QtWidgets import QApplication,QWidget,QVBoxLayout
from PySide6 import QtCharts
from PySide6.QtCore import Qt

class MyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.resize(800, 600)
        v = QVBoxLayout(self)
        self.chartView = QtCharts.QChartView(self)  #创建图表视图控件
        v.addWidget(self.chartView)
        self.chart = QtCharts.QChart()  #创建图表
        self.chartView.setChart(self.chart)  #将图表加入到图表视图控件中

        set1 = QtCharts.QBarSet("一组销售额")  # 创建数据项
        set1.append([12, 34, 23, 45])  # 添加数据
        set2 = QtCharts.QBarSet("二组销售额")  # 创建数据项
        set2.append([24, 33, 42, 41])  # 添加数据
        set3 = QtCharts.QBarSet("三组销售额")  # 创建数据项
        set3.append([21, 44, 23, 40])  # 添加数据

        self.barSeries = QtCharts.QBarSeries()  #创建数据序列
        self.barSeries.append([set1, set2, set3])  #添加数据项
        self.chart.addSeries(self.barSeries)   #图表中添加数据序列

        self.barCategoryAxis = QtCharts.QBarCategoryAxis()  #创建坐标轴
        self.chart.addAxis(self.barCategoryAxis,Qt.AlignBottom) #图表中添加坐标轴
        self.barCategoryAxis.append(["第一季度","第二季度","第三季度","第四季度"])
        self.categoryAxis = QtCharts.QCategoryAxis()  #创建数值坐标轴
        self.chart.addAxis(self.categoryAxis, Qt.AlignLeft)   #图表中添加坐标轴
        self.categoryAxis.setRange(0, 60)  # 设置坐标轴的数值范围
        self.categoryAxis.append("不及格", 10)  #添加条目
        self.categoryAxis.append("及格", 20)  #添加条目
        self.categoryAxis.append("良好", 25)  #添加条目
        self.categoryAxis.append("优秀", 42)  #添加条目
        self.categoryAxis.append("超出预期", 60)  #添加条目
        self.categoryAxis.setStartValue(5)  #指定起始值

        self.barSeries.attachAxis(self.categoryAxis)  #数据项与坐标轴关联
        self.barSeries.attachAxis(self.barCategoryAxis)  #数据项与坐标轴关联
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
