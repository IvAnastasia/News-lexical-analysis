#!/usr/bin/env python
# coding: utf-8

# In[ ]:


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
count_words(text, words)

