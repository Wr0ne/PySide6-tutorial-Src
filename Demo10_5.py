import sys  # Demo10_5.py
from PySide6.QtWidgets import (QApplication, QWidget, QComboBox, QTableView, QLabel,
          QPushButton, QHBoxLayout, QVBoxLayout, QFileDialog, QMenuBar, QGroupBox,
          QLineEdit, QSpinBox, QDoubleSpinBox)
from PySide6.QtSql import QSqlDatabase, QSqlTableModel, QSqlRecord
from PySide6.QtCore import Qt

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
        H1 = QHBoxLayout()
        H1.addWidget(label1, stretch=0);
        H1.addWidget(self.combox, stretch=1)
        label2 = QLabel("学号："); self.spin_ID = QSpinBox()
        label3 = QLabel("姓名："); self.lineEdit_name = QLineEdit()
        label4 = QLabel("语文："); self.doubleSpin_chinese = QDoubleSpinBox()
        label5 = QLabel("数学："); self.doubleSpin_math = QDoubleSpinBox()
        self.pushButton_add = QPushButton("在当前位置添加记录")
        self.groupBox1 = QGroupBox("添加记录")
        self.groupBox1.setEnabled(False)
        H2 = QHBoxLayout(self.groupBox1)
        H2.addWidget(label2, 0); H2.addWidget(self.spin_ID, 1)
        H2.addWidget(label3, 0); H2.addWidget(self.lineEdit_name, 1)
        H2.addWidget(label4, 0); H2.addWidget(self.doubleSpin_chinese, 1)
        H2.addWidget(label5, 0); H2.addWidget(self.doubleSpin_math, 1)
        H2.addWidget(self.pushButton_add)
        label6 = QLabel("删除行："); self.spin_deleteLine = QSpinBox()
        self.pushButton_delete = QPushButton("删除指定的记录")
        self.pushButton_delete_cur = QPushButton("删除当前记录")
        self.groupBox2 = QGroupBox("删除记录")
        self.groupBox2.setEnabled(False)
        H3 = QHBoxLayout(self.groupBox2)
        H3.addWidget(label6, 0); H3.addWidget(self.spin_deleteLine, 1)
        H3.addWidget(self.pushButton_delete); H3.addWidget(self.pushButton_delete_cur)

        self.tableView = QTableView()
        self.tableView.setAlternatingRowColors(True)
        V = QVBoxLayout(self)
        V.addWidget(menuBar); V.addLayout(H1); V.addWidget(self.groupBox1)
        V.addWidget(self.groupBox2); V.addWidget(self.tableView)

        self.combox.currentTextChanged.connect(self.comboxTextChanged) #信号与槽连接
        self.pushButton_add.clicked.connect(self.pushButton_add_clicked) #信号与槽连接
        self.pushButton_delete.clicked.connect(self.pushButton_delete_clicked) 
        self.pushButton_delete_cur.clicked.connect(self.pushButton_delete_cur_clicked)
    def actionOpen(self):  # 打开数据库的槽函数
        dbFile, fil = QFileDialog.getOpenFileName(self, dir='d:/',
                                     filter="SQLite(*.db *.db3);;All File(*.*)")
        if dbFile:
            self.setWindowTitle(dbFile)
            self.combox.clear()
            self.db = QSqlDatabase.addDatabase('QSQLITE')
            self.db.setDatabaseName(dbFile)
            if self.db.open():
                self.sqlTableModel = QSqlTableModel(self, self.db)  #数据库表格模型
                self.sqlTableModel.setEditStrategy(QSqlTableModel.OnFieldChange)
                self.tableView.setModel(self.sqlTableModel)
                tables = self.db.tables()
                if len(tables) > 0:
                    self.combox.addItems(tables)
                    self.groupBox1.setEnabled(True)
                    self.groupBox2.setEnabled(True)
                else:
                    self.groupBox1.setEnabled(False)
                    self.groupBox2.setEnabled(False)
    def comboxTextChanged(self, text):  #槽函数
        self.sqlTableModel.setTable(text)
        self.sqlTableModel.select()
        header = self.sqlTableModel.record()  #获取字段头部的记录
        for i in range(header.count()):
          self.sqlTableModel.setHeaderData(i,Qt.Horizontal,header.fieldName(i),Qt.DisplayRole)
    def pushButton_add_clicked(self):  #槽函数
        record = QSqlRecord(self.sqlTableModel.record())  #创建记录
        record.setValue("ID", self.spin_ID.value())  #设置记录的值
        record.setValue("name", self.lineEdit_name.text())
        record.setValue("语文", self.doubleSpin_chinese.value())
        record.setValue("数学", self.doubleSpin_math.value())
        self.spin_ID.setValue(self.spin_ID.value() + 1)

        currentRow = self.tableView.currentIndex().row()
        if not self.sqlTableModel.insertRecord(currentRow+1, record):  #插入行
            self.sqlTableModel.select()
    def pushButton_delete_clicked(self):  #槽函数
        row = self.spin_deleteLine.value()
        if row > 0 and row <= self.sqlTableModel.rowCount():
            if self.sqlTableModel.removeRow(row - 1):  #删除行
                self.sqlTableModel.select()  #重新查询数据
    def pushButton_delete_cur_clicked(self):
        currentRow = self.tableView.currentIndex().row()
        if self.sqlTableModel.removeRow(currentRow):  #删除行
            self.sqlTableModel.select()  #重新查询数据
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyWidget()
    win.show()
    sys.exit(app.exec())
