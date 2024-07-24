from PySide6.QtWidgets import QLabel, QPushButton    #myUi.py文件

class MyUi(object):  #定义MyUi类
    def setupUi(self,window):  #定义方法，形参window是一个窗口实例
        window.setWindowTitle('Hello')
        window.resize(300, 150)

        self.label = QLabel(window)  #在窗口上创建标签
        self.label.setText('欢迎使用本书学习编程！')
        self.label.setGeometry(80, 50, 150, 20)

        self.button = QPushButton(window)  #在窗口上创建按钮
        self.button.setText("关 闭")
        self.button.setGeometry(120, 100, 50, 20)
