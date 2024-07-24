import sys   #Demo6_18.py
from PySide6.QtWidgets import QApplication,QWidget,QVBoxLayout,QGraphicsProxyWidget,\
 QGraphicsScene,QGraphicsView,QPushButton,QGraphicsWidget,QGraphicsLinearLayout,QLabel
from PySide6.QtCore import Qt

class MyWindow(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        view = QGraphicsView()  # 视图控件
        scene = QGraphicsScene()  # 场景
        view.setScene(scene)  # 视图中设置场景
        v = QVBoxLayout(self)  # 布局
        v.addWidget(view)

        widget=QGraphicsWidget()
        widget.setFlags(QGraphicsWidget.ItemIsMovable | QGraphicsWidget.ItemIsSelectable)
        scene.addItem(widget)
        linear = QGraphicsLinearLayout(Qt.Vertical,widget)  #线性竖直布局

        label1=QLabel("MyLabel_1")
        label2=QLabel("MyLabel_2")
        button1=QPushButton("MyPushbutton_1")
        button2=QPushButton("MyPushbutton_2")
        p1=QGraphicsProxyWidget(); p1.setWidget(label1)  #代理控件
        p2 = QGraphicsProxyWidget(); p2.setWidget(label2)  #代理控件
        p3 = QGraphicsProxyWidget(); p3.setWidget(button1)  #代理控件
        p4 = QGraphicsProxyWidget(); p4.setWidget(button2)  #代理控件
        linear.addItem(p1);linear.addItem(p2);linear.addItem(p3);linear.addItem(p4)
        linear.setSpacing(10)
        linear.setStretchFactor(p3,1)
        linear.setStretchFactor(p4,2)
if __name__ == '__main__':
    app=QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
