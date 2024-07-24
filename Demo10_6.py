import sys  # Demo10_6.py
from PySide6.QtWidgets import (QApplication, QWidget, QComboBox, QTableView, QLabel,
                               QHBoxLayout, QVBoxLayout, QFileDialog, QMenuBar)
from PySide6.QtSql import QSqlDatabase,QSqlQueryModel,QSqlRelation,QSqlRelationalTableModel

class MyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()
    def setupUi(self):  # 建立界面
        menuBar = QMenuBar()
        fileMenu = menuBar.addMenu("文件(&F)")
        fileMenu.addAction("打开(&O)").triggered.connect(self.actionOpen) #信号与槽连接
        fileMenu.addSeparator()
        fileMenu.addAction("关闭(&E)").triggered.connect(self.close)  #信号与槽连接
        label1 = QLabel("选择数据表：")
        self.combox = QComboBox()
        self.combox.currentTextChanged.connect(self.comboxTextChanged) #信号与槽连接
        H1 = QHBoxLayout()
        H1.addWidget(label1, stretch=0); H1.addWidget(self.combox, stretch=1)

        self.tableView_query = QTableView()
        self.tableView_relation = QTableView()
        H2 = QHBoxLayout()
        H2.addWidget(self.tableView_query); H2.addWidget(self.tableView_relation)
        V = QVBoxLayout(self)
        V.addWidget(menuBar); V.addLayout(H1); V.addLayout(H2)
    def actionOpen(self):  # 打开数据库的槽函数
        dbFile, fil = QFileDialog.getOpenFileName(self, dir='d:/',
                                       filter="SQLite(*.db *.db3);;All File(*.*)")
        if dbFile:
          self.setWindowTitle(dbFile)
          self.combox.clear()
          self.db = QSqlDatabase.addDatabase('QSQLITE')
          self.db.setDatabaseName(dbFile)
          if self.db.open():
            self.sqlQueryModel = QSqlQueryModel(self)
            self.tableView_query.setModel(self.sqlQueryModel)  #数据库查询模型
            self.sqlRelationTableModel=QSqlRelationalTableModel(self,self.db)#关系表格模型
            self.sqlRelationTableModel.setEditStrategy(QSqlRelationalTableModel.OnFieldChange)
            self.sqlRelationTableModel.setJoinMode(QSqlRelationalTableModel.InnerJoin)#内连接
            self.tableView_relation.setModel(self.sqlRelationTableModel)
            tables = self.db.tables()
            if len(tables) > 0:
               self.combox.addItems(tables)
    def comboxTextChanged(self, text):  #槽函数
        self.sqlQueryModel.setQuery("SELECT * FROM "+ text)
        self.sqlRelationTableModel.setTable(text)
        if text == "table1":
          self.sqlRelationTableModel.setRelation(4,QSqlRelation("table2","学号",'物理'))#映射关系
          self.sqlRelationTableModel.setRelation(5,QSqlRelation("table2","学号",'化学'))#映射关系
        self.sqlRelationTableModel.select()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyWidget()
    win.show()
    sys.exit(app.exec())
