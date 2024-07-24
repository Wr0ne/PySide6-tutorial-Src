import sys  #Demo8_3.py
from PySide6.QtWidgets import QApplication,QWidget,QVBoxLayout,QMenuBar,\
                         QFileDialog,QPlainTextEdit
from PySide6.QtCore import QFile
from PySide6.QtCharts import QChartView,QChart,QLineSeries,QAreaSeries

class MyWindow(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setupUi()
    def setupUi(self):
        menuBar = QMenuBar()
        fileMenu = menuBar.addMenu("文件(&F)")
        fileMenu.addAction("打开(&O)").triggered.connect(self.action_open_triggered)
        fileMenu.addSeparator()
        fileMenu.addAction("退出(&E)").triggered.connect(self.close)
        self.plainText = QPlainTextEdit()
        chartView = QChartView()

        V=QVBoxLayout(self)
        V.addWidget(menuBar);V.addWidget(chartView);V.addWidget(self.plainText)
        self.chart = QChart()
        chartView.setChart(self.chart)
    def action_open_triggered(self):  #读取文件
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
                    temp=list()
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
        lineSeries_1 = QLineSeries()  #创建折线数据序列
        lineSeries_2 = QLineSeries()  #创建折线数据序列
        areaSeries = QAreaSeries()  #创建面积数据序列
        for i in data:
            lineSeries_1.append(i[0], i[1])  #添加数据
            lineSeries_2.append(i[0], i[2])  #添加数据
        areaSeries.setUpperSeries(lineSeries_1)  #设置上数据序列
        areaSeries.setLowerSeries(lineSeries_2)  #设置下数据序列
        self.chart.addSeries(areaSeries)  #图表中添加数据序列
        self.chart.createDefaultAxes()  #创建坐标轴
        areaSeries.setName("面积图")
        color_1 = areaSeries.borderColor()
        color_1.setRgb(255, 0, 0, 255)
        areaSeries.setBorderColor(color_1)
        color_2 = areaSeries.color()
        color_2.setRgb(0, 0, 255, 255)
        areaSeries.setColor(color_2)
        axis_x=self.chart.axisX()
        axis_x.setTitleText("时间")
        axis_y=self.chart.axisY()
        axis_y.setTitleText("加速度")
if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())
