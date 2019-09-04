#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:McDull Hunsaker

import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize

import pymysql

db = pymysql.connect(
        host='localhost',
        port = 3306,
        user='root',
        passwd='root',
        db ='test',
        )
cursor = db.cursor()

Word_dict={}

f = open('F:\project\PS3\zhongwen.txt',encoding='UTF-8')

m =f.read()
f1=m.lower()
#print(f1)

a=0
list_1=[]


#regular expression去掉标点符号
punctuation = '%—!,;:?."()&-\''
def removePunctuation(f1):
    text = re.sub(r'[{}]+'.format(punctuation), '', f1)
    return text.strip().lower()
f2=removePunctuation(f1)
#print(f2)

#print("___________________________________________________________________________________")

list_stopWords = list(set(stopwords.words('english')))
list_sentences = sent_tokenize(f2)
tokens =nltk.word_tokenize(f2)#拆分单词,变成一个数组
#print(tokens)#中文分词：结巴分词

#list_words = word_tokenize(f1)
# 过滤停止词
filtered_words = [w for w in tokens if not w in list_stopWords]
# print(filtered_words)
key_word = int(input("How many word in a phrase you want to look up into a letter:"))
for i in filtered_words:

    # print(filtered_words[a:a+2])
    together=filtered_words[a:a+key_word]

    key_phrase=" ".join(str(i) for i in together)
    list_1.append(key_phrase)
    a=a+1
    # for i in list_1:
    #     print(i)
#print(list_1)



#match

for b in list_1:
    list_2 = []
    cursor.execute("select * from hpodatabase where def like '%{keyphrase}%'; ".format(keyphrase=b))
    list_2.append(cursor.fetchall())
    cursor.execute("select * from hpodatabase where synonym like '%{keyphrase}%'; ".format(keyphrase=b))
    list_2.append(cursor.fetchall())
    cursor.execute("select * from hpodatabase where alt_id like '%{keyphrase}%'; ".format(keyphrase=b))
    list_2.append(cursor.fetchall())
    cursor.execute("select * from hpodatabase where is_a_ like '%{keyphrase}%'; ".format(keyphrase=b))
    list_2.append(cursor.fetchall())
    cursor.execute("select * from hpodatabase where is_a_ like '%{keyphrase}%'; ".format(keyphrase=b))
    list_2.append(cursor.fetchall())
    if list_2[0]==() and list_2[1]==() and list_2[2]==() and list_2[3]==() and list_2[4]==():
        continue
    else:
        for m in list_2:
            # print(m)
            for n in m:
                list_n=list(n)
                print(b,":",list_n)
                print("\n")
                # for h in list_n:
                #     if h =='':
                #         continue
                #     else:
                #         print(b, ":", h)
                # #print(type(h))
                    # if list_n[a] is None:
                    #     continue
                    # else:



                # if m[a]==():
                #     continue
                # else:
                #     a=a+1
                #     print(b,":",m[a])



cursor.close()
db.close()
