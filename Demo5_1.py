import sys   #Demo5_1.py
from PySide6.QtWidgets import (QApplication,QDialog,QWidget,QPushButton,QMenuBar,
QLabel, QGridLayout,QListWidget,QTextBrowser,QVBoxLayout,QHBoxLayout,QFileDialog)
from PySide6.QtCore import Qt

class MyDialog(QDialog):  #自定义对话框
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setupUi()
    def setupUi(self): #自定义对话框的界面
        label1 = QLabel("选修课科目")
        label2 = QLabel("已选科目")
        self.listWidget_available = QListWidget()  #列表控件
        self.listWidget_selected = QListWidget()  #列表控件
        btn_ok = QPushButton("确定")
        btn_cancel= QPushButton("取消")
        h=QHBoxLayout()  #按钮采用水平布局
        h.addStretch(1)
        h.addWidget(btn_ok)
        h.addWidget(btn_cancel)
        grid = QGridLayout(self)  #标签、列表框采用格栅布局
        grid.addWidget(label1,0,0)
        grid.addWidget(label2,0,1)
        grid.addWidget(self.listWidget_available,1,0)
        grid.addWidget(self.listWidget_selected,1,1)
        grid.addLayout(h,2,0,1,2)
        class_available= ["语文0","数学1","物理2","化学3","地理4","历史5",
"生物6","哲学7","测量8"]
        self.listWidget_available.addItems(class_available) #添加项
        for i in range(self.listWidget_available.count()):#用角色数据记录项的初始位置
            item = self.listWidget_available.item(i)  #获取项
            item.setData(Qt.UserRole,i)  #设置项的角色值，值为行号
        self.listWidget_available.itemClicked.connect(self.listWidget_available_clicked)
        self.listWidget_selected.itemClicked.connect(self.listWidget_selected_clicked)
        btn_ok.clicked.connect(self.btn_ok_clicked)  #“确定”按钮的单击
        btn_cancel.clicked.connect(self.btn_cancel_clicked)  #“取消”按钮的单击
    def listWidget_available_clicked(self,item):  #列表控件的单击槽函数
        row=self.listWidget_available.row(item)  #获取项的行号
        self.listWidget_available.takeItem(row)  #移除项
        i = item.data(Qt.UserRole)  #移除项的角色值
        for j in range(self.listWidget_selected.count()):
            if i < self.listWidget_selected.item(j).data(Qt.UserRole):
                self.listWidget_selected.insertItem(j, item) #根据角色值插入到列表中
        self.listWidget_selected.addItem(item)
    def listWidget_selected_clicked(self,item):  #列表控件的单击槽函数
        row = self.listWidget_selected.row(item)
        self.listWidget_selected.takeItem(row)
        i = item.data(Qt.UserRole)
        for j in range(self.listWidget_available.count()):
            if i < self.listWidget_available.item(j).data(Qt.UserRole):
                self.listWidget_available.insertItem(j, item)
        self.listWidget_available.addItem(item)
    def btn_ok_clicked(self):  # “确定”按钮的槽函数
        self.setResult(QDialog.Accepted)
        self.setVisible(False)
    def btn_cancel_clicked(self):  # “取消”按钮的槽函数
        self.setResult(QDialog.Rejected)
        self.setVisible(False)
class MyWindow(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.widget_setupUi()
    def widget_setupUi(self):  #建立主程序界面
        menuBar = QMenuBar(self)  #定义菜单栏
        file_menu = menuBar.addMenu("文件(&F)")  #定义菜单
        action_selection = file_menu.addAction("选修课(&C)")  #添加动作
        action_save = file_menu.addAction("保存(&S)")  #添加动作
        file_menu.addSeparator()
        action_exit = file_menu.addAction("退出(&E)")  #添加动作
        self.textBrowser = QTextBrowser(self)  #显示数据控件
        v= QVBoxLayout(self)  #主程序界面的布局
        v.addWidget(menuBar)
        v.addWidget(self.textBrowser)
        action_selection.triggered.connect(self.action_selection_triggered) #信号与槽连接
        action_save.triggered.connect(self.action_save_triggered) #信号与槽的连接
        action_exit.triggered.connect(self.close)  #退出动作的信号与窗口关闭的连接
    def action_selection_triggered(self):  #自定义槽函数
        dialog = MyDialog (self)  #自定义对话框实例
        if dialog.exec():  #模式显示对话框
            n= dialog.listWidget_selected.count()
            text="你选择的选修课是："
            if n>0:
                for i in range(n):
                    text=text+"  "+dialog.listWidget_selected.item(i).text()
                self.textBrowser.append(text)
            else:
                self.textBrowser.append("你没有选择任何选修课!")
    def action_save_triggered(self):  #自定义槽函数
        string = self.textBrowser.toPlainText()
        if len(string) > 0:
            filename, filter = QFileDialog.getSaveFileName(self, "保存文件",
                                             "d:\\", "文本文件(*.txt)")
            if len(filename) > 0:
                fp = open(filename, "a+", encoding="UTF-8")
                fp.writelines(string)
                fp.close()
if __name__ == '__main__':
    app=QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
