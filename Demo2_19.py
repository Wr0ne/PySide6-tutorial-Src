import sys  #Demo2_19.py
from PySide6.QtWidgets import (QApplication,QWidget,QLineEdit,QSpinBox,QLabel,
QTextBrowser,QFormLayout, QRadioButton,QHBoxLayout,QPushButton)
from PySide6.QtCore import Qt
class myWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QFormLayout")
        self.resize(300,200)
        self.setupUi()
    def setupUi(self):
        formLayout = QFormLayout(self)
        name= QLabel("姓名(&N)：")
        self.name_lineEdit = QLineEdit()
        name.setBuddy(self.name_lineEdit)  #定义伙伴关系
        formLayout.addRow(name,self.name_lineEdit)  #添加行
        number = QLabel("学号(&B)：")
        self.number_lineEdit = QLineEdit()
        number.setBuddy(self.number_lineEdit)
        formLayout.addRow(number, self.number_lineEdit)  #添加行
        self.age_spinBox = QSpinBox()
        formLayout.addRow("年龄(&A)：", self.age_spinBox)  #添加行
        self.male_radioButton = QRadioButton("男(&M)")
        self.male_radioButton.setChecked(True)
        self.female_radioButton = QRadioButton("女(&F)")
        h_layout = QHBoxLayout()
        h_layout.addWidget(self.male_radioButton)
        h_layout.addWidget(self.female_radioButton)
        formLayout.addRow("性别：",h_layout)  #添加行
        self.append_btn = QPushButton("添  加 (&A)") 
        formLayout.addRow(self.append_btn)  #添加行，按钮单独占据一行
        self.address_lineEdit = QLineEdit()
        formLayout.insertRow(4,"地址(&D)：",self.address_lineEdit)  #插入行
        self.class_lineEdit = QLineEdit()
        formLayout.insertRow(4,"班级(&C)：",self.class_lineEdit)  #插入行
        self.textBrowser = QTextBrowser()
        formLayout.addRow(self.textBrowser)  #添加行
        formLayout.setLabelAlignment(Qt.AlignRight)  #对齐方式
        self.append_btn.clicked.connect(self.append_clicked)  #信号与槽函数的连接
    def append_clicked(self):
        sex = "男"
        if self.female_radioButton.isChecked():
            sex = "女"
        template = "姓名：{} 学号：{} 年龄：{} 性别：{} 班级：{} 地址：{}"
        self.textBrowser.append(template.format(self.name_lineEdit.text(),
           self.number_lineEdit.text(),self.age_spinBox.value(),sex,self.class_lineEdit.text(),
           self.address_lineEdit.text()))
if __name__ == '__main__':
    app =QApplication(sys.argv)
    window = myWindow()
    window.show()
    sys.exit(app.exec())
