import sys   #Demo9_6.py
from PySide6.QtWidgets import QApplication,QWidget,QPushButton,QVBoxLayout,\
         QHBoxLayout,QFileDialog
from PySide6.QtMultimedia import QMediaDevices,QCamera,QMediaCaptureSession,QImageCapture
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtGui import QPainter,QColor
from PySide6.QtCore import QRectF

class ImagePreview(QWidget):  #自定义控件，用于显示图像
    def __init__(self,parent=None):
        super().__init__(parent)
        self.image = None    #该变量用于接收图像
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(palette.Window,QColor(0,0,0))
        self.setPalette(palette)
    def paintEvent(self,event):  #绘制事件
        if self.image:
            center_x = self.width()/2; center_y = self.height()/2
            image_width = self.image.size().width()
            image_height = self.image.size().height()
            if image_width/image_height>=self.width()/self.height():
                w = self.width(); h = w*image_height/image_width
            else:
                h = self.height(); w = h*image_width/image_height
            rectF = QRectF(center_x-w/2,center_y-h/2,w,h)
            painter = QPainter(self)
            painter.drawImage(rectF,self.image)  #在指定的范围绘制图像
class MyWindow(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.resize(1000,500)
        self.setupUi()
        self.imageCapturedList = list()  #该列表用于记录拍摄的照片
    def  setupUi(self):  #界面
        self.videoWidget = QVideoWidget()  #显示摄像头画面的控件
        self.imagePreview = ImagePreview() #自定义的显示图像的控件
        H1 = QHBoxLayout()   #水平布局
        H1.addWidget(self.videoWidget,stretch=1)
        H1.addWidget(self.imagePreview,stretch=1)
        self.btn_camera = QPushButton("启动摄像头")  #打开/关闭摄像头按钮
        self.btn_image = QPushButton("拍照")  #拍照按钮
        self.btn_previous = QPushButton("<< 前一个")  #显示前一个图形的按钮
        self.btn_next = QPushButton("后一个 >>")   #显示后一个图像的按钮
        self.btn_save = QPushButton("保存图像")    #保存图像的按钮
        self.btn_delete = QPushButton("删除照片")  #删除图像的按钮
        self.btn_image.setEnabled(False); self.btn_previous.setEnabled(False)
        self.btn_next.setEnabled(False); self.btn_save.setEnabled(False)
        self.btn_delete.setEnabled(False)
        H2 = QHBoxLayout()  #水平布局
        H2.addWidget(self.btn_camera); H2.addWidget(self.btn_image)
        H2.addWidget(self.btn_previous); H2.addWidget(self.btn_next)
        H2.addWidget(self.btn_save); H2.addWidget(self.btn_delete)
        V = QVBoxLayout(self)  #竖直布局
        V.addLayout(H1); V.addLayout(H2)

        self.mediaDevice = QMediaDevices(self)    #媒体设备
        self.cameraDevice = self.mediaDevice.defaultVideoInput() #获取默认的视频输入设备
        self.camera = QCamera(self.cameraDevice)    #根据视频输入设备定义视频接口
        self.imageCapture = QImageCapture(self)     #图像捕捉器
        self.mediaCaptureSession = QMediaCaptureSession(self)    #媒体捕获器
        self.mediaCaptureSession.setCamera(self.camera)  #设置媒体捕获器的视频接口
        self.mediaCaptureSession.setImageCapture(self.imageCapture) #设置图像捕捉
        self.mediaCaptureSession.setVideoOutput(self.videoWidget)  #设置视频输出控件

        self.btn_camera.clicked.connect(self.btn_camera_clicked)     #信号与槽函数连接
        self.btn_image.clicked.connect(self.imageCapture.capture)    #信号与槽函数连接
        self.imageCapture.imageCaptured.connect(self.image_captured)#信号与槽函数连接
        self.imageCapture.setQuality(QImageCapture.VeryHighQuality) #信号与槽函数连接
        self.btn_previous.clicked.connect(self.btn_previous_clicked)   #信号与槽函数连接
        self.btn_next.clicked.connect(self.btn_next_clicked)          #信号与槽函数连接
        self.btn_save.clicked.connect(self.btn_save_clicked)          #信号与槽函数连接
        self.btn_delete.clicked.connect(self.btn_delete_clicked)       #信号与槽函数连接
    def btn_camera_clicked(self):  #“开启/关闭摄像头”按钮的槽函数
        if self.btn_camera.text() == "启动摄像头":
            self.camera.start()
            self.btn_image.setEnabled(True)
            self.btn_camera.setText("停止摄像头")
        else:
            self.camera.stop()
            self.btn_image.setEnabled(False)
            self.btn_camera.setText("启动摄像头")
    def image_captured(self,id,image):  #“拍照”按钮的槽函数
        self.imageCapturedList.append(image)
        self.imagePreview.image = image
        self.imagePreview.update()
        self.btn_save.setEnabled(True); self.btn_delete.setEnabled(True)
        if len(self.imageCapturedList)>1:
            self.btn_previous.setEnabled(True); self.btn_next.setEnabled(True)
        else:
            self.btn_previous.setEnabled(False); self.btn_next.setEnabled(False)
    def btn_previous_clicked(self):  #“前一个”按钮的槽函数
        index = self.imageCapturedList.index(self.imagePreview.image)
        self.imagePreview.image = self.imageCapturedList[index-1]
        self.imagePreview.update()
    def btn_next_clicked(self):  #“后一个”按钮的槽函数
        index = self.imageCapturedList.index(self.imagePreview.image)
        if index == len(self.imageCapturedList)-1:
            self.imagePreview.image = self.imageCapturedList[0]
        else:
            self.imagePreview.image = self.imageCapturedList[index + 1]
        self.imagePreview.update()
    def btn_save_clicked(self):  #“保存”按钮的槽函数
        if self.imagePreview.image:
            fileName,filter=QFileDialog.getSaveFileName(self,dir='d:/', #获取保存媒体的文件
             caption='保存图片',filter="jpeg(*.jpeg);;png(*.png);;bmp(*.bmp);;tiff(*.tiff)")
            self.imagePreview.image.save(fileName)
    def btn_delete_clicked(self):  #“删除”按钮的槽函数
        index = self.imageCapturedList.index(self.imagePreview.image)
        self.imageCapturedList.pop(index)
        if len(self.imageCapturedList) == 0:
            self.imagePreview.image=None;
            self.imagePreview.update()
            self.btn_delete.setEnabled(False); self.btn_save.setEnabled(False)
            return
        if len(self.imageCapturedList) <= 1:
            self.btn_previous.setEnabled(False); self.btn_next.setEnabled(False)
        self.imagePreview.image = self.imageCapturedList[index-1]
        self.imagePreview.update()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
