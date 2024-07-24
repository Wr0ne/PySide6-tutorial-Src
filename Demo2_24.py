import sys  #Demo2_24.py
from PySide6.QtWidgets import (QApplication,QWidget,QPushButton,QLabel,QLineEdit,
              QTabWidget,QTextBrowser,QVBoxLayout)
from PySide6.QtGui import QFont,QIntValidator
from PySide6.QtCore import QRect

class MyWidget(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setWindowTitle("学生成绩查询系统")
        self.setGeometry(400,200,480,370)
        self.setupUi()

        self.__data = [ [202003, '没头脑', 89, 88, 93, 87],
                        [202002, '不高兴', 80, 71, 88, 98],
                        [202004, '倒霉蛋', 95, 92, 88, 94],
                        [202001, '鸭梨头', 93, 84, 84, 77],
                        [202005, '墙头草', 93, 86, 73, 86]]  #学生信息和成绩
    def setupUi(self):    # 创建界面上的控件
        self.widget_1 = QWidget()  #建立第1个窗口
        self.widget_2 = QWidget()  #建立第2个窗口
        self.tabWidget = QTabWidget(self)  #建立切换卡
        self.tabWidget.addTab(self.widget_1,"信息输入(&I)")  #添加第1个卡片
        self.tabWidget.addTab(self.widget_2,"查询结果(&E)")  #添加第2个卡片

        v = QVBoxLayout(self)  #竖直布局
        v.addWidget(self.tabWidget)

        self.label_1 = QLabel(self.widget_1)   #在第1个卡片的窗口中添加控件
        self.label_1.setGeometry(QRect(120, 40, 230, 30))
        font = QFont("楷体",pointSize=20)
        self.label_1.setFont(font)
        self.label_1.setText("学生考试成绩查询")

        self.label_2 = QLabel(self.widget_1)  #在第1个卡片的窗口中添加控件
        self.label_2.setGeometry(QRect(113, 130, 60, 20))
        self.label_2.setText("姓名(&N)：")

        self.label_3 = QLabel(self.widget_1)  #在第1个卡片的窗口中添加控件
        self.label_3.setGeometry(QRect(100, 160, 70, 20))
        self.label_3.setText("准考证号(&T)：")


        self.lineEdit_name = QLineEdit(self.widget_1)  #在第1个卡片窗口中添加控件
        self.lineEdit_name.setGeometry(QRect(190, 130, 113, 20))
        self.lineEdit_name.setClearButtonEnabled(True)  #设置清空按钮
        self.lineEdit_number = QLineEdit(self.widget_1) #在第1个卡片窗口中添加控件
        self.lineEdit_number.setGeometry(QRect(190, 160, 113, 20))
        self.lineEdit_number.setValidator(QIntValidator(202001,202100))  #设置验证
        self.lineEdit_number.setEchoMode(QLineEdit.Password)  #设置密码形式
        self.lineEdit_number.setClearButtonEnabled(True)  #设置清空按钮

        self.label_2.setBuddy(self.lineEdit_name)  #伙伴关系
        self.label_3.setBuddy(self.lineEdit_number)  #伙伴关系

        self.btn_enquire = QPushButton(self.widget_1)  #在第1个卡片窗口中添加控件
        self.btn_enquire.setGeometry(QRect(150, 210, 75, 23))
        self.btn_enquire.setText("查询(&E)")
        self.btn_enquire.clicked.connect(self.inquire)  #信号与槽的连接

        self.btnClear = QPushButton(self.widget_1)  #在第1个卡片窗口中添加控件
        self.btnClear.setGeometry(QRect(240, 210, 81, 23))
        self.btnClear.setText("清空(&C)")
        self.btnClear.clicked.connect(self.lineEdit_name.clear)   #信号与槽的连接
        self.btnClear.clicked.connect(self.lineEdit_number.clear)  #信号与槽的连接

        self.texBrowser = QTextBrowser(self.widget_2)  #在第2个卡片窗口中添加控件
        self.texBrowser.setFont(font)

        v_layout = QVBoxLayout(self.widget_2)  #第2个窗口的布局
        v_layout.addWidget(self.texBrowser)
    def inquire(self):
        if self.lineEdit_name.text() != "" and self.lineEdit_number.text() != "":
            number = int(self.lineEdit_number.text())
            template = "{}的考试成绩：语文 {} 数学 {} 英语 {} 物理 {}"
            for i in range(len(self.__data)):
                stu = self.__data[i]
                if stu[0] == number and stu[1] == self.lineEdit_name.text():
                    self.texBrowser.append(template.format(stu[1],stu[2],stu[3],stu[4],stu[5]))
                    break
                else:
                    if i == len(self.__data)-1:
                        self.texBrowser.append("查无此人")
            self.tabWidget.setCurrentWidget(self.widget_2)
if __name__ == '__main__':
    app=QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
