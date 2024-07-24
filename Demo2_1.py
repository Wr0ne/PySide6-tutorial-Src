from PySide6.QtCore import QPoint,QPointF  #Demo2_1.py
p1 = QPoint(-3,4)
p2 = QPointF(5,8)
print(QPoint.dotProduct(p1,p1),QPointF.dotProduct(p1,p2))
p3 = p2-p1
p4 = p1*3
print(p3.x(), p3.y(), p4.x(), p4.y())
print(p1 == p2, p1 != p2)
#运算结果如下：
#25 17.0
#8.0 4.0 -9 12
#False True
