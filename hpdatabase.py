#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:McDull Hunsaker
import MySQLdb
import re

def table_exists(con, table_name):#这个函数用来判断表是否存在
    sql = "show tables;"
    con.execute(sql)
    tables = [con.fetchall()]
    table_list = re.findall('(\'.*?\')',str(tables))
    table_list = [re.sub("'",'',each) for each in table_list]
    if table_name in table_list:
        return 1#存在返回1
    else:
        return 0#不存在返回

conn= MySQLdb.connect(
        host='localhost',
        port = 3306,
        user='root',
        passwd='root',
        db ='test',
        )
#通过获取到的数据库连接conn下的cursor()方法来创建游标。
cur = conn.cursor()

#创建数据表,通过游标cur 操作execute()方法可以写入纯sql语句。通过execute()方法中写如sql语句来对数据进行操作
if not table_exists(cur, 'hpodatabase'):
        cur.execute("create table HPOdatabase(id varchar(100) ,name varchar(3000),def varchar(3000),synonym varchar(3000),alt_id varchar(2000),is_a_ varchar(3000))")

#插入一条数据
# cur.execute("insert into HPOdatabase values('%s','%s','%s','%s','%s','%s').")
f = open('F:\project\hp.obo1.txt')
# for line in f:
#     if "def" in line:
#         line = line.replace("def","definition")
# print(f.read())
f1 =f.read().split("[Term]")

#print(len(f1))

for i in f1:
        id = ''
        name = ''
        definition = ''
        alt_id = ''
        synonym = ''
        is_a = ''
        # print(i)
        j = i.split("\n")
        for k in j:
                l = k.split(": ")
                # print(k)

                if 'id' in l:
                        id += l[1]
                        # print(id)
                if 'name' in l:
                        name +=l[1]
                        # print(name)

                if 'def' in l:
                        definition+=l[1]
                        # print(definition)
                if 'alt_id' in l:
                        alt_id+=l[1]
                        alt_id+=","
                        # print(alt_id)
                        # print(alt_id)
                if 'synonym' in l:
                        synonym+=l[1]
                        synonym += ","
                        # print(synonym)
                if 'is_a' in l:
                        is_a+=l[1]
                        is_a+=","
                        # print(is_a)

                # if "name" in k.split():
        #print("insert into HPOdatabase values('%s','%s','%s','%s','%s','%s')"%(id,name,definition,synonym,alt_id,is_a))
        cur.execute("insert into HPOdatabase values('%s','%s','%s','%s','%s','%s')"%(id,name,definition,synonym,alt_id,is_a))

        #conn.commit()
print('-----------------------------finished')
# print(definition)
# print("insert into HPOdatabase values(%s,%s,%s,%s,%s,%s)" % (id,name,definition,synonym,alt_id,is_a))
                # print(len(k))
                # print('------')
f.close()

#for line in f.readlines():
        #if "Term" in line:

#cur.close() 关闭游标
cur.close()

#conn.commit()方法在提交事物，在向数据库插入一条数据时必须要有这个方法，否则数据不会被真正的插入。
conn.commit()

#conn.close()关闭数据库连接

conn.close()
