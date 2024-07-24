import sys  #Demo1_11.py
from PySide6.QtWidgets import QApplication, QWidget
from myUi import MyUi  #从myUi.py文件中导入MyUi类

class MyWidget(QWidget,MyUi):  #创建MyWindget类，父类是QWidget和MyUi
    def __init__(self,parent = None):
        super().__init__(parent)  #初始化父类QWidget，self是QWidget的窗口对象
        self.setupUi(self)  #调用MyUi的setupUi()，以self为实参传递给形参window
        self.button.setText("Close")  # 重新设置按钮的显示文字
        self.button.clicked.connect(self.close)  # 窗口上的按钮事件与窗口事件关联
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWidget()  #用MyWidget类创建窗口对象myWindow
    myWindow.show()
    sys.exit(app.exec())
