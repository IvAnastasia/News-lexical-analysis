# -*- coding: utf-8 -*-
import re

def unigramms(text_name):
    uni_di = {}
    with open(text_name + '.txt', encoding='utf-8') as file:
        words = []
        text = file.read()
        words_li = re.findall("\w+", text)
        for word in words_li:
            unigramm = word.lower()
            words.append(unigramm)
        for unigramm in words:
            if unigramm in uni_di.keys():
                uni_di[unigramm] += 1
            else:
                uni_di[unigramm] = 1
    return uni_di

def bigramms(text_name):
    bigram_di = {}
    with open('rusnews.txt', encoding='utf-8') as file:
        words = []
        text = file.read()
        words_li = re.findall("\w+", text)
        for word in words_li:
            word = word.lower()
            words.append(word)
        for i in range(0, len(words) - 1):
            bigramm = words[i] + ' ' + words[i + 1]
            if bigramm in bigram_di.keys():
                bigram_di[bigramm] += 1
            else:
                bigram_di[bigramm] = 1
    return bigram_di

def trigramms(text_name):
    trigram_di = {}
    with open('rusnews.txt', encoding='utf-8') as file:
        words = []
        text = file.read()
        words_li = re.findall("\w+", text)
        for word in words_li:
            word = word.lower()
            words.append(word)
        for i in range(0, len(words) - 2):
            trigramm = words[i] + ' ' + words[i + 1] + ' ' + words[i + 2]
            if trigramm in trigram_di.keys():
                trigram_di[trigramm] += 1
            else:
                trigram_di[trigramm] = 1
    return trigram_di

#униграммы
unigram_rus = unigramms('rusnews')
for k, v in unigram_rus.items():
    if v > 1:
        print('слово "', k, '" встречается в текстах гос.новостей ', v, ' раз(а)')
unigram_indep = unigramms('rusnews')
for k, v in unigram_indep.items():
    if v > 1:
        print('слово "', k, '" встречается в текстах независимых новостей ', v, ' раз(а)')

#биграммы
bigram_rus = bigramms('rusnews')
for k, v in bigram_rus.items():
    if v > 1:
        print('биграмма "', k, '" встречается в текстах гос.новостей ', v, ' раз(а)')

bigram_indep = bigramms('indepnews')
for k, v in bigram_indep.items():
    if v > 1:
        print('биграмма "', k, '" встречается в текстах независимых новостей ', v, ' раз(а)')

#триграммы
trigram_rus = trigramms('rusnews')
for k, v in trigram_rus.items():
    if v > 1:
        print('триграмма "', k, '" встречается в текстах гос.новостей ', v, ' раз(а)')

trigram_indep = trigramms('indepnews')
for k, v in trigram_indep.items():
    if v > 1:
        print('триграмма "', k, '" встречается в текстах независимых новостей ', v, ' раз(а)')

#а теперь для каждой новости отдельно: сравним частотные уни-, би- и триграммы для каждой новости
#первое число в in range() - номер первой новости, второе число - номер последней новости
for n in range(1, 5):
    print('Текст №' + str(n))
    unigram_rus = unigramms('rusnew' + str(n))
    for k, v in unigram_rus.items():
        if v > 1:
            print('слово "', k, '" встречается в тексте этой гос.новости ', v, ' раз(а)')
    unigram_indep = unigramms('indepnew' + str(n))
    for k, v in unigram_indep.items():
        if v > 1:
            print('слово "', k, '" встречается в тексте этой гос.новости ', v, ' раз(а)')
    bigram_rus = bigramms('rusnew' + str(n))
    for k, v in bigram_rus.items():
        if v > 0:
            print('биграмма "', k, '" встречается в этой гос.новости ', v, ' раз(а)')
    bigram_indep = bigramms('indepnew' + str(n))
    for k, v in bigram_indep.items():
        if v > 0:
            print('биграмма "', k, '" встречается в этой независимой новости ', v, ' раз(а)')
    trigram_rus = trigramms('rusnew' + str(n))
    for k, v in trigram_rus.items():
        if v > 0:
            print('триграмма "', k, '" встречается в этой гос.новости ', v, ' раз(а)')
    trigram_indep = trigramms('indepnew' + str(n))
    for k, v in trigram_indep.items():
        if v > 0:
            print('триграмма "', k, '" встречается в этой независимой новости ', v, ' раз(а)')
