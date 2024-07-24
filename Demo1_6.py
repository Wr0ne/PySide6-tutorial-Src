import sys  #Demo1_6.py
from PySide6.QtWidgets import QApplication,QWidget,QLabel,QPushButton

class MyUi():  #定义MyUi类
    def setupUi(self,window):  # 定义方法，形参window是一个窗口实例对象
        window.setWindowTitle('Hello')
        window.resize(300, 150)

        self.label = QLabel(window)  # 在窗口上创建标签
        self.label.setText('欢迎使用本书学习编程！')
        self.label.setGeometry(80, 50, 150, 20)

        self.button = QPushButton(window)  # 在窗口上创建按钮
        self.button.setText("关 闭")
        self.button.setGeometry(120, 100, 50, 20)
        #self.button.clicked.connect(window.close)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = QWidget()

    ui = MyUi()  #用MyUi类创建实例ui
    ui.setupUi(myWindow)  #调用ui的方法setupUi()，并以窗口实例对象作为实参
    ui.button.setText("Close")  #重新设置按钮上显示的文字
    ui.button.clicked.connect(myWindow.close)  #窗口上的按钮事件与窗口事件关联

    myWindow.show()
    sys.exit(app.exec())
