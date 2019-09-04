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
if not table_exists(cur, 'gene_to_ph'):
        cur.execute("create table gene_to_ph(entrezgeneid varchar(100) ,entrezgenesymbol varchar(200),hpotermname varchar(200),hpotermid varchar(200))")

f = open('F:\project\genes_to_phenotype.txt')
for line in f:
    f1 =f.readline().split()
    list_1=f1
    #print(list_1)
# f1[0]=H_ID
#f1[1:-2]
# f1[-2]=G_ID
# f1[-1]=G_Name
# print(" ".join(f1[1:-2]))
    if len(f1) == 0:
        break
    else:
        #print(f1[0])
        H_ID=f1[0]
        H_name=" ".join(f1[1:-2])
        G_ID=f1[-2]
        G_Name=f1[-1]



# print(H_name)
# print(f1[1:-2])
# print(f1[-2])
# print(f1[-1])






#print(len(f1))
        cur.execute("insert into gene_to_ph values('%s','%s','%s','%s')"%(H_ID,H_name,G_ID,G_Name))


print("finished")

f.close()

#for line in f.readlines():
        #if "Term" in line:

#cur.close() 关闭游标
cur.close()

#conn.commit()方法在提交事物，在向数据库插入一条数据时必须要有这个方法，否则数据不会被真正的插入。
conn.commit()

#conn.close()关闭数据库连接

conn.close()
