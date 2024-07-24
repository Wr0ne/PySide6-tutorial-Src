import sys  #Demo2_4.py
from PySide6.QtWidgets import QApplication, QWidget, QLabel
from PySide6.QtGui import QFont, QColor
from random import randint, seed

class SetPalette(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setGeometry(200,200,1200,500)  #设置窗口尺寸
        self.setWindowTitle("设置调色板实例")
        self.createLabels()  #调用函数
        self.setLabelColor()  #调用函数
        self.getLabelColorRGB()  #调用函数
    def createLabels(self):  #创建10个标签
        self.labels = list()
        font = QFont("黑体",pointSize=20)
        string = "Nice to meet you! 很高兴认识你！"
        for i in range(10):
            label = QLabel(self)  #在窗口上创建标签控件
            label.setGeometry(5,50*i,1200,40)  #标签位置和尺寸
            label.setText(str(i)+': '+string)  #设置标签文字
            label.setFont(font)  #设置标签文字的字体
            self.labels.append(label) #标签列表
    def setLabelColor(self):
        seed(12)
        for label in self.labels:
            colorBase = QColor(randint(0,255), randint(0,255), randint(0,255))  #定义颜色
            colorText = QColor(randint(0,255), randint(0,255), randint(0,255))  #定义颜色
            palette = label.palette()
            palette.setColor(palette.Active,palette.Window,colorBase)  #定义背景色
            palette.setColor(palette.Active,palette.WindowText,colorText) #定义前景色
            label.setAutoFillBackground(True)  #设置背景自动填充
            label.setPalette(palette)  #设置调色板
    def getLabelColorRGB(self):  #获取标签前景颜色和背景颜色RGB值
        for label in self.labels:
            r,g,b,a = label.palette().window().color().getRgb()  #获取背景颜色的RGB值
            rT,gT,bT,a = label.palette().windowText().color().getRgb()#获取文字颜色的RGB值
            text = (label.text()+"背景颜色：{} {} {} 文字颜色：{} {} {}").format(r,g,b,rT,gT,bT)
            label.setText(text)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SetPalette()
    window.show()
    sys.exit(app.exec())
