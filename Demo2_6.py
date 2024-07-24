import sys  #Demo2_6.py
from PySide6.QtWidgets import QApplication,QWidget
from PySide6.QtGui import QPainter,QPixmap,QBitmap,QImage,QColor
from PySide6.QtCore import QRect

class ShowPictures(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setWindowTitle("绘图")
        self.pix = QPixmap()
        self.bit = QBitmap()
        self.image = QImage()
        self.pix.load("d:\\python\\pic.png")
        self.bit.load("d:\\python\\pic.png")
        self.image.load("d:\\python\\pic.png")
        #下面创建两个image图像，分别存储灰度图和明亮图
        self.image_1=QImage(self.image.width(),self.image.height(),QImage.Format_ARGB32)
        self.image_2=QImage(self.image.width(),self.image.height(),QImage.Format_ARGB32)

        self.gray()  #调用灰度处理函数
        self.bright()  #调用明亮处理函数
    def paintEvent(self, event):
        w = int(self.width()/2)   #窗口的一半宽度
        h = int(self.height()/2)  #窗口的一半高度
        rect1 = QRect(0,0,w-2,h-2)  #矩形区域1
        rect2 = QRect(w,0,w-2,h-2)  #矩形区域2
        rect3 = QRect(0,h, w-2, h-2)  #矩形区域3
        rect4 = QRect(w,h,w-2,h-2)  #矩形区域4

        painter = QPainter(self)
        painter.drawPixmap(rect1,self.pix)  #在矩形区域1绘图图像
        painter.drawPixmap(rect2,self.bit)  #在矩形区域2绘图图像
        painter.drawImage(rect3,self.image_1)  #在矩形区域3绘图图像
        painter.drawImage(rect4,self.image_2)  #在矩形区域4绘图图像
    def gray(self):  #对图像进行灰度处理
        color = QColor()
        for i in range(1,self.image_1.width()+1):
            for j in range(1,self.image_1.height()+1):
                alpha = self.image.pixelColor(i, j).alpha()  #获取像素点alpha值
                r = self.image.pixelColor(i, j).red()  #获取像素点红色值
                g = self.image.pixelColor(i, j).green() #获取像素点绿色值
                b = self.image.pixelColor(i, j).blue() #获取像素点蓝色值
                average = int((r+g+b)/3)  #取平均值
                color.setRgb(average,average,average,alpha)  #设置颜色
                self.image_1.setPixelColor(i,j,color)  #设置像素点的颜色
        self.image_1.save("d:\\gray.jpg")  #保存文件
    def bright(self): #对图像进行明亮处理
        color = QColor()
        delta = 50  #RGB增加值
        for i in range(1,self.image_1.width()+1):
            for j in range(1,self.image_1.height()+1):
                alpha = self.image.pixelColor(i,j).alpha()
                r = self.image.pixelColor(i, j).red()+ delta
                g = self.image.pixelColor(i, j).green()+ delta
                b = self.image.pixelColor(i, j).blue()+ delta
                if r > 255: r = 255
                if g > 255: g = 255
                if b > 255: b = 255
                color.setRgb(r, g, b, alpha)
                self.image_2.setPixelColor(i,j,color)
        self.image_2.save("d:\\birght.jpg")
if __name__ == '__main__':
    app=QApplication(sys.argv)
    window = ShowPictures()
    window.show()
    sys.exit(app.exec())
