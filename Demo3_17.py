import sys,os  #Demo3_17.py
from PySide6.QtWidgets import  QApplication,QWidget,QMenuBar,QPlainTextEdit,QVBoxLayout,QMessageBox,QFileDialog
class MyWindow(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setGeometry(100,100,600,500)
        self.widget_setupUi()
    def widget_setupUi(self):        #建立主程序界面
        menuBar = QMenuBar(self)  #定义菜单栏
        file_menu = menuBar.addMenu("文件(&F)")  #定义文件菜单
        action_open =file_menu.addAction("打开(&O)")
        action_saveAs = file_menu.addAction("另存(&S)")

        self.plainText = QPlainTextEdit(self)  #显示数据控件
        v= QVBoxLayout(self)             #主程序界面的布局
        v.addWidget(menuBar)
        v.addWidget(self.plainText)

        action_open.triggered.connect(self.action_open_triggered)    #信号与槽的连接
        action_saveAs.triggered.connect(self.action_saveAs_triggered) #信号与槽的连接
    def action_open_triggered(self):
        file = QFileDialog(self)
        file.setAcceptMode(QFileDialog.AcceptOpen)
        file.setFileMode(QFileDialog.ExistingFile)
        file.setNameFilter("文本文件(*.txt)")
        if file.exec():
            fileName = file.selectedFiles()
            try:
                fp = open(fileName[0],'r',encoding="UTF-8")
                string = fp.readlines()
                for i in string:
                    self.plainText.appendPlainText(i)
                fp.close()
            except:
                messageBox = QMessageBox(self)
                messageBox.setWindowTitle("文件打开信息")
                messageBox.setText("不能打开文件！")
                messageBox.setInformativeText("请选择UTF-8格式的text文件。")
                messageBox.setDetailedText("重新打开文件，并确保文件格式。")
                messageBox.setIcon(QMessageBox.Information)
                self.btn_accept = messageBox.addButton("重新选择文件",QMessageBox.AcceptRole)
                messageBox.addButton("取消",QMessageBox.RejectRole)
                #如果最后单击的是“重新选择文件”按钮，将再次打开文件对话框
                self.btn_accept.clicked.connect(self.action_open_triggered)
                messageBox.show()
    def action_saveAs_triggered(self):
        fileName,filter = QFileDialog.getSaveFileName(self,"保存文件","d:\\",filter="文本文件(*.txt)")
        if os.path.exists(fileName):
            #如果文件存在，再次提示是否需要覆盖吗？
            button = QMessageBox.warning(self,"再次确认","文件存在，真的要覆盖吗？",QMessageBox.Yes,QMessageBox.No)
            if button == QMessageBox.Yes:
                fp = open(fileName,"w",encoding="UTF-8")
                fp.writelines(self.plainText.toPlainText())
                fp.close()
                QMessageBox.information(self,"提示信息","文件保存完毕。") 
        else:
            fp = open(fileName, "w", encoding="UTF-8")
            fp.writelines(self.plainText.toPlainText())
            fp.close()
            QMessageBox.information(self, "提示信息", "文件保存完毕。") #提示保存完毕
if __name__ == '__main__':
    app=QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
