#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# средняя длина предложения
import re


def sentence_report(text: str):
    report = {
        'mean_symbol_sentence': 0,
        'mean_word_sentence': 0,
    }
    sentences = re.split(r'[.?!]', text)
    report['mean_symbol_sentence'] = sum(
        [len(s) for s in sentences]) / len(sentences) # средняя длина предложения в символах
    report['mean_word_sentence'] = sum(
        [len(s.split()) for s in sentences]) / len(sentences) # средняя длина предложения в словах
    return report

#сравним по всем новостям сразу
with open('rusnews.txt', encoding='utf-8') as file:
    text = file.read()
    ans = sentence_report(text)
    print('Гос. новости, средняя длина предложения в символах: ', ans['mean_symbol_sentence'], ', в словах: ', ans['mean_word_sentence'])
with open('indepnews.txt', encoding='utf-8') as file:
    text = file.read()
    ans = sentence_report(text)
    print('Независимые новости, средняя длина предложения в символах: ', ans['mean_symbol_sentence'], ', в словах: ', ans['mean_word_sentence'])

#сравним по каждой новости отдельно

sym_rus_num = 0
sym_indep_num = 0
for n in range(1, 2):
    print('Текст №' + str(n))
    with open('rusnew' + str(n) + '.txt', encoding='utf-8') as file:
        text = file.read()
        ans = sentence_report(text)
        rus_sym = ans['mean_symbol_sentence']
        rus_word = ans['mean_word_sentence']
        print('Гос. новость, средняя длина предложения в символах: ', rus_sym, ', в словах', rus_word)
    with open('indepnew' + str(n) + '.txt', encoding='utf-8') as file:
        text = file.read()
        ans = sentence_report(text)
        indep_sym = ans['mean_symbol_sentence']
        indep_word = ans['mean_word_sentence']
        print('Независимая новость, средняя длина предложения в символах', indep_sym, ', в словах: ', indep_word)
    if rus_sym > indep_sym:
        sym_rus_num += 1
        print('Среднее количество символов больше в гос.новости')
    elif indep_sym > rus_sym:
        sym_indep_num += 1
        print('Среднее количество символов больше в независимой новости')
if sym_rus_num > sym_indep_num:
    print('В целом гос. новостей, в которых символов больше, больше: ', sym_rus_num, 'vs.', sym_indep_num)
elif sym_rus_num < sym_indep_num:
    print('В целом независимых новостей, в которых символов больше, больше: ', sym_indep_num, 'vs.', sym_rus_num)
