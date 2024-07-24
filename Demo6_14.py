import sys   #Demo6_14.py
from PySide6.QtWidgets import (QApplication,QWidget,QGraphicsScene,QGraphicsView,
      QVBoxLayout,QStatusBar,QGraphicsRectItem,QGraphicsItem,QGraphicsEllipseItem)
from PySide6.QtCore import Qt,Signal,QPoint,QRectF

class myGraphicsView(QGraphicsView):  #视图控件的子类
    point_position=Signal(QPoint)  #自定义信号，参数是鼠标在视图中的位置
    def __init__(self,parent=None):
        super().__init__(parent)
    def mousePressEvent(self,event):  #鼠标单击事件
        self.point_position.emit(event.pos())  # 发送信号，参数是鼠标位置
        super().mousePressEvent(event)
    def mouseMoveEvent(self,event):  #鼠标移动事件
        self.point_position.emit(event.pos())   #发送信号，参数是鼠标位置
        super().mouseMoveEvent(event)
    def drawBackground(self, painter,rectF):  #重写背景函数，设置背景颜色
        painter.fillRect(rectF,Qt.gray)
class MyWindow(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.resize(800,600)        
        self.setupUI()
    def setupUI(self):
        self.graphicsView = myGraphicsView()  # 视图窗口
        self.statusbar = QStatusBar()  # 状态栏
        v=QVBoxLayout(self)
        v.addWidget(self.graphicsView)
        v.addWidget(self.statusbar)
        rectF=QRectF(-200,-150,400,300)
        self.graphicsScene=QGraphicsScene(rectF)  #创建场景
        self.graphicsView.setScene(self.graphicsScene)  #视图窗口设置场景
        rect_item=QGraphicsRectItem(rectF)  #以场景为坐标创建矩形
        rect_item.setFlags(QGraphicsItem.ItemIsSelectable| QGraphicsItem.ItemIsMovable)  #标识
        self.graphicsScene.addItem(rect_item)  #在场景中添加图项
        rectF=QRectF(-40,-40,80,80)
        ellipse_item = QGraphicsEllipseItem(rectF)  #以场景为坐标创建椭圆
        ellipse_item.setBrush(Qt.green)  #设置画刷
        ellipse_item.setFlags(QGraphicsItem.ItemIsSelectable | QGraphicsItem.ItemIsMovable)
        self.graphicsScene.addItem(ellipse_item)  #在场景中添加图项
        self.graphicsView.point_position.connect(self.mousePosition)  #信号与槽的连接
    def mousePosition(self,point):  #槽函数
        template="view坐标:{},{}  scene坐标:{},{}  item坐标:{},{}"
        point_scene=self.graphicsView.mapToScene(point)  #视图中的点映射到场景中
        item = self.graphicsView.itemAt(point)  #获取视图控件中的图项
        #item = self.graphicsScene.itemAt(point_scene,self.graphicsView.transform())#场景中图项
        if item:
            point_item=item.mapFromScene(point_scene)  #把场景坐标转换为图项坐标
            string=template.format(point.x(),point.y(),point_scene.x(),point_scene.y(),
                                  point_item.x(),point_item.y())
        else:
            string = template.format(point.x(), point.y(), point_scene.x(),
                                  point_scene.y(),"None","None")
        self.statusbar.showMessage(string)  #在状态栏中显示坐标信息
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
