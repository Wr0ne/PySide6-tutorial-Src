import sys  #Demo2_5.py
from PySide6.QtWidgets import QApplication,QWidget,QLabel,QVBoxLayout,\
                              QPushButton,QFileDialog
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

class MyPixmap(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setGeometry(200,200,800,500)  #设置窗口尺寸
        self.setupUi()  #调用函数建立界面
    def setupUi(self):   #创建界面
        self.label = QLabel("单击按钮打开图像文件！")  #创建标签
        self.label.setAlignment(Qt.AlignCenter)   #中心对齐
        font = self.label.font()   #获取字体
        font.setPointSize(10)  #设置字体大小
        self.label.setFont(font)  #给标签设置字体
        self.open_button = QPushButton("打开图像文件(&O)")  #创建按钮
        self.open_button.setFont(font)  #给按钮设置字体

        self.vertical_layout = QVBoxLayout(self)  #在窗口上创建竖直布局
        self.vertical_layout.addWidget(self.label)  #在布局中添加标签
        self.vertical_layout.addWidget(self.open_button)  #在布局中添加按钮

        self.open_button.clicked.connect(self.open_button_clciked)  #按钮信号与槽的连接
    def open_button_clciked(self):
        fileName,filter = QFileDialog.getOpenFileName(filter=  #打开对话框获取文件名
           '图像文件(*.png *.bmp *.jpg *.jpeg);;所有文件(*.*)')
        pixmap = QPixmap(fileName)  #创建QPixmap图像
        self.label.setPixmap(pixmap)  #在标签中显示图像
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyPixmap()
    window.show()
    sys.exit(app.exec())
