import sys  #Demo1_9.py
from PySide6.QtWidgets import QApplication, QWidget

from myUi import MyUi  #导入myUi.py文件中的MyUi类

def myWidget(parent = None):
    widget = QWidget(parent) #创建QWidget类的对象，调用QWidget类的__init__()函数
    ui = MyUi()  #实例化myUi.py文件中的MyUi类
    ui.setupUi(widget)  #调用MyUi类的setupUi()，以widget为实参传递给形参window
    ui.button.setText("Close")  #重新设置按钮上显示的文字
    ui.button.clicked.connect(widget.close)  #窗口上的按钮事件与窗口事件关联

    return widget   #函数的返回值是窗口实例对象
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = myWidget()  #调用myWidget()函数，返回值是窗口实例对象
    myWindow.show()
    sys.exit(app.exec())
