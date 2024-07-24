import sys  #Demo1_8.py
from PySide6.QtWidgets import QApplication, QWidget
from myUi import MyUi  #导入myUi.py文件中的MyUi类

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = QWidget()

    ui = MyUi()  #用MyUi类创建实例ui
    ui.setupUi(myWindow)  #调用ui的方法setupUi()，并以窗口实例作为实参
    ui.button.setText("Close")  #重新设置按钮上显示的文字
    ui.button.clicked.connect(myWindow.close)  #窗口上的按钮事件与窗口事件关联

    myWindow.show()
    sys.exit(app.exec())
