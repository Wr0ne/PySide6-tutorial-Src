from PySide6.QtCore import QSize,QSizeF,QMargins,Qt   #Demo2_2.py

s1 = QSize(5,6); s2 = QSizeF(8,10)
s3 = s2-s1; print("s3:",s3.width(), s3.height())
s4 = s1*3; print("s4:",s4.width(), s4.height())
margin = QMargins(1,2,3,4)
s5 = s2.shrunkBy(margin); print("s5:",s5.width(), s5.height())

s1 = QSize(5, 6)
ss = s1.scaled(10,20,Qt.IgnoreAspectRatio); print("IgnoreAspectRatio:",ss.width(), ss.height())
ss = s1.scaled(10,20,Qt.KeepAspectRatio); print("KeepAspectRatio:",ss.width(), ss.height())
ss = s1.scaled(10,20,Qt.KeepAspectRatioByExpanding)
print("KeepAspectRatioByExpanding:",ss.width(), ss.height())
#运行结果如下：
#s3: 3.0 4.0
#s4: 15 18
#s5: 4.0 4.0
#IgnoreAspectRatio: 10 20
#KeepAspectRatio: 10 12
#KeepAspectRatioByExpanding: 16 20
