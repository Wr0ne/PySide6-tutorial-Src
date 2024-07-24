import sys  #Demo2_27.py
from PySide6.QtWidgets import QApplication,QWidget,QLabel,QPushButton,QLineEdit,\
                              QHBoxLayout,QVBoxLayout,QTabWidget,QProgressBar
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import QUrl,Qt
from PySide6.QtGui import QIcon

class WidgetInTab(QWidget):  #切换卡中的控件
    def __init__(self,parent=None,tab=None):  #参数tab用于将切换卡控件的传递
        super().__init__(parent)
        self.tab = tab

        self.urlLabel = QLabel("网址(&D)：")
        self.urlLine = QLineEdit()   #地址栏
        self.urlLabel.setBuddy(self.urlLine)
        self.backBtn = QPushButton(icon=QIcon("d:\\python\\back.png"))  #后退按钮
        self.forwardBtn = QPushButton(icon=QIcon("d:\\python\\forward.png")) #前进按钮
        self.reloadBtn = QPushButton(icon=QIcon("d:\\python\\reload.png")) #重新加载按钮
        self.homeBtn = QPushButton(icon=QIcon("d:\\python\\home.png"))  #主页按钮
        self.webView = QWebEngineView()  #浏览器控件
        self.webPage = self.webView.page()  #浏览器内部的网页
        self.history = self.webPage.history()  #网页上的历史记录
        self.progressBar = QProgressBar()   #进度条控件
        self.progressBar.setRange(0,100)
        self.progressBar.setAlignment(Qt.AlignCenter)
        self.progressBar.setFormat("加载中，已完成%p%")

        self.homeAddress = "https://www.sohu.com"  #主页地址
        self.webPage.setUrl(self.homeAddress)

        H = QHBoxLayout()  # 水平布局
        H.addWidget(self.urlLabel);H.addWidget(self.urlLine);H.addWidget(self.backBtn) 
        H.addWidget(self.forwardBtn);H.addWidget(self.reloadBtn);H.addWidget(self.homeBtn) 

        V = QVBoxLayout(self)  # 竖直布局
        V.addLayout(H);V.addWidget(self.webView);V.addWidget(self.progressBar)#布局添加控件

        self.urlLine.returnPressed.connect(self.urlLine_returnPressed) #信号与槽函数的连接
        self.webPage.urlChanged.connect(self.url_changed)         #信号与槽函数的连接
        self.webPage.titleChanged.connect(self.title_changed)       #信号与槽函数的连接
        self.webPage.iconChanged.connect(self.icon_changed)       #信号与槽函数的连接
        self.webPage.newWindowRequested.connect(self.new_WindowRequested)#信号与槽连接
        self.forwardBtn.clicked.connect(self.forwardBtn_clicked)      #信号与槽函数的连接
        self.backBtn.clicked.connect(self.backBtn_clicked)           #信号与槽函数的连接
        self.reloadBtn.clicked.connect(self.webView.reload)          #信号与槽函数的连接
        self.homeBtn.clicked.connect(self.homeBtn_clicked)          #信号与槽函数的连接
        self.webPage.loadProgress.connect(self.progressBar.setValue)  #信号与槽函数的连接
        self.webPage.loadFinished.connect(self.load_finished)        #信号与槽函数的连接
        self.webPage.loadStarted.connect(self.load_started)          #信号与槽函数的连接
    def urlLine_returnPressed(self):  #输入新地址并回车后的槽函数
        url = QUrl.fromUserInput(self.urlLine.text())
        if url.isValid():
            self.webPage.load(url)  #加载网页
    def url_changed(self, url):  #URL地址发生变化时的槽函数
        self.urlLine.setText(url.toString())   #显示新的地址
        self.backBtn.setEnabled(self.history.canGoBack())
        self.forwardBtn.setEnabled(self.history.canGoForward())
    def title_changed(self,title):  #网页地址发生变化时的槽函数
        tab_index = self.tab.indexOf(self)  #获取当前页的索引
        self.tab.setTabText(tab_index,title)
    def icon_changed(self,icon):  #网页图标发生变化时的槽函数
        tab_index = self.tab.indexOf(self)
        self.tab.setTabIcon(tab_index, icon)
    def new_WindowRequested(self,request):  #需要新网页时的槽函数
        tab_index = self.tab.indexOf(self)
        newWindow = WidgetInTab(parent=None,tab=self.tab)  #创建切换卡内部的控件
        self.tab.insertTab(tab_index+1,newWindow,'加载中...')  #插入新卡片
        self.tab.setCurrentIndex(tab_index+1)  #将新插入的卡片作为当前卡片
        newWindow.webPage.load(request.requestedUrl())  #加载新网页
    def load_started(self):  #网页开始加载时的槽函数
        self.progressBar.show()
    def load_finished(self,ok):  #网页加载结束时的槽函数
        self.progressBar.hide()
    def backBtn_clicked(self):  #后退按钮的槽函数
        self.history.back()
        if not self.history.canGoBack():
            self.backBtn.setEnabled(False)
    def forwardBtn_clicked(self):  #前进按钮的槽函数
        self.history.forward()
        if not self.history.canGoForward():
            self.forwardBtn.setEnabled(False)
    def homeBtn_clicked(self):  #主页按钮的槽函数
        self.webPage.load(self.homeAddress)
class MyWindow(QWidget):  #主窗口
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setWindowTitle('QWebEnginePage的应用实例')
        self.resize(800,600)
        self.setupUi()
    def setupUi(self):
        self.tab = QTabWidget()  #切换卡控件
        self.tab.setTabsClosable(True)
        self.tab.setElideMode(Qt.ElideMiddle)
        H = QHBoxLayout(self)
        H.addWidget(self.tab)
        firstTab = WidgetInTab(parent=None,tab=self.tab)  #第一个卡片中的内容
        self.tab.addTab(firstTab, firstTab.webPage.title())

        self.tab.tabCloseRequested.connect(self.tab_closeRequested)
    def tab_closeRequested(self,index):
        if self.tab.count() > 1:
            self.tab.removeTab(index)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
