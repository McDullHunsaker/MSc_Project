#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:McDull Hunsaker
import re
import nltk
#import nltk.stem as ns
from nltk.corpus import stopwords
from nltk.text import TextCollection
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from collections import Counter


Word_dict={}

f = open('F:\project\PS3\zhongwen.txt',encoding='UTF-8')

m =f.read()
f1=m.lower()
#print(f1)



#regular expression去掉标点符号
punctuation = '-][%—!,;:?."()&-\''
def removePunctuation(f1):
    text = re.sub(r'[{}]+'.format(punctuation), '', f1)
    return text.strip().lower()
f2=removePunctuation(f1)



list_stopWords = list(set(stopwords.words('english')))
#print(list_stopWords)
list_sentences = sent_tokenize(f2)
tokens =nltk.word_tokenize(f2)#拆分单词,变成一个数组
#print(tokens)#中文分词：结巴分词

#list_words = word_tokenize(f1)
# 过滤停止词
filtered_words = [w for w in tokens if not w in list_stopWords]
#print(filtered_words)



# print(clean_tokens)
# #stemming词干化
# lemmatizer = WordNetLemmatizer()
# for a in clean_tokens:
#     List.append(lemmatizer.lemmatize(a))
# print(List)

# lemmatizer = ns.WordNetLemmatizer()
# for word in filtered_words:
#     # 将名词还原为单数形式
#     #n_lemma = lemmatizer.lemmatize(word, pos='n')
#     # 将动词还原为原型形式
#     v_lemma = lemmatizer.lemmatize(word, pos='v')
#     #List.append(n_lemma)
#     List.append(v_lemma)
#print(List)

#从图中，你可以肯定这篇文章正在谈论 PHP。这很棒！有一些词，如"the," "of," "a," "an," 等等。
# 这些词是停止词。一般来说，停止词语应该被删除，以防止它们影响我们的结果。
# sr = stopwords.words('english')
# for t in List:
#     if t in stopwords.words('english'):
#         List.remove(t)
# print(List)
#
# print("_________________________")

clean_tokens = tokens[:]
freq = nltk.FreqDist(filtered_words)
for key,val in freq.items():
    t=str(key) + ':' + str(val)
#print(t)


# freq.plot(20, cumulative=False)



# data = "All work and no play makes jack dull boy. All work and no play makes jack a dull boy."
# print(sent_tokenize(data))

#tf-idf
all_letters = open('F:\project\PS2\jnew2.txt',encoding='UTF-8')

n=all_letters.read()
f_all_letters=n.lower()
#print(f1)
# punctuation = '!,;:?.()—"\''
# def removePunctuation(f1):
#     text = re.sub(r'[{}]+'.format(punctuation), '', f1)
#     return text.strip().lower()
# f2=removePunctuation(f1)

sents=sent_tokenize(f_all_letters)
chong=[word_tokenize(sent) for sent in sents] #对每个句子进行分词
#print(chong)
#print(sents) #输出分词后的结果
# tokens =nltk.word_tokenize(f2)
corpus=TextCollection(chong) #构建语料库
#print("_______________@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
# print(corpus) #输出语料库


sents_1=sent_tokenize(f1)
chong_1=[word_tokenize(sent) for sent in sents_1]
corpus_1=TextCollection(chong_1)
# print("23333333333333333333333333333333333333333333333########################")
# print(corpus_1)
# print("_________________________")

#计算语料库中"one"的tf值
for a in filtered_words:

    tf=corpus_1.tf(a,corpus_1) # 1/12
    #print(a,"tf:",tf)
    #print(type(a))



#计算语料库中"one"的idf值iii

    idf=corpus.idf(a) #log(3/1)
    #print(a,"idf:",idf)

    tf_idf=tf*idf


    d = dict.fromkeys([a],tf_idf)
    #print(d)
    Word_dict.update(d)

#print("_________________________")
#print(Word_dict)
# from_high_to_low=sorted(Word_dict.items(), key=lambda d:d[1], reverse = False )
from_high_to_low=Counter(Word_dict).most_common() #返回一个列表，按照dict的value从大到小排序

#print(from_high_to_low)
for i in from_high_to_low:
     print(i)


#计算语料库中"one"的tf-idf值
#知道了”词频”（TF）和”逆文档频率”（IDF）以后，将这两个值相乘，就得到了一个词的TF-IDF值。
# 某个词对文章的重要性越高，它的TF-IDF值就越大。所以，排在最前面的几个词，就是这篇文章的关键词。
# tf_idf=corpus.tf_idf('have',corpus)
# print(tf_idf)
#freq.plot(20, cumulative=False)
all_letters.close()
f.close()
# spastic
# spastic
# llpo
#   search_key_word:
#   paraparesis