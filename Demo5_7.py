import sys   #Demo5_7.py
from PySide6.QtWidgets import QApplication,QWidget,QSplitter,QTextBrowser, \
                    QHBoxLayout,QTreeWidget,QTreeWidgetItem
from PySide6.QtCore import Qt

class MyWindow(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.widget_setupUi()
        self.treeWidget_setUp()
    def widget_setupUi(self):  #建立主程序界面
        h = QHBoxLayout(self)
        splitter=QSplitter(Qt.Horizontal,self)
        h.addWidget(splitter)
        self.treeWidget= QTreeWidget()
        self.textBrowser=QTextBrowser()
        splitter.addWidget(self.treeWidget)
        splitter.addWidget(self.textBrowser)
    def treeWidget_setUp(self):  #建立树结构控件
        self.treeWidget.setColumnCount(2)  #设置列数
        header= QTreeWidgetItem()  #表头项
        header.setText(0, "噪声源")
        header.setText(1, "噪声值")
        header.setTextAlignment(0,Qt.AlignCenter)
        header.setTextAlignment(1, Qt.AlignCenter)
        self.treeWidget.setHeaderItem(header)

        self.topItem_1=QTreeWidgetItem(self.treeWidget)  #顶层项
        self.topItem_1.setText(0,"高铁")
        child_1 = QTreeWidgetItem(self.topItem_1,["结构噪声","70"])  #子项
        child_2 = QTreeWidgetItem(self.topItem_1, ["电机噪声", "60"])  #子项
        child_3 = QTreeWidgetItem(self.topItem_1, ["空调噪声","44"])  #子项
        child_4 = QTreeWidgetItem(self.topItem_1, ["气动噪声"])  #子项
        child_5 = QTreeWidgetItem(child_4, ["受电弓噪声","66"])  #子项
        child_6 = QTreeWidgetItem(child_4, ["外壳气流噪声", "66"])  #子项

        self.topItem_2 = QTreeWidgetItem(self.treeWidget)  #顶层项
        self.topItem_2.setText(0, "地铁")
        child_7 = QTreeWidgetItem(self.topItem_2, ["结构噪声", "60"])  #子项
        child_8 = QTreeWidgetItem(self.topItem_2, ["电机噪声", "50"])  #子项
        child_9 = QTreeWidgetItem(self.topItem_2, ["空调噪声", "44"])  #子项
        child_10 = QTreeWidgetItem(self.topItem_2, ["气动噪声"])   #子项
        child_11 = QTreeWidgetItem(child_10, ["受电弓噪声", "56"])  #子项
        child_12 = QTreeWidgetItem(child_10, ["外壳气流噪声", "56"])  #子项

        self.treeWidget.itemClicked.connect(self.treeWidget_clicked)  #信号与槽的连接
        self.treeWidget.expandAll()
    def treeWidget_clicked(self,item,column):
        if item.text(1) !="":
            self.textBrowser.append("噪声源：%s  噪声值：%s"%(item.text(0),item.text(1)))
if __name__ == '__main__':
    app=QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
