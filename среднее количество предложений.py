import re

# среднее количество предложений в текстах
def mean_sentence_number(text):
    sentences = re.split(r'[.?!]|$', text)
    return len(sentences)

rus_sum = 0
indep_sum = 0
for n in range(1, 5):
    with open('rusnew' + str(n) + '.txt', encoding = 'utf-8') as file:
        text = file.read()
        rus_sum += mean_sentence_number(text)
    with open('indepnew' + str(n) + '.txt', encoding = 'utf-8') as file:
        text = file.read()
        indep_sum += mean_sentence_number(text)

rus = rus_sum/4
indep = indep_sum/4

if rus > indep:
    print('В гос. новостях в среднем предложений больше.')
elif indep > rus:
    print('В независимых новостях в среднем предложений больше.')
