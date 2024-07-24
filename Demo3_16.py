import sys  #Demo3_16.py
from PySide6.QtWidgets import  (QApplication,QWidget,QMenuBar,QPlainTextEdit,
QVBoxLayout,QInputDialog)
class MyWindow(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setWindowTitle("输入信息")
        self.setGeometry(100,100,600,500)
        self.inputDialog = QInputDialog(self)  #创建输入对话框
        self.inputDialog.setOkButtonText("确定")  #定义按钮名称
        self.inputDialog.setCancelButtonText("取消")  #定义按钮名称
        self.widget_setupUi()

    def widget_setupUi(self):  #建立主程序界面
        menuBar = QMenuBar(self)  #定义菜单栏
        primary_menu = menuBar.addMenu("基本信息")  #定义菜单
        action_name =primary_menu.addAction("输入姓名")
        action_sex = primary_menu.addAction("输入性别")
        action_age = primary_menu.addAction("输入年龄")
        action_telephone = primary_menu.addAction("电话号码")
        action_address = primary_menu.addAction("家庭住址")

        self.plainText = QPlainTextEdit(self)  #显示数据控件
        v= QVBoxLayout(self)  #主程序界面的布局
        v.addWidget(menuBar)
        v.addWidget(self.plainText)

        action_name.triggered.connect(self.action_name_triggered)  #动作与信号的连接
        action_sex.triggered.connect(self.action_sex_triggered)  #动作与信号的连接
        action_age.triggered.connect(self.action_age_triggered)  #动作与信号的连接
        action_telephone.triggered.connect(self.action_telephone_triggered)
        action_address.triggered.connect(self.action_address_triggered)
    def action_name_triggered(self):  #姓名动作的槽函数
        self.inputDialog.setWindowTitle("姓名")  #设置对话框窗口的标题名称
        self.inputDialog.setLabelText("输入姓名：")  #设置标签名称
        self.inputDialog.setInputMode(QInputDialog.TextInput) #设置对话框的类型
        if self.inputDialog.exec():  #显示对话框
            self.plainText.appendPlainText("姓名："+self.inputDialog.textValue())
    def action_sex_triggered(self):  #性别动作的槽函数
        self.inputDialog.setLabelText("选择性别：")
        self.inputDialog.setInputMode(QInputDialog.TextInput) #设置对话框类型
        sex=["男","女"]
        self.inputDialog.setComboBoxItems(sex)  #设置文本输入对话框的下拉列表内容
        self.inputDialog.textValueSelected.connect(self.output_sex)  #信号与槽函数连接
        self.inputDialog.exec()
        self.inputDialog.textValueSelected.disconnect(self.output_sex) #信号与槽函数断开
        self.inputDialog.setComboBoxItems(list())  #恢复初始状态
        self.inputDialog.setTextValue("")
    def action_age_triggered(self):  #年龄动作的槽函数
        self.inputDialog.setLabelText("输入年龄：")
        self.inputDialog.setInputMode(QInputDialog.IntInput)
        self.inputDialog.setIntRange(1,200)
        self.inputDialog.setIntStep(1)
        self.inputDialog.open()
        self.inputDialog.intValueSelected.connect(self.output_age)
    def action_telephone_triggered(self):  #电话动作的槽函数
        (number,ok)= QInputDialog.getInt(self,"电话号码","输入电话号码：")
        if ok:
            self.plainText.appendPlainText("电话："+str(number))
    def action_address_triggered(self):  #地址动作的槽函数
        (address,ok)=QInputDialog.getMultiLineText(self,"地址","输入家庭地址：")
        if ok:
            self.plainText.appendPlainText("地址："+address)
    def output_sex(self,sex):  #对话框信号的槽函数
        self.plainText.appendPlainText("性别：" + sex)
    def output_age(self,age):  #对话框信号的槽函数
        self.plainText.appendPlainText("年龄："+str(age))
        self.inputDialog.intValueSelected.disconnect(self.output_age)
if __name__ == '__main__':
    app=QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
