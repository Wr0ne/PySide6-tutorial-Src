import sys  #Demo10_4.py
from PySide6.QtWidgets import QApplication,QWidget,QComboBox,QTableView,QLabel,\
    QHBoxLayout,QVBoxLayout,QFileDialog,QMenuBar
from PySide6.QtSql import QSqlDatabase,QSqlQueryModel
from PySide6.QtCore import Qt

class MyWidget(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self. setupUi()
    def setupUi(self):  #建立界面
        menuBar = QMenuBar()
        fileMenu = menuBar.addMenu("文件(&F)")
        fileMenu.addAction("打开(&O)").triggered.connect(self.actionOpen)#信号与槽连接
        fileMenu.addSeparator()
        fileMenu.addAction("关闭(&E)").triggered.connect(self.close) #信号与槽连接

        label = QLabel("选择数据表：")
        self.combox = QComboBox()
        self.combox.currentTextChanged.connect(self.comboxTextChanged)#信号与槽连接
        H = QHBoxLayout()
        H.addWidget(label,stretch=0);H.addWidget(self.combox,stretch=1)

        self.tableView = QTableView()
        self.tableView.setAlternatingRowColors(True)
        V = QVBoxLayout(self)
        V.addWidget(menuBar);V.addLayout(H);V.addWidget(self.tableView)
    def actionOpen(self):  #槽函数
        dbFile, fil=QFileDialog.getOpenFileName(self, dir='d:/',
                                   filter = "SQLite(*.db *.db3);; All File(*.*)")
        if dbFile:
            self.setWindowTitle(dbFile)
            self.combox.clear()
            self.db = QSqlDatabase.addDatabase('QSQLITE')  #数据库连接
            self.db.setDatabaseName(dbFile)
            self.sqlQueryModel = QSqlQueryModel(self)  #数据库查询模型
            if self.db.open():
                tables = self.db.tables()
                if len(tables) > 0:
                    self.combox.addItems(tables)
    def comboxTextChanged(self,text):  #槽函数
        self.sqlQueryModel.setQuery("SELECT * FROM {}".format(text),self.db) #设置查询
        header = self.sqlQueryModel.record()  #获取字段头部的记录
        for i in range(header.count()):
          self.sqlQueryModel.setHeaderData(i,Qt.Horizontal,header.fieldName(i),
Qt.DisplayRole)
        self.tableView.setModel(self.sqlQueryModel)  #设置表格视图的数据模型
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyWidget()
    win.show()
    sys.exit(app.exec())
