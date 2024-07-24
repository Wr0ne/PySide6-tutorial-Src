import sys,math   #Demo6_16.py
from PySide6.QtWidgets import (QApplication,QMainWindow,QGraphicsScene,
                             QGraphicsView,QGraphicsItem)
from PySide6.QtCore import Qt,Signal,QPoint,QRectF,QPointF,QLineF
from PySide6.QtGui import QPainterPath,QPolygonF,QLinearGradient

class myGraphicsView(QGraphicsView):  #视图控件的子类
    press_point=Signal(QPoint)  #自定义信号，参数是按下鼠标按键时鼠标在视图中的位置
    move_point=Signal(QPoint)  #自定义信号，参数是移动鼠标时鼠标在视图中的位置
    release_point=Signal(QPoint) #自定义信号，参数是释放鼠标按键时鼠标在视图中的位置
    def __init__(self,parent=None):
        super().__init__(parent)
    def mousePressEvent(self,event):  #按下鼠标按键的事件
        self.press_point.emit(event.pos())  # 发送信号，参数是鼠标位置
        super().mousePressEvent(event)
    def mouseMoveEvent(self,event):  #鼠标移动事件
        self.move_point.emit(event.pos())   #发送信号，参数是鼠标位置
        super().mouseMoveEvent(event)
    def mouseReleaseEvent(self,event):  #释放鼠标按键的事件
        self.release_point.emit(event.pos())
        super().mouseReleaseEvent(event)
    def drawBackground(self, painter,rectF):  #重写背景函数，设置背景颜色
        linear = QLinearGradient(rectF.topLeft(),rectF.bottomLeft())  # 线性渐变
        linear.setStops([(0, Qt.blue), (0.7, Qt.gray)])  # 设置颜色
        painter.fillRect(rectF,linear)  # 用渐变填充矩形
class QGraphicsTriangle(QGraphicsItem):  #自定义三角形图项
    def __init__(self,point1,point2,parent=None):
        super().__init__(parent)
        self.__p1=point1  #三角形第1个点，鼠标按下时的位置
        self.__p2=point2  #三角形第2个点，鼠标移动时的位置
        self.__p3=QPointF(2*self.__p1.x()-self.__p2.x(),self.__p2.y())  #三角形第3个点
    def paint(self,painter,option,widget):  #绘制三角形
        path=QPainterPath()
        path.moveTo(self.__p1)
        path.lineTo(self.__p2)
        path.lineTo(self.__p3)
        path.closeSubpath()
        painter.drawPath(path)
    def boundingRect(self):  #返回图项区域
        x1=min(self.__p2.x(),self.__p3.x())
        y1=min(self.__p1.y(),self.__p2.y())
        x2 = max(self.__p2.x(), self.__p3.x())
        y2 = max(self.__p1.y(), self.__p2.y())
        return QRectF(QPointF(x1,y1),QPointF(x2,y2))
class QGraphicsCurve(QGraphicsItem):  #自定义曲线图项
    def __init__(self,polygonF,parent=None):
        super().__init__(parent)
        self.__polygonF=polygonF
    def paint(self,painter,option,widget):
        painter.drawPolyline(self.__polygonF)  #绘制曲线
    def boundingRect(self):
        p1=self.__polygonF.first()
        p2=self.__polygonF.last()
        x1=min(p1.x(),p2.x())
        y1=min(p1.y(),p2.y())
        x2 = max(p1.x(),p2.x())
        y2 = max(p1.y(),p2.y())
        return QRectF(QPointF(x1,y1),QPointF(x2,y2))
