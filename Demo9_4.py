import sys   #Demo9_4.py
from PySide6.QtWidgets import QApplication,QWidget,QPushButton,QVBoxLayout,QHBoxLayout
from PySide6.QtMultimedia import QMediaDevices,QCamera,QMediaCaptureSession
from PySide6.QtMultimediaWidgets import QVideoWidget

class MyWindow(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.resize(800,600)
        self.setupUi()
    def  setupUi(self):  #界面
        self.videoWidget=QVideoWidget()  #显示视频的控件
        self.btn_start=QPushButton("启动摄像头")  #打开摄像头按钮
        self.btn_stop=QPushButton("停止摄像头")  #停止摄像头按钮
        h=QHBoxLayout()  #按钮水平布局
        h.addWidget(self.btn_start)
        h.addWidget(self.btn_stop)
        v=QVBoxLayout(self)  #竖直布局
        v.addWidget(self.videoWidget)
        v.addLayout(h)

        self.mediaDevice = QMediaDevices(self)   #媒体设备
        self.cameraDevice = self.mediaDevice.defaultVideoInput() #获取默认的视频输入设备
        self.camera = QCamera(self.cameraDevice)  #根据视频输入设备定义视频接口
        self.mediaCaptureSession = QMediaCaptureSession(self)  #媒体捕获器
        self.mediaCaptureSession.setCamera(self.camera)  #设置媒体捕获器的视频接口
        self.mediaCaptureSession.setVideoOutput(self.videoWidget)#设置捕获器的视频输出控件

        self.btn_start.clicked.connect(self.camera.start)  #信号与槽连接
        self.btn_stop.clicked.connect(self.camera.stop)    #信号与槽连接
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
