import sys  #Demo2_12.py
from PySide6.QtWidgets import (QApplication,QWidget,QPushButton,QLabel,QComboBox,
QHBoxLayout, QVBoxLayout,QSpacerItem,QSizePolicy,QFileDialog)
from PySide6.QtGui import QPainter,QBitmap,QImage,QPixmap,QColor,QIcon
from PySide6.QtCore import QRect,Qt

class MyWindow(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setWindowTitle("QComoBox例子")
        self.resize(500, 400)
        self.setupUi()  #调用函数
    def setupUi(self):  #建立界面上的控件
        self.pushButton = QPushButton("选择图形文件",self)
        self.label_1 = QLabel("图片显示方式")
        self.label_2 = QLabel("图片明亮度")
        self.comboBox_1 = QComboBox()
        self.comboBox_2 = QComboBox()
        for i in range(160, -220, -20):
            self.comboBox_2.addItem(str(i))

        self.horizontalLayout = QHBoxLayout()  #水平布局控件
        self.horizontalLayout.addWidget(self.pushButton)
        self.horizontalLayout.addWidget(self.label_1)
        self.horizontalLayout.addWidget(self.comboBox_1)
        self.horizontalLayout.addWidget(self.label_2)
        self.horizontalLayout.addWidget(self.comboBox_2)

        self.verticalLayout = QVBoxLayout(self)  #竖直布局控件
        spacerItem = QSpacerItem(20, 300, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.comboBox_1.setEnabled(False)
        self.comboBox_2.setEnabled(False)

        self.pushButton.clicked.connect(self.openImage)  #按钮信号与槽函数的关联
    def openImage(self):  #按钮的槽函数
        name,filter=QFileDialog.getOpenFileName(self, "选择文件", "d:\\", "图像(*.png *.jpg)")
        if len(name)>0:
            self.comboBox_1.clear() #清空item
            self.image = QImage(name)
            self.bitmap = QBitmap(name).toImage()
            w = self.image.width()
            h = self.image.height()
            self.gray_image = QImage(w,h,QImage.Format_ARGB32) #创建灰色图片
            self.gray()  #调用函数，完成灰色图片
            self.bright_image = QImage(w,h,QImage.Format_ARGB32)  #创建明亮图标
            self.bright()  #调用函数，完成明亮图片
            #添加item，包含图标和关联数据
            self.comboBox_1.addItem(QIcon(QPixmap().fromImage(self.image)),
                                    "原始图片", userData=self.image)
            self.comboBox_1.addItem(QIcon(QPixmap().fromImage(self.bitmap)),
                                    "单色图片", userData=self.bitmap)
            self.comboBox_1.addItem(QIcon(QPixmap().fromImage(self.gray_image)),
                                    "灰色图片", userData=self.gray_image)
            self.comboBox_1.addItem(QIcon(QPixmap().fromImage(self.bright_image)),
                                    "明亮图片", userData=self.bright_image)
            self.comboBox_1.setEnabled(True)
                #comboBox信号与槽的关联
            self.comboBox_1.currentTextChanged[str].connect(self.comboBox_1_changed)
            self.comboBox_2.currentTextChanged[str].connect(self.comboBox_2_changed)
        else:
            self.comboBox_1.setEnabled(False)
            self.comboBox_2.setEnabled(False)
    def gray(self):  #对图像进行灰度处理
        color = QColor()
        for i in range(1,self.image.width()+1):
            for j in range(1,self.image.height()+1):
                alpha = self.image.pixelColor(i, j).alpha()  #获取像素点alpha值
                r = self.image.pixelColor(i, j).red()  #获取像素点红色值
                g = self.image.pixelColor(i, j).green() #获取像素点绿色值
                b = self.image.pixelColor(i, j).blue() #获取像素点蓝色值
                average = int((r+g+b)/3)  #取平均值
                color.setRgb(average,average,average,alpha)  #设置颜色
                self.gray_image.setPixelColor(i,j,color)  #设置像素点的颜色
    def bright(self): #对图像进行明亮处理
        color = QColor()
        delta = 60  #RGB变化的初始值
        if self.comboBox_2.isEnabled():
            delta = int(self.comboBox_2.currentText())
        for i in range(1,self.image.width()+1):
            for j in range(1,self.image.height()+1):
                alpha = self.image.pixelColor(i,j).alpha()
                r = self.image.pixelColor(i, j).red()+ delta
                g = self.image.pixelColor(i, j).green()+ delta
                b = self.image.pixelColor(i, j).blue()+ delta
                if r > 255: r = 255
                if g > 255: g = 255
                if b > 255: b = 255
                if r < 0: r = 0
                if g < 0: g = 0
                if b < 0: b = 0
                color.setRgb(r, g, b, alpha)
                self.bright_image.setPixelColor(i,j,color)
        self.comboBox_1.setItemData(3,self.bright_image,role=Qt.UserRole)
    def comboBox_1_changed(self,text):  #槽函数
        if text == "明亮图片":
            self.comboBox_2.setEnabled(True)
            self.bright()   #重新生成明亮图片
        else:
            self.comboBox_2.setEnabled(False)
        self.update()  #刷新屏幕
    def comboBox_2_changed(self,text):  #槽函数
        self.bright()  #重新生成明亮图片
        self.update()  #刷新屏幕
    def paintEvent(self,event):  #绘制屏幕图片
        if self.comboBox_1.isEnabled():
            rect = QRect(0,0,self.width(),self.height()-50)
            painter = QPainter(self)
            index = self.comboBox_1.currentIndex()
            painter.drawImage(rect,self.comboBox_1.itemData(index))
if __name__ == '__main__':
    app=QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
