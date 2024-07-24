import sys  #Demo2_26.py
from PySide6.QtWidgets import QApplication,QWidget,QLabel,QPushButton,\
                              QLineEdit,QHBoxLayout,QVBoxLayout
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import QUrl
from PySide6.QtGui import QIcon

class myWebView(QWebEngineView):   #创建QWebEngineView的子类
    def __init__(self,parent=None):
        super().__init__(parent)
    def createWindow(self,type):      #重写createWindow()函数
        return self
class MyWindow(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setWindowTitle('QWebEngineView的应用实例')
        self.resize(800,600)
        self.setupUi()
    def setupUi(self):
        self.urlLabel = QLabel("网址(&D)：")
        self.urlLine = QLineEdit()
        self.urlLabel.setBuddy(self.urlLine)
        self.backBtn = QPushButton(icon=QIcon("d:\\python\\back.png"))
        self.forwardBtn = QPushButton(icon=QIcon("d:\\python\\forward.png"))
        self.reloadBtn = QPushButton(icon=QIcon("d:\\python\\reload.png"))
        self.homeBtn = QPushButton(icon=QIcon("d:\\python\\home.png"))
        self.webEngineView = myWebView()  #用QWebEngineView的子类创建浏览器
        self.webEngineView.setUrl("https://www.sohu.com")
        self.urlLine.setText("https://www.sohu.com")
        H = QHBoxLayout()              #水平布局
        H.addWidget(self.urlLabel)        #水平布局中添加控件
        H.addWidget(self.urlLine)
        H.addWidget(self.backBtn)
        H.addWidget(self.forwardBtn)
        H.addWidget(self.reloadBtn)
        H.addWidget(self.homeBtn)
        V = QVBoxLayout(self)              #竖直布局
        V.addLayout(H)                   #竖直布局中布局
        V.addWidget(self.webEngineView)    #竖直布局中添加控件

        self.urlLine.returnPressed.connect(self.urlLine_returnPressed)   #信号与槽函数的连接
        self.webEngineView.titleChanged.connect(self.setWindowTitle)  #信号与槽函数的连接
        self.webEngineView.urlChanged.connect(self.urlChanged)       #信号与槽函数的连接
        self.webEngineView.iconChanged.connect(self.setWindowIcon)  #信号与槽函数的连接
        self.forwardBtn.clicked.connect(self.webEngineView.forward)    #信号与槽函数的连接
        self.backBtn.clicked.connect(self.webEngineView.back)         #信号与槽函数的连接
        self.reloadBtn.clicked.connect(self.webEngineView.reload)      #信号与槽函数的连接
        self.homeBtn.clicked.connect(self.homeBtn_clicked)           #信号与槽函数的连接
    def urlLine_returnPressed(self):
        url = QUrl.fromUserInput(self.urlLine.text())
        if url.isValid():
            self.webEngineView.load(url)  #加载网页
    def urlChanged(self, url):
        self.urlLine.setText(url.toString())   #显示新的地址
    def homeBtn_clicked(self):
        self.webEngineView.load("https://www.sohu.com")
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
