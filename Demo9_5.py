import sys   #Demo9_5.py
from PySide6.QtWidgets import QApplication,QWidget,QPushButton,QVBoxLayout,\
         QHBoxLayout,QFileDialog
from PySide6.QtMultimedia import QMediaDevices,QCamera,QMediaCaptureSession,\
         QMediaRecorder,QMediaPlayer,QAudioInput,QAudioOutput,QMediaFormat
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtCore import QFileInfo

class MyWindow(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.resize(800,600)
        self.setupUi()
    def  setupUi(self):  #界面
        self.videoWidget = QVideoWidget()  #显示视频的控件
        self.btn_camera = QPushButton("启动摄像头")  #打开/关闭摄像头按钮
        self.btn_recoder = QPushButton("录制视频")  #录制按钮
        self.btn_recoder.setEnabled(False)
        self.btn_palyer = QPushButton("播放录制的视频")  #播放视频按钮
        self.btn_palyer.setEnabled(False)
        h=QHBoxLayout()  #按钮水平布局
        h.addWidget(self.btn_camera)
        h.addWidget(self.btn_recoder)
        h.addWidget(self.btn_palyer)
        v=QVBoxLayout(self)  #竖直布局
        v.addWidget(self.videoWidget)
        v.addLayout(h)

        self.mediaDevice = QMediaDevices(self)    #媒体设备
        self.cameraDevice = self.mediaDevice.defaultVideoInput() #获取默认的视频输入设备
        self.audioInputDevice = self.mediaDevice.defaultAudioInput()
        self.audioOutputDevice = self.mediaDevice.defaultAudioOutput()
        self.camera = QCamera(self.cameraDevice)       #根据视频输入设备定义视频接口
        self.audioInput = QAudioInput(self.audioInputDevice)
        self.audioOutput = QAudioOutput(self.audioOutputDevice)
        self.mediaRecorder = QMediaRecorder(self)  #媒体录制
        self.mediaRecorder.setEncodingMode(QMediaRecorder.ConstantBitRateEncoding)
        self.mediaRecorder.setQuality(QMediaRecorder.NormalQuality)
        self.mediaRecorder.setVideoFrameRate(10)
        self.mediaCaptureSession = QMediaCaptureSession(self)  #媒体捕获器
        self.mediaCaptureSession.setCamera(self.camera)    #设置媒体捕获器的视频接口
        self.mediaCaptureSession.setAudioInput(self.audioInput) #设置媒体捕捉器的音频输入
        self.mediaCaptureSession.setRecorder(self.mediaRecorder) #设置捕获器的媒体录制
        self.mediaPlayer = QMediaPlayer(self)                    #媒体播放器
        self.mediaPlayer.setAudioOutput(self.audioOutput)     #设置媒体播放器的音频输出

        self.btn_camera.clicked.connect(self.btn_camera_clicked)  #信号与槽连接
        self.btn_recoder.clicked.connect(self.btn_recoder_clicked)  #信号与槽连接
        self.btn_palyer.clicked.connect(self.btn_player_clicked)    #信号与槽连接
        self.mediaPlayer.mediaStatusChanged.connect(self.mediaPlayer_mediaStatusChanged)
    def btn_camera_clicked(self):
        if self.btn_camera.text() == "启动摄像头":
            self.mediaCaptureSession.setVideoOutput(self.videoWidget)#设置捕获器的输出控件
            self.camera.start()
            self.btn_recoder.setEnabled(True)
            self.btn_camera.setText("停止摄像头")
            self.btn_recoder.setText("开始录制")
        else:
            self.mediaRecorder.stop()
            self.camera.stop()
            self.btn_recoder.setEnabled(False)
            self.btn_camera.setText("启动摄像头")
    def btn_recoder_clicked(self):
        if self.btn_recoder.text() == "开始录制":
            fileName, filter = QFileDialog.getSaveFileName(self, dir='d:/', #获取保存媒体的文件
                     caption='保存视频', filter="WMV(*.WMV)")
            if fileName:
                path = QFileInfo(fileName).path()              #文件的路径
                name = QFileInfo(fileName).completeBaseName() #文件名称，不含扩展名
                self.btn_palyer.setEnabled(False)
                self.btn_palyer.setText('播放录制的视频')
                self.mediaPlayer.stop()
                self.mediaCaptureSession.setVideoOutput(self.videoWidget)

                self.mediaFormat = QMediaFormat()   #媒体格式
                self.mediaFormat.setVideoCodec(QMediaFormat.VideoCodec.WMV)#设置视频格式
                self.mediaFormat.setAudioCodec(QMediaFormat.AudioCodec.MP3)#设置音频格式
                self.mediaFormat.setFileFormat(QMediaFormat.WMV)   #设置文件格式
                self.mediaRecorder.setMediaFormat(self.mediaFormat)   #设置媒体格式
                self.mediaRecorder.setOutputLocation(path+name)      #设置媒体的保存文件
                self.camera.start()

                self.mediaRecorder.record()   #开始录制音频和视频
                self.btn_recoder.setText("停止录制")
        else:
            self.mediaRecorder.stop()
            self.btn_recoder.setText("开始录制")
            self.btn_palyer.setEnabled(True)
    def btn_player_clicked(self):
        if self.btn_palyer.text() == '播放录制的视频':
            source = self.mediaRecorder.actualLocation()
            self.mediaPlayer.setVideoOutput(self.videoWidget)
            self.mediaPlayer.setSource(source)  # 设置播放器的播放内容
            self.mediaPlayer.play()
            self.btn_palyer.setText("停止播放")
        elif self.btn_palyer.text() == '停止播放':
            self.mediaPlayer.stop()
            self.mediaCaptureSession.setVideoOutput(self.videoWidget)
            self.btn_palyer.setText('播放录制的视频')
    def mediaPlayer_mediaStatusChanged(self,status):
        if status == QMediaPlayer.EndOfMedia:
            self.mediaCaptureSession.setVideoOutput(self.videoWidget)
            self.btn_palyer.setText('播放录制的视频')
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
