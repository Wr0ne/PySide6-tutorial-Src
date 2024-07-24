import sys   #Demo1_19.py
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox
from PySide6.QtCore import Slot, Signal
from student_new import Ui_Form  #导入student_new.py文件中的Ui_Form类

class MyWidget(QWidget):
    numberSignal = Signal(int)  #自定义信号

    def __init__(self,parent = None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.__student = dict()  #记录学生姓名、学号、成绩的字典，关键字是学号
        self.numberSignal.connect(self.isNumberExisting)  #自定义信号与槽函数的连接
    @Slot()
    def on_btnCalculate_clicked(self):
        s = self.ui.chinese.value()+self.ui.math.value()+self.ui.english.value()
        self.ui.total.setText(str(s))
        template = "{:.1f}".format(s/3)
        self.ui.average.setText(template)

        temp = list()
        temp.append(self.ui.name.text())
        temp.append(self.ui.number.value())
        temp.append(self.ui.chinese.value())
        temp.append(self.ui.math.value())
        temp.append(self.ui.english.value())
        temp.append(s)
        temp.append(float(template))
        self.__student[self.ui.number.value()] = temp
    @Slot()
    def on_btnSave_clicked(self):
        template = "姓名{} 学号{} 语文{} 数学{} 英语{} 总成绩{} 平均分{}\n"  #文本模板
        try:
            fp = open("d:\\student_score.txt", 'a+', encoding='UTF-8')  #打开文件
        except:
            print("打开文件失败！")
        else:
            for i in self.__student.values():
                score = template.format(i[0], i[1], i[2], i[3], i[4], i[5], i[6])  #格式化字符串
                fp.write(score)  # 往文件中写入数据
            fp.close()
    @Slot()
    def on_number_editingFinished(self):  #输入学号完成时的槽函数（自动关联的槽函数）
        self.numberSignal.emit(self.ui.number.value())  #发送信号，信号参数是学号
    def isNumberExisting(self,value):
        if value in self.__student:  #如果学号已经存在
            existing=QMessageBox.question(self,"确认信息","该学号已经存在，是否覆盖？",
                            QMessageBox.Yes | QMessageBox.No)   #提示对话框
            if existing == QMessageBox.No:  #如果不覆盖，需要重新输入学号
                self.ui.number.setValue(0)  #学号设置为0，等待重新输入
                self.ui.number.setFocus()   #学号获得焦点
if  __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWidget()
    myWindow.show()
    sys.exit(app.exec())
