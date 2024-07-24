import pymysql  #Demo10_2.py

dbName = "mydatabase"  #数据库名称
con = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='12345678',
     database=dbName, charset='utf8')  #数据库连接，数据中有中文时需设置charset='utf8'
cur = con.cursor()  #创建游标

cur.execute('''CREATE TABLE score    
     (ID INTEGER,name TEXT, 语文 REAL, 数学 REAL)''')  #执行SQL命令，创建数据表score
information = ((2001,"张",78,89),(2002,"刘",88,82.5),      #学生考试信息
            (2003,"王",78.5,83),(2004,"张",72.5,86))
cur.executemany("INSERT INTO score VALUES (%s,%s,%s,%s)", information) #执行多条SQL命令
con.commit()   #提交事务
con.close()    #关闭数据库

con = pymysql.connect(host='localhost', port=3306, user='root', password='12345678',
                      db=dbName, charset='utf8')  #重新建立对数据库的连接
cur = con.cursor()  #创建游标
cur.execute("SELECT * From score where name = '张' ") #查询数据表中的内容
rows = cur.fetchall()  #获取数据表中的所有内容
for row in rows:  #输出查询到的内容
    print(row)
con.close()  #关闭数据库
#运行结果如下：
#(2001, '张', 78.0, 89.0)
#(2004, '张', 72.5, 86.0)
