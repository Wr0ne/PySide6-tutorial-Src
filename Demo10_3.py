from PySide6.QtSql import QSqlDatabase,QSqlQuery  #Demo10_3.py
import sqlite3

dbName = "d:/student_score_new.db"  #数据库保存位置和数据库名称
db = QSqlDatabase.addDatabase('QSQLITE')
db.setDatabaseName(dbName)
information1 = ((2011,"张一",78,89),(2012,"刘一",88,82.5),   #学生考试信息
               (2013,"王一",78.5,83),(2014,"张一",72.5,86))
information2 = ((2021,"张二",98,79),(2022,"刘二",83,86.5),   #学生考试信息
               (2023,"王二",88.5,83),(2024,"张二",792.5,89))
if db.open():
    db.exec('''CREATE TABLE score1    
        (ID INTEGER,name TEXT,语文 REAL,数学 REAL)''')  #执行一条SQL命令，创建数据表
    db.exec('''CREATE TABLE score2    
        (ID INTEGER,name TEXT,语文 REAL,数学 REAL)''')  #执行一条SQL命令，创建数据表
    print(db.tables())  # 输出数据库中的表名称
    if db.transaction():
        query = QSqlQuery(db)
        for i in information1:
            query.prepare("INSERT INTO score1 VALUES (?,?,?,?)")  #占位符是?
            query.addBindValue(i[0]);query.addBindValue(i[1])     #按顺序设置占位符的值
            query.bindValue(2,i[2]);query.bindValue(3,i[3])        #按索引设置占位符的值
            query.exec()
        db.commit()   #提交事务
        for i in information2:
            query.prepare("INSERT INTO score2 VALUES (:ID,:name,:chinese,:math)") #占位符是:
            query.bindValue(0,i[0]);query.bindValue(1,i[1])           #按索引设置占位符的值
            query.bindValue(':math',i[3]);query.bindValue(':chinese',i[2])#按名称设置占位符的值
            query.exec()
        db.commit()   #提交事务
    db.close()  #关闭数据库

db_new = QSqlDatabase.addDatabase('QSQLITE') #重新打开数据库并输出一个数据表中的数据
db_new.setDatabaseName(dbName)
if db_new.open():
    query = QSqlQuery(db_new)
    print(query.at())
    if query.exec('SELECT * FROM score1'):
        while query.next():
            print(query.value('ID'),query.value('name'),query.value('语文'),query.value('数学'))
    db_new.close()  #关闭数据库
con = sqlite3.connect(dbName)   #用sqlite3打开数据库，并输出另一个数据表中的数据
cur = con.cursor()  #创建游标
for row in cur.execute("SELECT * From score2"):  #查询数据表中的内容
    print(row)
con.close()  #关闭数据库
