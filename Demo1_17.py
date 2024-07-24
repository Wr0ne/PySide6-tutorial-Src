import sys  #Demo1_17.py
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import Slot
from student import Ui_Form  #导入student.py文件中的Ui_Form类

class MyWidget(QWidget):
    def __init__(self,parent = None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.__count = 0
        self.__score = list()
        self.ui.btnCalculate.clicked.connect(self.scoreCalculate)  #手动连接信号与槽
    def scoreCalculate(self):   #“计算”按钮的槽函数，需手动与信号连接
        s = self.ui.chinese.value()+self.ui.math.value()+self.ui.english.value()
        self.ui.total.setText(str(s))
        template = "{:.1f}".format(s/3)
        self.ui.average.setText(template)

        self.__count = self.__count + 1
        temp = list()
        temp.append(self.__count)
        temp.append(self.ui.chinese.value())
        temp.append(self.ui.math.value())
        temp.append(self.ui.english.value())
        temp.append(s)
        temp.append(float(template))
        self.__score.append(temp)
    @Slot()  #槽参数类型修饰符
    def on_btnSave_clicked(self):   #自动关联槽函数
        template = "{}:语文{} 数学{} 英语{} 总成绩{} 平均分{}\n"  #定义文本模板
        try:
            fp = open("d:\\student_score.txt",'a+',encoding='UTF-8')  #打开文件
        except:
            print("打开文件失败！")
        else:
            for i in self.__score:
                score = template.format(i[0],i[1],i[2],i[3],i[4],i[5])  #格式化字符串
                fp.write(score)   #往文件中写入数据
            fp.close()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWidget()
    myWindow.show()
    #myWindow.ui.btnCalculate.clicked.connect(myWindow.scoreCalculate)  #手动连接信号与槽
    sys.exit(app.exec())
