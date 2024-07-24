import sys,random  #Demo8_9.py
from PySide6.QtWidgets import QApplication,QWidget,QVBoxLayout
from PySide6 import QtCharts
from PySide6.QtCore import Qt

class MyWidget(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.resize(1000,600)
        v = QVBoxLayout(self)
        chartView = QtCharts.QChartView(self)  #创建图表视图控件
        v.addWidget(chartView)
        chart = QtCharts.QChart()  #创建图表
        chartView.setChart(chart)  #图表控件中设置图表
        chart.setTitle("随机数据")  #设置图表的标题
        lineSeries = QtCharts.QLineSeries()   #创建折线数据序列
        lineSeries.setName("随机序列")  #设置数据序列的名称
        random.seed(10000)
        for i in range(101):
            lineSeries.append(i, 100000*random.random())  #数据序列中添加数据
        chart.addSeries(lineSeries)  #图表中添加数据序列
        axis_x = QtCharts.QValueAxis()  #创建数值坐标轴
        axis_x.setTitleText("Numbers")  #设置坐标轴的标题
        axis_x.setTitleBrush(Qt.black)
        axis_x.setLabelsColor(Qt.black)
        axis_x.setRange(0,100)  #设置坐标轴的范围
        axis_x.setTickCount(10)  #设置刻度的数量
        axis_x.applyNiceNumbers()  #应用智能刻度标签
        axis_x.setLinePenColor(Qt.black)  #设置坐标轴的颜色
        pen = axis_x.linePen()  #获取坐标轴的钢笔
        pen.setWidth(2)  #设置钢笔的宽度
        axis_x.setLinePen(pen)  #设置坐标轴的钢笔
        axis_x.setGridLineColor(Qt.gray)  #设置网格线的颜色
        pen=axis_x.gridLinePen()  #获取网格线的钢笔
        pen.setWidth(2)  #设置钢笔宽度
        axis_x.setGridLinePen(pen)  #设置网格线的宽度
        axis_x.setMinorTickCount(3)  #设置次刻度的数量
        axis_x.setLabelFormat("%5.1f")  #设置标签的格式

        axis_y = QtCharts.QLogValueAxis()  #建立对数坐标轴
        axis_y.setBase(10.0)  #定义对数基
        axis_y.setMax(100000.0)  #设置最大值
        axis_y.setMin(100.0)  #设置最小值
        axis_y.setTitleText("Random Values")  #设置标题
        axis_y.setMinorTickCount(9)  #设置次网格线的数量
        axis_y.setLabelFormat("%6d")  #设置格式

        chart.setAxisX(axis_x, lineSeries)  #设置坐标轴的数据
        chart.setAxisY(axis_y, lineSeries)  #设置坐标轴的数据
if __name__== "__main__":
    app=QApplication(sys.argv)
    window=MyWidget()
    window.show()
    sys.exit(app.exec())
