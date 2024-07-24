import sys   #Demo1_3.py
from PySide6.QtWidgets import QApplication,QWidget

app = QApplication(sys.argv)  #创建应用程序实例对象
myWindow = QWidget()  #创建窗口实例
myWindow.show()   #显示窗口
n = app.exec()  #执行exec()方法，进入事件循环，如果遇到窗口退出命令，返回整数n
sys.exit(n)  #通知Python系统，结束程序运行
