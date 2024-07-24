import sys  #Demo1_5.py
from PySide6.QtWidgets import QApplication,QWidget,QLabel,QPushButton

def setupUi(window):   #形参window是一个窗口实例对象
    window.setWindowTitle('Hello')  #设置窗口标题
    window.resize(300, 150)  #设置窗口尺寸

    label = QLabel(window)   #在窗口上创建标签
    label.setText('欢迎使用本书学习编程！')
    label.setGeometry(80, 50, 150, 20)  #设置标签在窗口中的位置和标签的宽度和高度

    button = QPushButton(window)  #在窗口上创建按钮
    button.setText("关 闭")
    button.setGeometry(120, 100, 50, 20) #设置按钮在窗口中的位置和按钮的宽度和高度
    button.clicked.connect(window.close)  #按钮事件与窗口事件的关联
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = QWidget()
    setupUi(myWindow)   #调用setupUi()函数，并把窗口作为实参传递给setupUi()函数
    myWindow.show()
    sys.exit(app.exec())
