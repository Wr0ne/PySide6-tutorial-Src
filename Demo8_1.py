import sys,math  #Demo8_1.py
from PySide6.QtWidgets import QApplication,QWidget,QVBoxLayout
from PySide6.QtCharts import QChartView,QChart,QLineSeries,QValueAxis

class MyWidget(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.resize(800,600)
        V = QVBoxLayout(self)
        chartView = QChartView(self)  #创建图表视图控件
        V.addWidget(chartView)
        chart = QChart()  #创建图表
        chartView.setChart(chart)   #图表控件中添加图表
        chart.setTitle("sin-cos")   #设置图表的标题
        series_sin = QLineSeries()   #创建折线数据序列
        series_cos = QLineSeries()   #创建折线数据序列
        series_sin.setName("sin")   #设置数据序列的名称
        series_cos.setName("cos")   #设置数据序列的名称

        for i in range(360):
            series_sin.append(i, math.sin(math.radians(i)))  #数据序列中添加数据
            series_cos.append(i, math.cos(math.radians(i)))  #数据序列中添加数据
        chart.addSeries(series_sin)  #图表中添加数据序列
        chart.addSeries(series_cos)  #图表中添加数据序列
        axis_x = QValueAxis()  #创建坐标轴
        axis_x.setRange(0,360)  #设置坐标轴的范围
        axis_x.setTitleText("degree")  #设置坐标轴的标题
        axis_y = QValueAxis()
        axis_y.setRange(-1,1)
        axis_y.setTitleText("values")
        chart.setAxisX(axis_x, series_sin)  #设置坐标轴的数据
        chart.setAxisY(axis_y, series_sin)  #设置坐标轴的数据
        chart.setAxisX(axis_x, series_cos)
        chart.setAxisY(axis_y, series_cos)
if __name__== "__main__":
    app=QApplication(sys.argv)
    window=MyWidget()
    window.show()
    sys.exit(app.exec())
