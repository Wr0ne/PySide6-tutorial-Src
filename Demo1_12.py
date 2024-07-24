import sys  #Demo1_12.py
from PySide6.QtWidgets import QApplication,QWidget,QLabel,QPushButton

class MyWidget(QWidget):  #创建MyWindget类，父类是QWidget
    def __init__(self,parent = None):
        super().__init__(parent)  #初始化父类QWidget，self是QWidget的窗口对象
        self.setupUi()  #调用setupUi()方法，在窗口上添加控件
        self.button.setText("Close")  # 重新设置按钮的显示文字
        self.button.clicked.connect(self.close)  #窗口上的按钮信号与窗口事件关联

    def setupUi(self):  #定义方法
        self.setWindowTitle('Hello')
        self.resize(300, 150)

        self.label = QLabel(self)  #在窗口上创建标签
        self.label.setText('欢迎使用本书学习编程！')
        self.label.setGeometry(80, 50, 150, 20)

        self.button = QPushButton(self)  #在窗口上创建按钮
        self.button.setText("关 闭")
        self.button.setGeometry(120, 100, 50, 20)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWidget()  #用MyWidget类创建窗口对象myWindow
    myWindow.show()
    sys.exit(app.exec())
