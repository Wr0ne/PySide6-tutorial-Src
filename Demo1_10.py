import sys  #Demo1_10.py
from PySide6.QtWidgets import QApplication, QWidget
from myUi import MyUi  #导入myUi.py文件中的MyUi类

class MyWidget(QWidget):  #创建MyWindget类，父类是QWidget
    def __init__(self,parent = None):
        super().__init__(parent) #初始化父类QWidget，self将是QWidget的窗口对象
        ui = MyUi()  #实例化myUi.py文件中的MyUi类
        ui.setupUi(self)  #调用MyUi的setupUi()，以self为实参传递给形参window
        ui.button.setText("Close")  # 重新设置按钮的显示文字
        ui.button.clicked.connect(self.close)  # 窗口上的按钮事件与窗口事件关联
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWidget()  #用MyWidget类创建窗口对象myWindow
    myWindow.show()
    sys.exit(app.exec())
