#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# процент уникальных слов в тексте
import string
import pymorphy2


def unique_words_percent(text: str):
    morph = pymorphy2.MorphAnalyzer()
    
# избавились от пунктуации
    for c in string.punctuation:
        text = text.replace(c, "")
    
    all_words = text.split()
    unique_words = set()
    for word in all_words:
        word_normal_form = morph.parse(word)[0].normal_form
        if word_normal_form not in unique_words:
            unique_words.add(word_normal_form)
     # процент уникальных слов       
    return len(unique_words) / len(all_words) * 100

#сравним по всем новостям сразу
with open('rusnews.txt', encoding='utf-8') as file:
    text = file.read()
    print('Процент уникальных слов в гос. новостях: ', unique_words_percent(text))
with open('indepnews.txt', encoding='utf-8') as file:
    text = file.read()
    print('Процент уникальных слов в независимых новостях: ', unique_words_percent(text))

#сравним по каждой новости отдельно
rus = 0
indep = 0
for n in range(1, 2):
    print('Текст №' + str(n))
    with open('rusnew' + str(n) + '.txt', encoding='utf-8') as file:
        text = file.read()
        rus_uniq = unique_words_percent(text)
        print('Процент уникальных слов в этой гос. новости: ', rus_uniq)
    with open('indepnew' + str(n) +'.txt', encoding='utf-8') as file:
        text = file.read()
        indep_uniq = unique_words_percent(text)
        print('Процент уникальных слов в этой независимой новости: ', indep_uniq)
    if rus_uniq > indep_uniq:
        rus += 1
    else:
        indep += 1
if rus > indep:
    print('В целом гос. новостей, в которых уникальных слов больше, больше: ', rus, 'vs.', indep)
elif rus < indep:
    print('В целом независимых новостей, в которых уникальных слов больше, больше: ', indep, 'vs.', rus)
