import sys   #Demo1_4.py
from PySide6.QtWidgets import QApplication,QWidget,QLabel,QPushButton

app = QApplication(sys.argv)  #创建应用实例

myWindow = QWidget()  #创建窗口实例
myWindow.setWindowTitle('Hello')  #设置窗口标题
myWindow.resize(300,150)  #设置窗口长宽

myLabel = QLabel(myWindow)  #在窗口上创建标签实例
string = '欢迎使用本书学习编程！'
myLabel.setText(string)   #设置标签文字
myLabel.setGeometry(80,50,150,20)  #设置标签的位置和长宽

myButton = QPushButton(myWindow)  #在窗口上创建按钮实例
myButton.setText("关 闭")  #设置按钮文本
myButton.setGeometry(120,100,50,20)  #设置按钮的位置和长宽
myButton.clicked.connect(myWindow.close) #将按钮的单击事件和窗口的关闭事件关联

myWindow.show()   #显示窗口
n = app.exec() #执行exec()方法，进入事件循环，如果遇到窗口退出命令，返回整数n
print("n=",n)   #输出窗口关闭时返回的整数
try:   #捕获程序退出事件
    sys.exit(n)  #通知Python系统，结束程序运行
except SystemExit:
    print("请在此做一些其他工作。")  #Python解释器停止执行前的工作
#单击关闭按钮后，得到如下结果
#n= 0
#请在此做一些其他工作。
