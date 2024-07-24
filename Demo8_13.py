import sys  #Demo8_13.py
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout
from PySide6.QtCore import Qt,QPointF
from PySide6 import QtCharts

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

        self.barSeries = QtCharts.QBarSeries()  #创建数据序列
        self.barSeries.append([set1, set2])  #添加数据项
        self.lineSeries = QtCharts.QLineSeries()  #创建数据序列
        self.lineSeries.setName("去年季度总额")
        self.lineSeries.append([QPointF(0,32),QPointF(1,46),QPointF(2,43),QPointF(3,48)])
        self.chart.addSeries(self.barSeries)   #图表中添加数据序列
        self.chart.addSeries(self.lineSeries)   #图表中添加数据序列

        self.barCategoryAxis = QtCharts.QBarCategoryAxis()  #创建坐标轴
        self.chart.addAxis(self.barCategoryAxis, Qt.AlignBottom)  #图表中添加坐标轴
        self.barCategoryAxis.append(["第一季度","第二季度","第三季度","第四季度"])#添加条目
        self.valueAxis = QtCharts.QValueAxis()
        self.valueAxis.setRange(0,50)
        self.chart.addAxis(self.valueAxis,Qt.AlignLeft)

        self.barSeries.attachAxis(self.valueAxis)  #数据项与坐标轴关联
        self.barSeries.attachAxis(self.barCategoryAxis)  #数据项与坐标轴关联
        self.lineSeries.attachAxis(self.valueAxis)  #数据项与坐标轴关联
        self.lineSeries.attachAxis(self.barCategoryAxis)  #数据项与坐标轴关联
        ##以下是对图例的设置
        legend = self.chart.legend()
        legend.setAlignment(Qt.AlignBottom)
        legend.setBackgroundVisible(True)
        legend.setBorderColor(Qt.red)
        legend.setColor(Qt.yellow)
        pen = legend.pen()
        pen.setWidth(4)
        legend.setPen(pen)
        legend.setToolTip("销售团队的销售额对比")
        legend.setShowToolTips(True)
        legend.setMarkerShape(legend.MarkerShapeFromSeries)
        for i in legend.markers():
            font=i.font()
            font.setPointSize(12)
            i.setFont(font)
            if i.type() == QtCharts.QLegendMarker.LegendMarkerTypeBar:
                i.setShape(QtCharts.QLegend.MarkerShapeRotatedRectangle)
            else:
                i.setShape(QtCharts.QLegend.MarkerShapeFromSeries)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
