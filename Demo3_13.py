import sys  #Demo3_13.py
from PySide6.QtWidgets import (QApplication,QDialog,QWidget,QPushButton,QLineEdit, 
      QMenuBar,QTextBrowser,QVBoxLayout,QHBoxLayout,QFormLayout,QFileDialog)
class MyWindow(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setWindowTitle("学生成绩输入系统")
        self.widget_setupUi()
        self.dialog_setupUi()
    def widget_setupUi(self):  #建立主程序界面
        menuBar = QMenuBar(self)  #定义菜单栏
        file_menu = menuBar.addMenu("文件(&F)")  #定义菜单
        action_input = file_menu.addAction("输入成绩(&I)")  #添加动作
        action_save = file_menu.addAction("保存(&S)")  #添加动作
        file_menu.addSeparator()
        action_exit = file_menu.addAction("退出(&E)")  #添加动作
        self.textBrowser = QTextBrowser(self)  #显示数据控件
        v= QVBoxLayout(self)  #主程序界面的布局
        v.addWidget(menuBar)
        v.addWidget(self.textBrowser)

        action_input.triggered.connect(self.action_input_triggered)  #信号与槽函数连接
        action_save.triggered.connect(self.action_save_triggered)   #信号与函数槽连接
        action_exit.triggered.connect(self.close)   #信号与槽函数连接
    def dialog_setupUi(self):  #建立对话框界面
        self.dialog = QDialog(self)
        self.btn_apply = QPushButton("应用")
        self.btn_ok = QPushButton("确定")
        self.btn_cancel = QPushButton("取消")
        h = QHBoxLayout()
        h.addWidget(self.btn_apply)
        h.addWidget(self.btn_ok)
        h.addWidget(self.btn_cancel)
        self.line_name = QLineEdit()
        self.line_number = QLineEdit()
        self.line_chinese = QLineEdit()
        self.line_math = QLineEdit()
        self.line_english = QLineEdit()
        f = QFormLayout(self.dialog)
        f.addRow("姓名：", self.line_name)
        f.addRow("学号：", self.line_number)
        f.addRow("语文：", self.line_chinese)
        f.addRow("数学：", self.line_math)
        f.addRow("英语：", self.line_english)
        f.addRow(h)
        self.btn_apply.clicked.connect(self.btn_apply_clicked)  #信号与槽函数连接
        self.btn_ok.clicked.connect(self.btn_ok_clicked)   #信号与槽函数连接
        self.btn_cancel.clicked.connect(self.dialog.close)   #信号与槽函数连接
    def action_input_triggered(self):  #自定义槽函数
        self.dialog.open()
    def action_save_triggered(self):  #自定义槽函数
        string = self.textBrowser.toPlainText()
        if len(string) > 0:
            filename, filter = QFileDialog.getSaveFileName(self, "保存文件",
                                             "d:\\", "文本文件(*.txt)")
            if len(filename) > 0:
                fp = open(filename, "a+", encoding="UTF-8")
                fp.writelines(string)
                fp.close()
    def btn_apply_clicked(self):   #自定义槽函数，单击“应用”按钮
        template="姓名：{}  学号：{}  语文：{}  数学：{}  英语：{}"
        string = template.format(self.line_name.text(),self.line_number.text(),
               self.line_chinese.text(),self.line_math.text(),self.line_english.text())
        self.textBrowser.append(string)
        self.line_name.clear()
        self.line_number.clear()
        self.line_chinese.clear()
        self.line_math.clear()
        self.line_english.clear()
    def btn_ok_clicked(self):   #自定义槽函数，单击“确定”按钮
        self.btn_apply_clicked()
        self.dialog.close()
if __name__ == '__main__':
    app=QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
