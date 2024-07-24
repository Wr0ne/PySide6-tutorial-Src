import sys,os   #Demo6_17.py
from PySide6.QtWidgets import QApplication,QWidget,QVBoxLayout,QGraphicsProxyWidget,\
                QGraphicsScene,QGraphicsView,QFrame,QPushButton,QFileDialog
from PySide6.QtGui import QPainter,QTransform,QPixmap
from PySide6.QtCore import Qt,QRect

class myFrame(QFrame):  #创建QFrame的子类
    def __init__(self,parent=None):
        super().__init__(parent)
        #self.setFrameShape(QFrame.Box)
        self.fileName=""
    def paintEvent(self,event):  #重写painterEvent，完成绘图
        if os.path.exists(self.fileName):
            pix=QPixmap(self.fileName)
            painter=QPainter(self)
            rect=QRect(0,0,self.width(),self.height())
            painter.drawPixmap(rect,pix)
        super().paintEvent(event)
class myPixmapWidget(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.resize(600,400)
        self.frame=myFrame()  #自定义QFrame的实例
        self.button=QPushButton("选择图片文件")  #按钮实例
        self.button.clicked.connect(self.button_clicked)  #按钮信号与槽函数的连接
        v = QVBoxLayout(self)  #布局
        v.addWidget(self.frame)
        v.addWidget(self.button)
    def button_clicked(self):  #按钮的槽函数
        (fileName, filter) = QFileDialog.getOpenFileName(self, caption="打开图片",
                dir="d:\\",filter="图片(*.png *.bmp *.jpg *.jpeg)")
        self.frame.fileName=fileName
        self.frame.update()
class MyWindow(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        pix=myPixmapWidget()  #绘图窗口
        view=QGraphicsView()  #视图控件
        scene=QGraphicsScene()  #场景
        view.setScene(scene)  #在视图中设置场景
        proxy=QGraphicsProxyWidget(None,Qt.Window)  #创建代理控件
        proxy.setWidget(pix)  #代理控件设置控件
        proxy.setTransform(QTransform().shear(1,-0.5)) #错切变换
        scene.addItem(proxy)  #在场景中添加图项
        v = QVBoxLayout(self)  #布局
        v.addWidget(view)
if __name__ == '__main__':
    app=QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
