import sys   #Demo2_22.py
from PySide6.QtWidgets import QApplication,QWidget,QGroupBox,QFrame,QRadioButton,QHBoxLayout

class MyWidget(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setWindowTitle("QFrame的应用")
        self.resize(300,100)
        self.setupUi()
    def setupUi(self):    # 创建界面上的控件
        self.r_1 = QRadioButton("男")
        self.r_2 = QRadioButton("女")
        self.r_3 = QRadioButton("党员")
        self.r_4 = QRadioButton("团员")
        self.r_5 = QRadioButton("群众")

        self.frame_1 = QFrame()
        self.frame_2 = QFrame()
        self.h_layout_1 = QHBoxLayout(self.frame_1)
        self.h_layout_1.addWidget(self.r_1)
        self.h_layout_1.addWidget(self.r_2)
        self.h_layout_2 = QHBoxLayout(self.frame_2)
        self.h_layout_2.addWidget(self.r_3)
        self.h_layout_2.addWidget(self.r_4)
        self.h_layout_2.addWidget(self.r_5)
        self.groupBox = QGroupBox("选择基本信息",self)
        self.h_layout_3 = QHBoxLayout(self.groupBox)
        self.h_layout_3.addWidget(self.frame_1)
        self.h_layout_3.addWidget(self.frame_2)

        self.r_1.setChecked(True)
        self.r_3.setChecked(True)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
