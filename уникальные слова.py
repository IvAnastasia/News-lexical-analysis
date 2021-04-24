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

