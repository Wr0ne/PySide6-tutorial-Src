import sys  #Demo3_1.py
from PySide6.QtWidgets import QApplication, \
    QPushButton,QLabel

app = QApplication(sys.argv)
myWindow = QPushButton()
myWindow.setWindowTitle("QPushButton")
myWindow.resize(250,100)
label = QLabel("我是QLablel")
label.setParent(myWindow) #setParent()方法
label.setGeometry(80,20,100,30)
btn = QPushButton("我是QPushButton",
myWindow)
btn.setGeometry(60,50,100,30)
myWindow.show()
n = app.exec()
sys.exit(n)
