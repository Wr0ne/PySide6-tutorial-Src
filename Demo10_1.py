import sqlite3  #Demo10_1.py

dbName = "d:/student_score.db"  #数据库保存位置和数据库名称
con = sqlite3.connect(dbName)  #新建数据库
cur = con.cursor()  #创建游标
cur.execute('''CREATE TABLE score    
     (ID INTEGER,name TEXT, 语文 REAL, 数学 REAL)''') #执行一条SQL命令，创建表格
information = ((2001,"张",78,89),(2002,"刘",88,82.5),   #学生考试信息
               (2003,"王",78.5,83),(2004,"张",72.5,86))
cur.executemany("INSERT INTO score VALUES (?,?,?,?)", information) #执行多条SQL命令
con.commit()   #提交事务
con.close()    #关闭数据库

con = sqlite3.connect(dbName)  #打开数据库
cur = con.cursor()  #创建游标
for row in cur.execute("SELECT * From score"):  #查询数据表中的内容
    print(row)
cur.execute("SELECT * From score Where name = '张' ") #重新查询数据表中的内容
rows = cur.fetchall()  #获取数据表中的所有内容
for row in rows:
    print(row)
con.close()  #关闭数据库
#运行结果如下：
#(2001, '张', 78.0, 89.0)
#(2002, '刘', 88.0, 82.5)
#(2003, '王', 78.5, 83.0)
#(2004, '张', 72.5, 86.0)
#(2001, '张', 78.0, 89.0)
#(2004, '张', 72.5, 86.0)
