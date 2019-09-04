#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:McDull Hunsaker
import pymysql
from nltk.stem import WordNetLemmatizer


list_2=[]
list_1=[]
db = pymysql.connect(
        host='localhost',
        port = 3306,
        user='root',
        passwd='root',
        db ='test',
        )
cursor = db.cursor()

key_word = input("search_key_word:")
lemmatizer = WordNetLemmatizer()
#print("Welcome user {name}...".format(name=username))
noun=lemmatizer.lemmatize('{keyname}'.format(keyname=key_word), pos="n")
# print(noun)
adj=lemmatizer.lemmatize('{keyname}'.format(keyname=key_word), pos="a")
# print(adj)

#noun word
#print("________________")
# print("noun word:")
a=cursor.execute("select * from hpodatabase where def like '%{keyname_1}%'; ".format(keyname_1=noun))#精确查找
#print(a)
# fetcall=cursor.fetchall()
# print(fetcall)
list_2.append(cursor.fetchall())
b=cursor.execute("select * from hpodatabase where synonym like '%{keyname_1}%'; ".format(keyname_1=noun))
#print(b)
#print(cursor.fetchall())
list_2.append(cursor.fetchall())
c=cursor.execute("select * from hpodatabase where alt_id like '%{keyname_1}%'; ".format(keyname_1=noun))
#print(c)
#print(cursor.fetchall())
list_2.append(cursor.fetchall())
d=cursor.execute("select * from hpodatabase where is_a_ like '%{keyname_1}%'; ".format(keyname_1=noun))
#print(d)
#print(cursor.fetchall())
list_2.append(cursor.fetchall())
i=cursor.execute("select * from hpodatabase where name like '%{keyname_1}%'; ".format(keyname_1=noun))

#print(cursor.fetchall())
list_2.append(cursor.fetchall())
# t=a+b+c+d+i
# print(t)

#adjective word
#print("________________")
# print("adjective word:")
e=cursor.execute("select * from hpodatabase where def like '%{keyname_1}%'; ".format(keyname_1=adj))#精确查找
#print(e)
# fetcall=cursor.fetchall()
# print(fetcall)
list_2.append(cursor.fetchall())
f=cursor.execute("select * from hpodatabase where synonym like '%{keyname_1}%'; ".format(keyname_1=adj))
#print(f)
#print(cursor.fetchall())
list_2.append(cursor.fetchall())
g=cursor.execute("select * from hpodatabase where alt_id like '%{keyname_1}%'; ".format(keyname_1=adj))
#print(g)
#print(cursor.fetchall())
list_2.append(cursor.fetchall())
h=cursor.execute("select * from hpodatabase where is_a_ like '%{keyname_1}%'; ".format(keyname_1=adj))
#print(h)
k=cursor.execute("select * from hpodatabase where is_a_ like '%{keyname_1}%'; ".format(keyname_1=adj))

#print(cursor.fetchall())
# t=e+f+g+h+k
# print(t)
list_2.append(cursor.fetchall())
for i in list_2:
    for j in i:
        print("______________________")
        print(j)
#print(list_2)



#print(list)
#print(type(list))
# print(b)
# print(c)
# print(d)
key_word = input("search_key_word:")
lemmatizer = WordNetLemmatizer()
#print("Welcome user {name}...".format(name=username))
noun=lemmatizer.lemmatize('{keyname}'.format(keyname=key_word), pos="n")
adj=lemmatizer.lemmatize('{keyname}'.format(keyname=key_word), pos="a")

#noun word
#print("________________")
# print("noun word:")
a=cursor.execute("select * from hpodatabase where def like '%{keyname_1}%'; ".format(keyname_1=noun))#精确查找
#print(a)
# fetcall=cursor.fetchall()
# print(fetcall)
list_1.append(cursor.fetchall())
b=cursor.execute("select * from hpodatabase where synonym like '%{keyname_1}%'; ".format(keyname_1=noun))
#print(b)
#print(cursor.fetchall())
list_1.append(cursor.fetchall())
c=cursor.execute("select * from hpodatabase where alt_id like '%{keyname_1}%'; ".format(keyname_1=noun))
#print(c)
#print(cursor.fetchall())
list_1.append(cursor.fetchall())
d=cursor.execute("select * from hpodatabase where is_a_ like '%{keyname_1}%'; ".format(keyname_1=noun))
#print(d)
#print(cursor.fetchall())

list_1.append(cursor.fetchall())
i=cursor.execute("select * from hpodatabase where name like '%{keyname_1}%'; ".format(keyname_1=noun))
#print(e)
#print(cursor.fetchall())
list_1.append(cursor.fetchall())
# t=a+b+c+d+i
# print(t)

#adjective word
#print("________________")
# print("adjective word:")
e=cursor.execute("select * from hpodatabase where def like '%{keyname_1}%'; ".format(keyname_1=adj))#精确查找
#print(e)
# fetcall=cursor.fetchall()
# print(fetcall)
list_1.append(cursor.fetchall())
f=cursor.execute("select * from hpodatabase where synonym like '%{keyname_1}%'; ".format(keyname_1=adj))
#print(f)
#print(cursor.fetchall())
list_1.append(cursor.fetchall())
g=cursor.execute("select * from hpodatabase where alt_id like '%{keyname_1}%'; ".format(keyname_1=adj))
#print(g)
#print(cursor.fetchall())
list_1.append(cursor.fetchall())
h=cursor.execute("select * from hpodatabase where is_a_ like '%{keyname_1}%'; ".format(keyname_1=adj))
#print(h)
#print(cursor.fetchall())
list_1.append(cursor.fetchall())

j=cursor.execute("select * from hpodatabase where name like '%{keyname_1}%'; ".format(keyname_1=adj))
#print(h)
#print(cursor.fetchall())
list_1.append(cursor.fetchall())
# cursor.fetchall()set
# t=e+f+g+h+j
# print(t)
set1 = set(list_2)
set2 = set(list_1)
list_3=[]
list_4=[]
for i in set1:
    for j in i:
        for k in j:
            list_3.append(k)
# print(list_3)

# print("_______________________________________________________")
for i in set1:
    for j in i:
        for k in j:
            list_4.append(k)
# print(list_4)

set3=set(list_3)
set4=set(list_4)



#print(set1)
print("____________________________________________________________")
#print(set2)
final_result=set3 & set4
#print(final_result)
for i in final_result:
    print(i)
# {4,5}
# [4,5]
cursor.close()
db.close()
#00024
#0005的时候刚好是基因名称
# ('stacey', 0.08652837015341475)
# ('pax2', 0.08496401407835749)
#toxemia