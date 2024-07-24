import sys  #Demo8_4.py
from PySide6.QtWidgets import QApplication,QWidget,QVBoxLayout
from PySide6.QtCharts import QChartView,QChart,QPieSeries,QPieSlice

class MyWindow(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        chartView = QChartView()
        V = QVBoxLayout(self)
        V.addWidget(chartView)

        self.chart = QChart()
        chartView.setChart(self.chart)
        pieSeries = QPieSeries()
        pieSeries.setLabelsPosition(QPieSlice.LabelOutside)
        pieSeries.setPieStartAngle(90)
        pieSeries.setPieEndAngle(-270)

        first = QPieSlice("第1季度销售额", 32.3)  #创建切片
        second = QPieSlice("第2季度销售额", 22.5)  #创建切片
        second.setExploded(exploded=True)  #爆炸切片
        pieSeries.append(first)  #添加切片
        pieSeries.append(second)  #添加切片
        pieSeries.append("第3季度销售额", 46.3)  #添加切片
        pieSeries.append("第4季度销售额", 52.7)  #添加切片
        pieSeries.setLabelsVisible(visible=True)  #标签可见
        pieSeries.setHoleSize(0.3)  #孔的尺寸
        self.chart.addSeries(pieSeries)  #图表中添加数据序列
if __name__ == '__main__':
    app=QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
