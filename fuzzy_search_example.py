#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:McDull Hunsaker

import pymysql

db = pymysql.connect(
        host='localhost',
        port = 3306,
        user='root',
        passwd='root',
        db ='test',
        )
cursor = db.cursor()
list_1=[]
#cursor.execute("select*from hpodatabase where id like '%44%';")#模糊查询
cursor.execute("select * from ph_to_gene where genename like '%pax2%'; ")#精确查找
list_1.append(cursor.fetchall())
for i in list_1:
    for j in i:
        print(j)
cursor.close()
db.close()
