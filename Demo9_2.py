import sys   #Demo9_2.py
from PySide6.QtWidgets import QApplication,QPushButton,QVBoxLayout,\
       QHBoxLayout,QFileDialog,QWidget,QGraphicsView,QGraphicsScene
from PySide6.QtCore import QUrl,Qt
from PySide6.QtMultimedia import QMediaPlayer,QAudioOutput
from PySide6.QtMultimediaWidgets import QVideoWidget,QGraphicsVideoItem

class MyVideoWidget(QVideoWidget): #建立QVideoWidget的子类，重新keyPressEvent()事件
    def __init__(self,parent=None):
        super().__init__(parent)
    def keyPressEvent(self,event):  #全屏后按Esc键回到原状态
        if event.key() == Qt.Key_Escape and self.isFullScreen():
            self.setFullScreen(False)
    def mouseDoubleClickEvent(self,event): #双击全屏显示
        if not self.isFullScreen():
            self.setFullScreen(True)
        else:
            self.setFullScreen(False)
class MyWindow(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.resize(800,400)
        self.setupUi()
    def  setupUi(self):  #界面
        self.videoWidget = MyVideoWidget()  #显示视频的控件
        self.videoItem = QGraphicsVideoItem()

        self.graphicsView = QGraphicsView()  # 视图窗口
        self.graphicsScene = QGraphicsScene()  # 创建场景
        self.graphicsView.setScene(self.graphicsScene)  # 视图窗口设置场景
        self.videoItem = QGraphicsVideoItem()  # 视频图项
        self.videoItem.setFlags(self.videoItem.ItemIsSelectable | self.videoItem.ItemIsMovable)
        self.graphicsScene.addItem(self.videoItem)  # 场景中添加视频图项

        H = QHBoxLayout()
        H.addWidget(self.videoWidget,stretch=1)
        H.addWidget(self.graphicsView,stretch=1)
        self.btn_open=QPushButton("打开媒体文件")  #打开音频或视频按钮
        self.btn_play_stop=QPushButton("播放/停止")  #播放/停止按钮
        self.btn_play_stop.setEnabled(False)
        self.btn_pause_continue = QPushButton("暂停/继续")  #暂停/继续按钮
        self.btn_pause_continue.setEnabled(False)
        self.btn_mute=QPushButton("静音")  #静音按钮
        self.btn_fullScreen = QPushButton("全屏")
        h=QHBoxLayout()  #按钮水平布局
        h.addWidget(self.btn_open)
        h.addWidget(self.btn_play_stop)
        h.addWidget(self.btn_pause_continue)
        h.addWidget(self.btn_mute)
        h.addWidget(self.btn_fullScreen)
        v=QVBoxLayout(self)  #竖直布局
        v.addLayout(H)
        v.addLayout(h)

        self.player_1 = QMediaPlayer(self)  #音频和视频播放器
        self.player_2 = QMediaPlayer(self)  # 音频和视频播放器
        self.audioOupt = QAudioOutput()  # 播放音频设备
        self.audioOupt.setVolume(0.5)
        self.player_1.setVideoOutput(self.videoWidget)  #设置播放器的视频输出控件
        self.player_2.setVideoOutput(self.videoItem)  # 设置播放器的视频图项
        self.player_1.setAudioOutput(self.audioOupt)    #设置播放器的音频输出设备
        self.player_1.hasAudioChanged.connect(self.has_audioVideo_changed)#音频信号的连接
        self.player_1.hasVideoChanged.connect(self.has_audioVideo_changed)#视频信号的连接
        self.btn_open.clicked.connect(self.btn_open_clicked)  #打开媒体文件的信号与槽连接
        self.btn_play_stop.clicked.connect(self.btn_play_stop_clicked)#播放/停止按钮的连接
        self.btn_pause_continue.clicked.connect(self.btn_pause_continue_clicked)
        self.btn_mute.clicked.connect(self.btn_mute_clicked)  #静音按钮的信号与槽连接
        self.btn_fullScreen.clicked.connect(self.btn_fullScreen_clicked)
    def btn_open_clicked(self):  #打开按钮的槽函数
        fileName,fil=QFileDialog.getOpenFileName(self,caption="选择影音文件",dir="d:\\",
        filter="影音文件(*.wav *.mp4 *.mp3 *.wma *.avi *.wmv *.rm *.asf);;所有文件(*.*)")
        if fileName:
            url=QUrl.fromLocalFile(fileName)
            self.player_1.setSource(url)  #设置播放器的播放内容
            self.player_2.setSource(url)  #设置播放器的播放内容
    def has_audioVideo_changed(self,has): #有音频和视频时的槽函数
        if has:
            self.btn_play_stop.setEnabled(True)
            self.btn_play_stop.setText('播放')
        else:
            self.btn_play_stop.setEnabled(False)
            self.btn_play_stop.setText('播放/停止')
    def btn_play_stop_clicked(self):  #播放/停止按钮的槽函数
        if self.btn_play_stop.text()=="播放":
            self.player_1.play()
            self.player_2.play()
            self.btn_play_stop.setText("停止")
            self.btn_pause_continue.setEnabled(True)
            self.btn_pause_continue.setText('暂停')
        elif self.btn_play_stop.text()=="停止":
            self.player_1.stop()
            self.player_2.stop()
            self.btn_play_stop.setText("播放")
            self.btn_pause_continue.setEnabled(False)
            self.btn_pause_continue.setText('暂停/继续')
    def btn_pause_continue_clicked(self):  #暂停/继续按钮的槽函数
        if self.btn_pause_continue.text()=="暂停":
            self.player_1.pause()
            self.player_2.pause()
            self.btn_pause_continue.setText("继续")
        elif self.btn_pause_continue.text()=="继续":
            self.player_1.play()
            self.player_2.play()
            self.btn_pause_continue.setText("暂停")
    def btn_mute_clicked(self):  #静音按钮的槽函数
        muted=self.audioOupt.isMuted()
        self.audioOupt.setMuted(not muted)
        if muted:
            self.btn_mute.setText("放音")
        else:
            self.btn_mute.setText("静音")
    def btn_fullScreen_clicked(self): #全屏按钮的槽函数
        self.videoWidget.setFullScreen(True)
    def resizeEvent(self,event):
        self.videoItem.setSize(self.graphicsView.size())
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
