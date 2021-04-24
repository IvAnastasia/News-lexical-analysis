#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# среднее количество предложений в тексте
def mean_sentence_texts(texts: list):
    sum_sentences_number = 0
    for text in texts:
        sentences = re.split(r'[.?!]', text)
        sum_sentences_number += len(sentences)
    return sum_sentences_number / len(texts)

