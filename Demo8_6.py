import sys  #Demo8_6.py
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout
from PySide6 import QtCharts
from PySide6.QtCharts import QChartView,QChart,QCandlestickSeries,QCandlestickSet,QValueAxis,QBarCategoryAxis
from PySide6.QtCore import Qt

class MyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.resize(800, 600)
        V = QVBoxLayout(self)
        self.chartView = QChartView(self)  #创建图表视图控件
        V.addWidget(self.chartView)
        self.chart = QChart()  #创建图表
        self.chartView.setChart(self.chart)  #将图表加入到图表视图控件中
        self.chart.setTitle("XXXX股票历史涨跌情况")  # 设置图表标题

        open = [12.8, 13.0, 13.2 ,12.9, 13.2, 14.9]  #股票开盘价
        high = [13.8, 15.5, 14.3, 14.9, 14.2, 15.1]   #股票最高价
        low  = [11.7, 12.0, 11.8, 11.7, 13.0, 13.3]  #股票最低价
        close = [12.7, 14.2, 12.8, 12.2, 13.7, 14.6]   #股票收盘价

        self.candleSetList = list()  #放置蜡烛数据的列表
        for i in range(len(open)):
            candleSet = QCandlestickSet()  #蜡烛数据
            candleSet.setOpen(open[i])  #设置初始值
            candleSet.setHigh(high[i])  #设置最高值
            candleSet.setLow(low[i])  #设置最低值
            candleSet.setClose(close[i])  #设置期末值
            self.candleSetList.append(candleSet)

        self.candlestickSeries = QCandlestickSeries()  #蜡烛数据序列
        self.candlestickSeries.append(self.candleSetList)  #添加蜡烛数据
        self.candlestickSeries.setIncreasingColor(Qt.red)  #设置上涨时颜色
        self.candlestickSeries.setDecreasingColor(Qt.green)  #设置下跌时的颜色
        self.candlestickSeries.setCapsVisible(True)  #显示帽线

        self.chart.addSeries(self.candlestickSeries)
        self.barCategoryAxis = QBarCategoryAxis()  #创建坐标轴
        self.barCategoryAxis.append(["1", "2", "3", "4","5","6"])
        self.chart.setAxisX(self.barCategoryAxis, self.candlestickSeries)  #图表设置X轴
        self.valueAxis = QValueAxis()   #创建坐标轴
        self.valueAxis.setRange(11, 16)  #设置坐标轴的数值范围
        self.chart.setAxisY(self.valueAxis, self.candlestickSeries)  #图表设置Y轴
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
