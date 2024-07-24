import sys  #Demo3_19.py
from PySide6.QtWidgets import  (QApplication,QWidget,QMenuBar,QPlainTextEdit,
QVBoxLayout, QWizard,QWizardPage,QMessageBox,QPushButton,QLineEdit,QFormLayout)

class QWizardPage_1(QWizardPage):  #第1个向导页类
    def __init__(self,parent=None):
        super().__init__(parent)
        form= QFormLayout(self)
        self.line_name = QLineEdit()
        self.line_number = QLineEdit()
        form.addRow("姓名：",self.line_name)
        form.addRow("学号：",self.line_number)
        self.setTitle("学生成绩输入系统")
        self.setSubTitle("基本信息")
        self.line_name.textChanged.connect(self.isComplete)
        self.line_number.textChanged.connect(self.isComplete)
        self.line_name.textChanged.connect(self.completeChanged_emit)
        self.line_number.textChanged.connect(self.completeChanged_emit)

        self.registerField("name",self.line_name)  #创建字段
        self.registerField("number",self.line_number)  #创建字段
    def isComplete(self):  #重写isComplete()函数
        if self.line_name.text() != "" and self.line_number.text() != "":
            return True
        else:
            return False
    def completeChanged_emit(self):  #重写isComplete()函数后，需要重新发送信号
        self.completeChanged.emit()
    def validatePage(self):  #重写validatePage()函数
        if self.line_number.text().isdigit():  #确保学号中输入的是数字
            return True
        else:
            QMessageBox.warning(self,"警告","输入有误，请检查输入的信息。")
            return False
class QWizardPage_2(QWizardPage):  #第2个向导页类
    def __init__(self,parent=None):
        super().__init__(parent)
        form= QFormLayout(self)
        self.line_telephone = QLineEdit()
        self.line_address = QLineEdit()
        form.addRow("电话：",self.line_telephone)
        form.addRow("地址：",self.line_address)
        self.setTitle("学生成绩输入系统")
        self.setSubTitle("联系方式")
        
        self.registerField("telephone",self.line_telephone)  #创建字段
        self.registerField("address",self.line_address)  #创建字段
class QWizardPage_3(QWizardPage):  #第3个向导页类
    def __init__(self,parent=None):
        super().__init__(parent)
        form= QFormLayout(self)
        self.line_chinese = QLineEdit()
        self.line_math = QLineEdit()
        self.line_english = QLineEdit()
        form.addRow("语文：",self.line_chinese)
        form.addRow("数学：",self.line_math)
        form.addRow("英语：", self.line_english)
        self.setTitle("学生成绩输入系统")
        self.setSubTitle("考试成绩")
        
        self.registerField("chinese",self.line_chinese)  #创建字段
        self.registerField("math",self.line_math)   #创建字段
        self.registerField("english",self.line_english)  #创建字段
class QWizard_studentnumber(QWizard):  #向导对话框
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setWizardStyle(QWizard.ModernStyle)
        self.addPage(QWizardPage_1(self))  #添加向导页
        self.addPage(QWizardPage_2(self))  #添加向导页
        self.addPage(QWizardPage_3(self))  #添加向导页

        self.btn_back = QPushButton("上一步")
        self.btn_next = QPushButton("下一步")
        self.btn_finish = QPushButton("完成")
        self.setButton(QWizard.BackButton, self.btn_back)  #添加按钮
        self.setButton(QWizard.NextButton, self.btn_next)  #添加按钮
        self.setButton(QWizard.FinishButton, self.btn_finish)  #添加按钮
        self.setButtonLayout([self.Stretch,self.BackButton,self.NextButton,self.FinishButton]) 
class MyWindow(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.widget_setupUi() #建立主界面
        self.wizard = QWizard_studentnumber(self)  #实例化向导对话框
        self.wizard.btn_finish.clicked.connect(self.btn_finish_clicked) #完成按钮信号与槽的连接
    def widget_setupUi(self):  #建立主程序界面
        menuBar = QMenuBar(self)  #定义菜单栏
        file_menu = menuBar.addMenu("文件(&F)")  #定义文件菜单
        action_enter =file_menu.addAction("进入")
        action_enter.triggered.connect(self.action_enter_triggered) #动作的信号与槽函数的连接
        self.plainText = QPlainTextEdit(self)  #显示数据控件
        v= QVBoxLayout(self)  #主界面的布局
        v.addWidget(menuBar)
        v.addWidget(self.plainText)
    def action_enter_triggered(self):  #动作的槽函数
        self.wizard.setStartId(0)
        self.wizard.restart()
        self.wizard.open()
    def btn_finish_clicked(self): #单击最后一页的“完成”按钮，输入的数据在plainText中显示
        template="姓名：{} 学号：{} 电话：{} 地址：{} 语文：{} 数学：{} 英语：{}"
        string=template.format(self.wizard.field("name"),self.wizard.field("number"), self.wizard.field("telephone"),self.wizard.field("address"),self.wizard.field("chinese"),
        self.wizard.field("math"),self.wizard.field("english")) #获取字段值，格式化输出文本
        self.plainText.appendPlainText(string)
if __name__ == '__main__':
    app=QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
