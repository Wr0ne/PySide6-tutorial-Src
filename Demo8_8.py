import sys,math  #Demo8_8.py
from PySide6.QtWidgets import QApplication,QWidget,QVBoxLayout
from PySide6.QtCharts import QChartView,QPolarChart,QLineSeries,QScatterSeries,QValueAxis
from PySide6.QtCore import Qt

class MyWidget(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.resize(1000,600)
        V = QVBoxLayout(self)
        chartView = QChartView(self)  #创建图表视图控件
        V.addWidget(chartView)
        chart = QPolarChart()          #创建极坐标图表
        chartView.setChart(chart)      #图表控件中设置图表
        chart.setTitle("极坐标图表")    #设置图表的标题
        lineSeries = QLineSeries()       #创建折线数据序列
        lineSeries.setName("折线")     #设置数据序列的名称
        scatterSeries = QScatterSeries()  #创建散点数据序列
        scatterSeries.setName("散点")

        r0=10
        for angle in range(0,360,2):
            r = (r0 ** 2 + (math.pi * r0 * angle / 180) ** 2) ** 0.5
            lineSeries.append(angle, r)  #数据序列中添加数据
        r0=12
        for angle in range(0,360,5):
            r = (r0 ** 2 + (math.pi * r0 * angle / 180) ** 2) ** 0.5
            scatterSeries.append(angle, r)
        chart.addSeries(lineSeries)     #图表中添加数据序列
        chart.addSeries(scatterSeries)  #图表中添加数据序列

        axis_angle = QValueAxis()       #创建数值坐标轴
        axis_angle.setTitleText("Angle")  #设置坐标轴的标题
        axis_angle.setRange(0,360)
        axis_angle.setLinePenColor(Qt.black)
        axis_radius = QValueAxis()     #创建数值坐标轴
        axis_radius.setTitleText("Distance")
        axis_radius.setRange(0,80)
        axis_radius.setGridLineColor(Qt.gray)

        chart.addAxis(axis_angle,QPolarChart.PolarOrientationAngular) #添加坐标轴
        chart.addAxis(axis_radius,QPolarChart.PolarOrientationRadial) #添加坐标轴

        lineSeries.attachAxis(axis_angle)      #数据序列与坐标轴关联
        lineSeries.attachAxis(axis_radius)     #数据序列与坐标轴关联
        scatterSeries.attachAxis(axis_angle)   #数据序列与坐标轴关联
        scatterSeries.attachAxis(axis_radius)   #数据序列与坐标轴关联
if __name__== "__main__":
    app=QApplication(sys.argv)
    window=MyWidget()
    window.show()
    sys.exit(app.exec())
