#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:McDull Hunsaker
from textrank4zh import TextRank4Keyword, TextRank4Sentence
import codecs

file = r"F:\project\PS3\zhongwen.txt"
text = codecs.open(file, 'r', 'utf-8').read()

word = TextRank4Keyword()

word.analyze(text, window=2, lower=True)
w_list = word.get_keywords(num=20, word_min_len=1)

print('keyword:')

for w in w_list:
    print(w.word, w.weight)

phrase = word.get_keyphrases(keywords_num=5, min_occur_num=2)

print(phrase)
print('keyphrase:')

for p in phrase:
    print(p)

sentence = TextRank4Sentence()

sentence.analyze(text, lower=True)
s_list = sentence.get_key_sentences(num=3, sentence_min_len=5)

print('keysentence:')

for s in s_list:
    print(s.sentence, s.weight)




