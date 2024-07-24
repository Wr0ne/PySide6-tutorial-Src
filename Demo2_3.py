import sys  #Demo2_3.py
from PySide6.QtWidgets import QApplication,QWidget,QLabel
from PySide6.QtGui import QFont

class TestFont(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setGeometry(200,200,800,600)  #设置窗口尺寸
        self.createFont()  #调用函数
        self.createLabels()  #调用函数
        self.getLabelFont()  #调用函数
    def createFont(self):  #生成10个字体
        self.fonts = list()  #字体列表
        fontName=('宋体','仿宋','黑体','楷体','隶书','幼圆','华文中宋','方正舒体', '华文黑体', 'Times New Roman')
        for i in range(10):
            f = QFont()
            f.setPointSizeF(25.5)
            f.setFamily(fontName[i])
            self.fonts.append(f)
        self.fonts[0].setBold(True)
        self.fonts[1].setItalic(True)
        self.fonts[2].setStrikeOut(True)
        self.fonts[3].setOverline(True)
        self.fonts[4].setUnderline(True)
        self.fonts[5].setCapitalization(QFont.AllUppercase)
        self.fonts[6].setWeight(QFont.Thin)
        self.fonts[7].setWordSpacing(50)
        self.fonts[8].setStretch(70)
        self.fonts[9].setPixelSize(50)
    def createLabels(self):
        self.labels = list()
        string = "Nice to Meet You! 很高兴认识你！"
        for i in range(10):
            label = QLabel(self)  #在窗口上创建标签控件
            label.setGeometry(0,50*i,800,70)  #标签位置和尺寸
            label.setText(str(i)+': '+string)  #设置标签文字
            label.setFont(self.fonts[i])  #设置标签文字的字体
            self.labels.append(label) #标签列表
    def getLabelFont(self):  #获取每个字体的信息
        print("字体信息：")
        template="Label {}, family:{}, Bold:{}, Italic:{}, StrikeOut:{}, OverLine:{}, UnderLine:{}, " \
            "Capitalization:{}, Weight:{}, WordSpacing:{}, Stretch:{}, PixelSize:{}, PointSize:{}"
        j = 0
        for i in self.labels:
            f = i.font()  #获取标签的字体
            print(template.format(j,f.family(),f.bold(),f.italic(),f.strikeOut(),f.overline(),f.underline(),
            f.capitalization(),f.weight(),f.wordSpacing(),f.stretch(),f.pixelSize(),f.pointSize()))
            j = j+1
if __name__ == '__main__':
    app=QApplication(sys.argv)
    font = app.font()  #获取程序默认的字体
    font.setFamily('Helvetica [Cronyx]')  #设置字体名称
    app.setFont(font)  #设置程序默认的字体
    window = TestFont()
    window.show()
    sys.exit(app.exec())
