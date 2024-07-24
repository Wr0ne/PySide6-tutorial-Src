import sys  #Demo8_2.py
from PySide6.QtWidgets import  QApplication,QWidget,QVBoxLayout,QMenuBar,\
                         QFileDialog,QPlainTextEdit
from PySide6.QtCore import QFile
from PySide6.QtCharts import QChartView,QChart,QLineSeries,QSplineSeries,QScatterSeries

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
        self.plainText = QPlainTextEdit()
        chartView = QChartView()
        v=QVBoxLayout(self)
        v.addWidget(menuBar)
        v.addWidget(chartView)
        v.addWidget(self.plainText)
        self.chart = QChart()
        chartView.setChart(self.chart)
    def action_open_triggered(self):
        fileName,fil=QFileDialog.getOpenFileName(self,"打开测试文件","d:/","文本文件(*.txt)")
        file = QFile(fileName)
        data=list()
        if file.exists():
            file.open(QFile.ReadOnly | QFile.Text)  # 打开文件
            self.plainText.clear()
            try:
                while not file.atEnd():
                    string = file.readLine()  # 按行读取
                    string = str(string, encoding='utf-8').strip()  # 转成字符串
                    self.plainText.appendPlainText(string)
                    temp = list()
                    for i in string.split():
                        temp.append(float(i))  #转成浮点数，并添加数据
                    data.append(temp)

                self.chart.removeAllSeries()  #移除现有曲线
                self.plot(data)  #调用函数，绘制曲线
            except:
                self.plainText.appendPlainText('打开文件出错！')
            finally:
                file.close()
    def plot(self,data):  #绘制图表的函数
        lineSeries = QLineSeries()  #创建折线数据序列
        splineSeries = QSplineSeries()  #创建样条数据序列
        scatterSeries = QScatterSeries()  #创建散点数据序列
        lineSeries.setName("折线图")
        splineSeries.setName("样条曲线图")
        scatterSeries.setName("散点图")
        scatterSeries.setMarkerShape(QScatterSeries.MarkerShapeStar)
        scatterSeries.setBestFitLineVisible(True)  #逼近线
        for i in data:
            lineSeries.append(i[0], i[1])  #添加数据
            splineSeries.append(i[0], i[1])  #添加数据
            scatterSeries.append(i[0], i[2])  #添加数据
        self.chart.addSeries(lineSeries)  #图表中添加数据序列
        self.chart.addSeries(splineSeries)  #图表中添加数据序列
        self.chart.addSeries(scatterSeries)  #图表中添加数据序列
        self.chart.createDefaultAxes()  #创建坐标轴
if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())
