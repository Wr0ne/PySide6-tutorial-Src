import sys  #Demo2_10.py
from PySide6.QtWidgets import QApplication,QWidget,QPushButton,QLabel,QLineEdit
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
                   [202005, '墙头草', 93, 86, 73, 86] ] #学生信息和成绩，可从文件读取
    def setupUi(self):    # 创建界面上的控件
        self.label_1 = QLabel(self)
        self.label_1.setGeometry(QRect(120, 40, 231, 31))
        font = QFont("楷体",pointSize=20)
        self.label_1.setFont(font)
        self.label_1.setText("学生考试成绩查询")

        self.label_2 = QLabel(self)
        self.label_2.setGeometry(QRect(113, 130, 60, 20))
        self.label_2.setText("姓名(&N)：")

        self.label_3 = QLabel(self)
        self.label_3.setGeometry(QRect(100, 160, 70, 20))
        self.label_3.setText("准考证号(&T)：")

        self.label_4 = QLabel(self)
        self.label_4.setGeometry(QRect(100, 260, 100, 20))
        self.label_4.setText("查询结果如下：")

        self.lineEdit_name = QLineEdit(self)
        self.lineEdit_name.setGeometry(QRect(190, 130, 113, 20))
        self.lineEdit_name.setClearButtonEnabled(True)  #设置清空按钮
        self.lineEdit_number = QLineEdit(self)
        self.lineEdit_number.setGeometry(QRect(190, 160, 113, 20))
        self.lineEdit_number.setValidator(QIntValidator(202001,202100)) #设置验证
        self.lineEdit_number.setEchoMode(QLineEdit.Password)  #设置密码形式
        self.lineEdit_number.setClearButtonEnabled(True)  #设置清空按钮
        self.lineEdit_results = QLineEdit(self)
        self.lineEdit_results.setGeometry(QRect(70, 300, 321, 20))
        self.lineEdit_results.setReadOnly(True)  #设置只读属性
        self.label_2.setBuddy(self.lineEdit_name)  #伙伴关系
        self.label_3.setBuddy(self.lineEdit_number)  #伙伴关系

        self.btn_enquire = QPushButton(self)
        self.btn_enquire.setGeometry(QRect(150, 210, 75, 23))
        self.btn_enquire.setText("查询(&E)")
        self.btn_enquire.clicked.connect(self.inquire)  #信号与槽的连接

        self.btnClear = QPushButton(self)
        self.btnClear.setGeometry(QRect(240, 210, 81, 23))
        self.btnClear.setText("清空(&C)")
        self.btnClear.clicked.connect(self.lineEdit_name.clear)  #信号与槽的连接
        self.btnClear.clicked.connect(self.lineEdit_number.clear)  #信号与槽的连接
        self.btnClear.clicked.connect(self.lineEdit_results.clear)  #信号与槽的连接

        self.lineEdit_name.textChanged.connect(self.text_changed)  #信号与槽的连接
        self.lineEdit_number.textChanged.connect(self.text_changed)  #信号与槽的连接
        self.text_changed()
    def inquire(self):
        number = int(self.lineEdit_number.text())
        template = "{}的考试成绩：语文 {} 数学 {} 英语 {} 物理 {}"
        for i in range(len(self.__data)):
            stu = self.__data[i]
            if stu[0] == number and stu[1] == self.lineEdit_name.text():
                self.lineEdit_results.setText(template.format(stu[1], stu[2], stu[3], stu[4], stu[5]))
                break
            else:
                if i == len(self.__data) - 1:
                    self.lineEdit_results.setText("查无此人")
    def text_changed(self):
        if self.lineEdit_number.text() !="" and self.lineEdit_name.text() != "":
            self.btn_enquire.setEnabled(True)
        else:
            self.btn_enquire.setEnabled(False)
        if self.lineEdit_number.text() !="" or self.lineEdit_name.text() != "":
            self.btnClear.setEnabled(True)
        else:
            self.btnClear.setEnabled(False)
if __name__ == '__main__':
    app=QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
