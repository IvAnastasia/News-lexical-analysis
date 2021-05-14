#!/usr/bin/env python
# coding: utf-8

! pip install pymorphy2
import pymorphy2
morph = pymorphy2.MorphAnalyzer()

import string

#количество опредленных слов в тексте
def count_words(text: str, words: list):
    morph = pymorphy2.MorphAnalyzer()
# избавились от пунктуации
    for c in string.punctuation:
        text = text.replace(c, "")
    report = {w: 0 for w in words}
    all_words = text.split()
    for word in all_words:
        word_normal_form = morph.parse(word)[0].normal_form
        if word_normal_form in report:
            report[word_normal_form] += 1
    return report

words = ['русский', 'российский', 'западный', 'американский']

for n in range(1, 5):
    print('Текст №' + str(n))
    with open('rusnew' + str(n) + '.txt', encoding = 'utf-8') as file:
        text = file.read()
        print('Гос.новость: ', count_words(text, words))
    with open('indepnew' + str(n) + '.txt', encoding = 'utf-8') as file:
        text = file.read()
        print('Независимая новость: ', count_words(text, words))
   
print('Всего')
with open('rusnews.txt', encoding = 'utf-8') as file:
        text = file.read()
        print('Гос.новости: ', count_words(text, words))
with open('indepnews.txt', encoding = 'utf-8') as file:
        text = file.read()
        print('Независимые новости: ', count_words(text, words))
