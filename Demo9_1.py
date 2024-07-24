import sys   #Demo9_1.py
from PySide6.QtWidgets import QApplication,QPushButton,QVBoxLayout,\
                      QHBoxLayout,QFileDialog,QWidget,QSlider
from PySide6.QtCore import QUrl,Qt
from PySide6.QtMultimedia import QMediaPlayer,QAudioOutput
from PySide6.QtMultimediaWidgets import QVideoWidget

class MyWindow(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.resize(800,600)
        self.setupUi()
    def  setupUi(self):  #界面
        self.videoWidget=QVideoWidget()  #显示视频的控件        
        self.audioOutput = QAudioOutput()  #播放音频设备
        self.audioOutput.setVolume(0.5)
        self.btn_open=QPushButton("打开媒体文件")  #打开音频或视频按钮
        self.btn_play_stop=QPushButton("播放/停止")  #播放/停止按钮
        self.btn_play_stop.setEnabled(False)
        self.btn_pause_continue = QPushButton("暂停/继续")  #暂停/继续按钮
        self.btn_pause_continue.setEnabled(False)
        self.btn_mute=QPushButton("静音")  #静音按钮
        self.progress_slider=QSlider(Qt.Horizontal)  #播放进度滑块
        self.progress_slider.setSingleStep(1)
        self.volume_slider=QSlider(Qt.Horizontal)  #音量控制滑块
        self.volume_slider.setRange(0,100)
        self.volume_slider.setValue(50)
        self.volume_slider.setTickInterval(5)
        self.volume_slider.setTickPosition(QSlider.TicksAbove)
        self.playback_rate_slider=QSlider(Qt.Horizontal)  #播放速率控制滑块
        self.playback_rate_slider.setRange(-100,100)
        self.playback_rate_slider.setValue(20)
        self.playback_rate_slider.setTickInterval(5)
        self.playback_rate_slider.setTickPosition(QSlider.TicksAbove)
        h=QHBoxLayout()  #按钮水平布局
        h.addWidget(self.btn_open)
        h.addWidget(self.btn_play_stop)
        h.addWidget(self.btn_pause_continue)
        h.addWidget(self.btn_mute)
        h.addWidget(self.volume_slider)
        h.addWidget(self.playback_rate_slider)
        v=QVBoxLayout(self)  #竖直布局
        v.addWidget(self.videoWidget)
        v.addWidget(self.progress_slider)
        v.addLayout(h)
        self.player=QMediaPlayer(self)  #音频和视频播放器
        self.player.setVideoOutput(self.videoWidget)  #设置播放器的视频输出控件
        self.player.setAudioOutput(self.audioOutput)    #设置播放器的音频输出设备
        self.player.hasAudioChanged.connect(self.has_audio_video_changed)#信号连接
        self.player.hasVideoChanged.connect(self.has_audio_video_changed)#信号连接
        self.btn_open.clicked.connect(self.btn_open_clicked)  #信号与槽连接
        self.btn_play_stop.clicked.connect(self.btn_play_stop_clicked)#信号与槽连接连接
        self.btn_pause_continue.clicked.connect(self.btn_pause_continue_clicked)
        self.btn_mute.clicked.connect(self.btn_mute_clicked)  #信号与槽连接
        self.progress_slider.actionTriggered.connect(self.player_setPosition)#信号与槽连接
        self.player.durationChanged.connect(self.player_duration_changed) #信号与槽连接
        self.volume_slider.valueChanged.connect(self.player_setVolume) #信号与槽连接
        self.playback_rate_slider.valueChanged.connect(self.player_setPlayRate) #信号连接
        self.player.positionChanged.connect(self.progress_slider.setValue) #信号与槽连接
    def btn_open_clicked(self):  #打开按钮的槽函数
        fileName,fil=QFileDialog.getOpenFileName(self,caption="选择影音文件",dir="d:\\",
       filter="影音文件(*.wav *.mp4 *.mp3 *.wma *.avi *.wmv *.rm *.asf);;所有文件(*.*)")
        if fileName:
            url=QUrl.fromLocalFile(fileName)
            self.player.setSource(url)  #设置播放器的播放内容
            self.progress_slider.setValue(0)
            self.playback_rate_slider.setValue(20)
    def has_audio_video_changed(self,has): #有音频和视频时的槽函数
        if has:
            self.btn_play_stop.setEnabled(True)
            self.btn_play_stop.setText('播放')
        else:
            self.btn_play_stop.setEnabled(False)
            self.btn_play_stop.setText('播放/停止')
    def btn_play_stop_clicked(self):  #播放/停止按钮的槽函数
        if self.btn_play_stop.text()=="播放":
            self.player.play()
            self.btn_play_stop.setText("停止")
            self.btn_pause_continue.setEnabled(True)
            self.btn_pause_continue.setText('暂停')
        elif self.btn_play_stop.text()=="停止":
            self.player.stop()
            self.btn_play_stop.setText("播放")
            self.btn_pause_continue.setEnabled(False)
            self.btn_pause_continue.setText('暂停/继续')
        self.progress_slider.setValue(0)
        self.playback_rate_slider.setValue(20)
    def btn_pause_continue_clicked(self):  #暂停/继续按钮的槽函数
        if self.btn_pause_continue.text()=="暂停":
            self.player.pause()
            self.btn_pause_continue.setText("继续")
        elif self.btn_pause_continue.text()=="继续":
            self.player.play()
            self.btn_pause_continue.setText("暂停")
    def btn_mute_clicked(self):  #静音按钮的槽函数
        muted=self.audioOupt.isMuted()
        self.audioOupt.setMuted(not muted)
        if self.audioOupt.isMuted():
            self.btn_mute.setText("放音")
        else:
            self.btn_mute.setText("静音")
    def player_duration_changed(self,duration):  #播放器播放时长的槽函数
        self.progress_slider.setRange(0,duration)
    def player_setPosition(self,action):
        self.player.setPosition(self.progress_slider.value())
    def player_setVolume(self, value):  #音量滑块的槽函数
        self.audioOupt.setVolume(value/100)
    def player_setPlayRate(self):  #播放速率滑块的槽函数
        if self.player.hasVideo():
            self.player.setPlaybackRate(self.playback_rate_slider.value()/20)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