class MyWindow(QMainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.resize(800,600)
        self.setupUI()  #界面
        self.menu_toolbar_Setup()  #菜单和工具栏
        # shape用于记录哪个绘图按钮被选中
        self.shape={'直线':False,'矩形':False,'椭圆':False,'三角形':False,'圆':False,'曲线':False}
        self.__temp=None  #用于指向鼠标移动时产生的临时图项
    def setupUI(self):  #界面建立
        self.graphicsView = myGraphicsView()  # 视图窗口
        self.setCentralWidget(self.graphicsView)
        rectF=QRectF(self.width()/2,self.height()/2,self.width(),self.height())
        self.graphicsScene=QGraphicsScene(rectF)  #创建场景
        self.graphicsView.setViewportUpdateMode(QGraphicsView.FullViewportUpdate)
        self.graphicsView.setScene(self.graphicsScene)  #视图窗口设置场景
        self.graphicsView.press_point.connect(self.press_position)  #信号与槽的连接
        self.graphicsView.move_point.connect(self.move_position)  #信号与槽的连接
        self.graphicsView.release_point.connect(self.release_position)  #信号与槽的连接
    def menu_toolbar_Setup(self):  #菜单和工具栏
        self.menubar = self.menuBar()  #菜单栏
        self.draw=self.menubar.addMenu('绘图')  #绘图菜单
        action_line=self.draw.addAction('直线')  #动作
        action_line.triggered.connect(self.line_triggered)  #动作与槽的连接
        action_rect=self.draw.addAction('矩形')
        action_rect.triggered.connect(self.rect_triggered)
        action_ellipse = self.draw.addAction('椭圆')
        action_ellipse.triggered.connect(self.ellipse_triggered)
        action_triangle = self.draw.addAction('三角形')
        action_triangle.triggered.connect(self.triangle_triggered)
        action_circle = self.draw.addAction('圆')
        action_circle.triggered.connect(self.cirle_triggered)
        action_curve=self.draw.addAction('曲线')
        action_curve.triggered.connect(self.curve_triggered)
        self.draw.addSeparator()
        action_stop=self.draw.addAction('停止')
        action_stop.triggered.connect(self.stop_triggered)
        action_delete=self.draw.addAction("删除")
        action_delete.triggered.connect(self.delete_triggered)
        action_clear=self.draw.addAction("清空")
        action_clear.triggered.connect(self.graphicsScene.clear)
        action_clear.triggered.connect(self.graphicsScene.update)

        self.toolbar_draw=self.addToolBar("绘图")  #工具栏
        self.toolbar_draw.addAction(action_line)
        self.toolbar_draw.addAction(action_rect)
        self.toolbar_draw.addAction(action_ellipse)
        self.toolbar_draw.addAction(action_triangle)
        self.toolbar_draw.addAction(action_circle)
        self.toolbar_draw.addAction(action_curve)
        self.toolbar_draw.addSeparator()
        self.toolbar_draw.addAction(action_stop)
        self.toolbar_draw.addSeparator()
        self.toolbar_draw.addAction(action_delete)
        self.toolbar_draw.addAction(action_clear)
    def press_position(self,point):  #鼠标按下的槽函数
        self.__pressPos=self.graphicsView.mapToScene(point) #映射成场景坐标
        if self.shape['曲线']:
            self.polygon=QPolygonF()
            self.polygon.append(self.__pressPos)
    def move_position(self,point):  #鼠标移动的槽函数
        self.__movePos=self.graphicsView.mapToScene(point)
        if self.shape['曲线']:
            self.polygon.append(self.__movePos)
        self.move_draw(self.__pressPos,self.__movePos)  #调用绘图函数
    def release_position(self,point):  #鼠标释放的槽函数
        if self.__temp:
            self.__temp.setFlags(QGraphicsItem.ItemIsSelectable | QGraphicsItem.ItemIsFocusable)
            self.__temp=None
        rect=self.graphicsScene.itemsBoundingRect()
        if rect.width()>self.width() or rect.height()>self.height():
            self.graphicsScene.setSceneRect(rect)
    def line_triggered(self):  #绘制直线动作的槽函数
        self.shape={'直线':True,'矩形':False,'椭圆':False,'三角形':False,'圆':False,'曲线':False}
    def rect_triggered(self):  #绘制矩形动作的槽函数
        self.shape={'直线':False,'矩形':True,'椭圆':False,'三角形':False,'圆':False,'曲线':False}
    def ellipse_triggered(self):  #绘制椭圆动作的槽函数
        self.shape={'直线':False,'矩形':False,'椭圆':True,'三角形':False,'圆':False,'曲线':False}
    def triangle_triggered(self):  #绘制三角形动作的槽函数
        self.shape={'直线':False,'矩形':False,'椭圆':False,'三角形':True,'圆':False,'曲线':False}
    def cirle_triggered(self):  #绘制圆动作的槽函数
        self.shape={'直线':False,'矩形':False,'椭圆':False,'三角形':False,'圆':True,'曲线':False}
    def curve_triggered(self):  #绘制曲线动作的槽函数
        self.shape={'直线':False,'矩形':False,'椭圆':False,'三角形':False,'圆':False,'曲线':True}
    def stop_triggered(self):  #停止绘制动作的槽函数
        self.shape={'直线':False,'矩形':False,'椭圆':False,'三角形':False,'圆':False,'曲线':False}
    def delete_triggered(self):  #清空图项动作的槽函数
        if len(self.graphicsScene.selectedItems()):
            for i in self.graphicsScene.selectedItems():
                self.graphicsScene.removeItem(i)
    def move_draw(self,p1,p2):  #鼠标移动时绘制图形
        x1 = min(p1.x(), p2.x())
        y1 = min(p1.y(), p2.y())
        x2 = max(p1.x(), p2.x())
        y2 = max(p1.y(), p2.y())
        rectF = QRectF(QPointF(x1, y1), QPointF(x2, y2)) #鼠标按下点与移动点的矩形区域
        if self.__temp:  #在鼠标移动过程中，如果变量已经指向图项，需要把图项移除
            self.graphicsScene.removeItem(self.__temp)
        if self.shape['直线']:
            self.__temp=self.graphicsScene.addLine(QLineF(p1,p2)) #添加直线
        if self.shape['矩形']:
            self.__temp=self.graphicsScene.addRect(rectF) #添加矩形
        if self.shape['椭圆']:
            self.__temp=self.graphicsScene.addEllipse(rectF)  #添加椭圆
        if self.shape['三角形']:
            self.__temp=QGraphicsTriangle(p1,p2)  #实例化自定义三角形图项
            self.graphicsScene.addItem(self.__temp)  #添加图项
        if self.shape['圆']:
            r = math.sqrt((p1.x()-p2.x())**2+(p1.y()-p2.y())**2)
            pointF_1 = QPointF(p1.x()-r,p1.y()-r)
            pointF_2 = QPointF(p1.x()+r,p1.y()+r)
            self.__temp=self.graphicsScene.addEllipse(QRectF(pointF_1,pointF_2)) #添加圆
        if self.shape['曲线']:
            self.__temp = QGraphicsCurve(self.polygon)  #实例化自定义曲线图项
            self.graphicsScene.addItem(self.__temp)  #添加图项
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
