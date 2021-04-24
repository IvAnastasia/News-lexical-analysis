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

