# -*- coding: utf-8 -*-
import re

reg = re.compile(r"\d+")

def numbers_freq(text):
    reg = re.compile(r"\d+")
    numbers = re.findall(reg, text)
    freq = len(numbers) / len(text.split())
    return [freq, len(numbers)]

#сравним кол-во чисел во всех гос. новостях и во всех независимых новостях
with open('rusnews.txt') as file:
    text = file.read()
    rus_freq = numbers_freq(text)[0]
    rus_numbers = numbers_freq(text)[1]
with open('indepnews.txt') as file:
    text = file.read()
    indep_freq = numbers_freq(text)[0]
    indep_numbers = numbers_freq(text)[1]

if rus_numbers > indep_numbers:
    print('В целом в гос.новостях чисел больше: ' + str(rus_numbers) + 'чисел/числа в гос.новостях vs. ' + str(indep_numbers) + 'чисел/числа в независимых новостях')
else:
    print('В целом в независимых новостях чисел больше: ' + str(indep_numbers) + ' чисел/числа в независимых новостях vs. ' + str(rus_numbers) + ' чисел/числа в гос.новостях')
if rus_freq > indep_freq:
    print('В гос.новостях числа встречаются чаще (относительно объёма текста)')
elif rus_freq < indep_freq:
    print('В независимых новостях числа встречаются чаще (относительно объёма текста)')

#сравним кол-во чисел в каждой из гос. новостей и соответствующей ей независимой новости
count_rus = 0
count_indep = 0
for n in range(1, 17):
    with open('rusnew' + str(n) +'.txt') as file:
        text = file.read()
        rus_numbers = re.findall(reg, text)
    with open('indepnew' + str(n) + '.txt') as file:
        text = file.read()
        indep_numbers = re.findall(reg, text)
    if len(rus_numbers) > len(indep_numbers):
        count_rus += 1
    elif len(rus_numbers) < len(indep_numbers):
        count_indep += 1
if count_rus > count_indep:
    print('Гос.новостей, в которых чисел больше, больше: ' + str(count_rus) + ' vs. ' + str(count_indep))
if count_indep > count_rus:
    print('Независимых новостей, в которых чисел больше, больше: ' + str(count_indep) + ' vs. ' + str(count_rus))
