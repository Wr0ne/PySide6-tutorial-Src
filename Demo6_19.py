import sys,os   #Demo6_19.py
from PySide6.QtWidgets import QApplication,QWidget,QVBoxLayout,QHBoxLayout,\
QGraphicsScene,QGraphicsView,QPushButton,QGraphicsBlurEffect,QGraphicsColorizeEffect,\
QGraphicsDropShadowEffect,QGraphicsOpacityEffect,QFileDialog,QGraphicsPixmapItem
from PySide6.QtGui import QPixmap,QLinearGradient
from PySide6.QtCore import Qt

class MyWindow(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setupUi()
        self.pixmapItem=None
    def setupUi(self):
        self.view = QGraphicsView()  # 视图控件
        self.scene = QGraphicsScene()  # 场景
        self.view.setScene(self.scene)  # 视图中设置场景
        self.btn_open=QPushButton("打开图片...")
        self.btn_blur = QPushButton("模糊效果")
        self.btn_color = QPushButton("变色效果")
        self.btn_shadow = QPushButton("阴影效果")
        self.btn_opacity= QPushButton("透明效果")
        h=QHBoxLayout()
        h.addWidget(self.btn_open)
        h.addWidget(self.btn_blur)
        h.addWidget(self.btn_color)
        h.addWidget(self.btn_shadow)
        h.addWidget(self.btn_opacity)
        v=QVBoxLayout(self)
        v.addWidget(self.view)
        v.addLayout(h)
        self.btn_open.clicked.connect(self.btn_open_clicked)
        self.btn_blur.clicked.connect(self.btn_blur_clicked)
        self.btn_color.clicked.connect(self.btn_color_clicked)
        self.btn_shadow.clicked.connect(self.btn_shadow_clicked)
        self.btn_opacity.clicked.connect(self.btn_opacity_clicked)
        self.btn_blur.setEnabled(False)
        self.btn_color.setEnabled(False)
        self.btn_shadow.setEnabled(False)
        self.btn_opacity.setEnabled(False)
    def btn_open_clicked(self):
        (fileName,filter)=QFileDialog.getOpenFileName(self,caption="打开图片",
                    dir="d:\\",filter="图片(*.png *.bmp *.jpg *.jpeg)")
        if os.path.exists(fileName):
            if self.pixmapItem != None:
                self.scene.removeItem(self.pixmapItem)
            pix=QPixmap(fileName)
            self.pixmapItem=QGraphicsPixmapItem(pix)
            self.scene.addItem(self.pixmapItem)
            self.btn_blur.setEnabled(True)
            self.btn_color.setEnabled(True)
            self.btn_shadow.setEnabled(True)
            self.btn_opacity.setEnabled(True)
        else:
            if self.pixmapItem == None:
                self.btn_blur.setEnabled(False)
                self.btn_color.setEnabled(False)
                self.btn_shadow.setEnabled(False)
                self.btn_opacity.setEnabled(False)
    def btn_blur_clicked(self):
        self.effect=QGraphicsBlurEffect()
        self.effect.setBlurRadius(10)
        self.effect.setBlurHints(QGraphicsBlurEffect.QualityHint)
        self.pixmapItem.setGraphicsEffect(self.effect)
    def btn_color_clicked(self):
        self.effect=QGraphicsColorizeEffect()
        self.effect.setColor(Qt.blue)
        self.effect.setStrength(10)
        self.pixmapItem.setGraphicsEffect(self.effect)
    def btn_shadow_clicked(self):
        self.effect=QGraphicsDropShadowEffect()
        self.pixmapItem.setGraphicsEffect(self.effect)
    def btn_opacity_clicked(self):
        rect=self.pixmapItem.boundingRect()
        linear=QLinearGradient(rect.topLeft(),rect.bottomLeft())
        linear.setColorAt(0.1,Qt.transparent)
        linear.setColorAt(0.5,Qt.black)
        linear.setColorAt(0.9,Qt.white)
        self.effect=QGraphicsOpacityEffect()
        self.effect.setOpacityMask(linear)
        self.pixmapItem.setGraphicsEffect(self.effect)
if __name__ == '__main__':
    app=QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
