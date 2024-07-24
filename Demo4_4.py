import sys  #Demo4_4.py
from PySide6.QtWidgets import QApplication,QWidget,QFileDialog,QMenuBar
from PySide6.QtGui import QPixmap,QPainter
from PySide6.QtCore import QRect,QPoint,Qt

class MyWindow(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)  #设置成接受拖放事件
        self.resize(600,600)
        self.pixmap = QPixmap()  #创建QPixmap图像
        self.pix_width = 0  #获取初始宽度
        self.pix_height = 0  #获取初始高度
        self.translate_x = 0  #用于控制x向平移
        self.translate_y = 0  #用于控制y向平移
        self.pixmap_scale_x = 0.0 #用于记录图象的长度比例，用于图像缩放
        self.pixmap_scale_y = 0.0  #用于记录图象的高度比例，用于图像缩放
        self.start=QPoint(0,0)  #鼠标单击时光标位置
        # 记录图像中心的变量，初始定义在窗口的中心
        self.center = QPoint(int(self.width() / 2), int(self.height() / 2))
        menuBar = QMenuBar(self)
        menuFile = menuBar.addMenu("文件(&F)")
        menuFile.addAction("打开(&O)").triggered.connect(self.actionOpen_triggered)
        menuFile.addSeparator()
        menuFile.addAction("退出(&E)").triggered.connect(self.close)  #动作与槽连接
    def paintEvent(self,event): #窗口绘制处理函数，当窗口刷新时调用该函数
        self.center=QPoint(self.center.x()+self.translate_x, self.center.y()+self.translate_y)
        #图像绘制区域的左上角点，用于缩放图像
        point_1 = QPoint(self.center.x() - self.pix_width, self.center.y() - self.pix_height)
        # 图像绘制区域的右下角点，用于缩放图像
        point_2 = QPoint(self.center.x() + self.pix_width, self.center.y() + self.pix_height)
        self.rect = QRect(point_1, point_2)  #图像绘制区域
        painter = QPainter(self)  # 绘图
        painter.drawPixmap(self.rect,self.pixmap)
    def mousePressEvent(self, event):  #鼠标按键按下事件的处理函数
        self.start=event.pos()  #鼠标位置
    def mouseMoveEvent(self,event): #鼠标移动事件的处理函数
        if event.modifiers() == Qt.ControlModifier and event.buttons()==Qt.LeftButton:
            self.translate_x = event.x()-self.start.x()  #鼠标的移动量
            self.translate_y = event.y()-self.start.y()  #鼠标的移动量
            self.start = event.pos()
            self.update()  #会调用paintEvent()
    def wheelEvent(self,event): #鼠标滚轮事件的处理函数
       if event.modifiers() == Qt.ControlModifier:
         if (self.pix_width>10 and self.pix_height>10) or event.angleDelta().y()>0:
           self.pix_width=self.pix_width+int(event.angleDelta().y()/10*self.pixmap_scale_x)
           self.pix_height=self.pix_height+int(event.angleDelta().y()/10*self.pixmap_scale_y)
           self.update()  #会调用paintEvent()
    def mouseDoubleClickEvent(self, event): #双击鼠标事件的处理函数
        self.actionOpen_triggered()
    def actionOpen_triggered(self):  #打开文件的动作
        fileDialog = QFileDialog(self)
        fileDialog.setNameFilter("图像文件(*.png *.jpeg *.jpg)")
        fileDialog.setFileMode(QFileDialog.ExistingFile)
        if fileDialog.exec():
            self.pixmap.load(fileDialog.selectedFiles()[0])
            self.pix_width = int(self.pixmap.width() / 2)   #获取初始宽度
            self.pix_height = int(self.pixmap.height() / 2)  #获取初始高度
            self.pixmap_scale_x = self.pix_width/(self.pix_width+self.pix_height)
            self.pixmap_scale_y = self.pix_height/(self.pix_width+self.pix_height)
            self.center = QPoint(int(self.width() / 2), int(self.height() / 2))
            self.update()
    def dragEnterEvent(self,event):  #拖动进入事件
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()
    def dropEvent(self,event):  #释放事件
        urls = event.mimeData().urls()  #获取被拖动文件的地址列表
        fileName = urls[0].toLocalFile()  #将文件地址转成本地地址
        self.pixmap.load(fileName)
        self.pix_width = int(self.pixmap.width() / 2)   #获取初始宽度
        self.pix_height = int(self.pixmap.height() / 2)  #获取初始高度
        self.pixmap_scale_x = self.pix_width / (self.pix_width + self.pix_height)
        self.pixmap_scale_y = self.pix_height / (self.pix_width + self.pix_height)
        self.center = QPoint(int(self.width() / 2), int(self.height() / 2))
        self.update()
if __name__ == '__main__':
    app=QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
