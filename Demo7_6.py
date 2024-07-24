import sys   #Demo7_6.py
from PySide6.QtWidgets import QApplication,QMainWindow,QPlainTextEdit,QFileDialog
from PySide6.QtCore import QDir

class MyWindow(QMainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.resize(800,600)
        self.setupUI()  #界面
    def setupUI(self):  #界面建立
        self.plainText = QPlainTextEdit()
        self.setCentralWidget(self.plainText)
        self.status=self.statusBar()
        self.menubar = self.menuBar()  # 菜单栏
        self.file=self.menubar.addMenu('文件')  #文件菜单
        action_dir=self.file.addAction('选择路径')  #动作
        action_dir.triggered.connect(self.action_dir_triggered)
        self.file.addSeparator()
        action_close = self.file.addAction('关闭')
        action_close.triggered.connect(self.close)
    def action_dir_triggered(self):
        path=QFileDialog.getExistingDirectory(self,caption="选择路径")
        dir = QDir(path)
        dir.setFilter(QDir.Files)  #只显示文件
        if dir.exists(path):
            template = "文件名：{} 文件大小：{}字节 创建日期：{} 修改日期：{} "
            fileInfo_list=dir.entryInfoList()  #获取文件信息列表
            n=len(fileInfo_list)  #文件数量
            if n:  #如果路径下有文件
                self.status.showMessage("选择的路径是："+ dir.toNativeSeparators(path)+
                                        "，该路径下有"+str(n)+"个文件。")
                self.plainText.clear()
                self.plainText.appendPlainText(dir.toNativeSeparators(path)+"下的文件如下：")
                for info in fileInfo_list:
                    string=template.format(info.fileName(),info.size(),
                        info.birthTime().toString(),info.lastModified().toString())
                    self.plainText.appendPlainText(string)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
