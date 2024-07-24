import sys  #Demo1_15.py
from PySide6.QtWidgets import QApplication, QWidget
import student  #导入student.py文件

class myWidget(QWidget):  #创建myWindget类，父类是QWidget
    def __init__(self,parent = None):
        super().__init__(parent)  #初始化父类QWidget，这时self是QWidget的窗口对象
        self.ui = student.Ui_Form()  #实例化student.py文件中的Ui_Form类
        self.ui.setupUi(self) #调用Ui_Form类的函数setupUi()，并以self为实参传递给形参Form
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = myWidget()  #用myWidget()类创建窗口myWindow
    myWindow.show()
    sys.exit(app.exec())
