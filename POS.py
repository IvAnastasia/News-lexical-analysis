pip install pymorphy2
import pymorphy2
morph = pymorphy2.MorphAnalyzer()

def get_POS(word):
    p = morph.parse('стали')[0]
    return p.tag.POS

def POS_freq_dict(text_name):
    freq_dict = {}
    with open(text_name + '.txt') as file:
        text = file.read()
        dirty_words = re.findall("\w+", text)
        for dirty_word in dirty_words:
            word = dirty_word.lower()
            words.append(word)
        for word in words:
            POS = get_POS(word)
            if POS not in freq_dict.keys():
                freq_dict[POS] = 1
            else:
                freq_dict[POS] += 1
    return freq_dict

def words_number(di):
    return sum(di.values())

#сравним по частотности разные частей речи по всем гос. новостям и по всем независимым новостям
rus_POS = POS_freq_dict('rusnews')
indep_POS = POS_freq_dict('indepnews')
for key in rus_POS.keys():
    if key in indep_POS.keys():
        print(key, ' (в абсолютных числах):', 'в гос.новостях ', rus_POS[key], ',', 'в независимых новостях ', indep_POS[key])
        print(key, ' (по доли употребления, т.е. в зависимости от объёмов текста):', 'в гос.новостях ', rus_POS[key]/words_number(rus_POS), ',', 'в независимых новостях ', indep_POS[key]/words_number(indep_POS))

#сравним по частотности разные частей речи по каждой из гос. новостей и соответствующей ей независимой новости
for n in range(1, 2):
    print('Текст №' + str(n))
    rus_POS = POS_freq_dict('rusnew' + str(n))
    indep_POS = POS_freq_dict('indepnew' + str(n))
    for key in rus_POS.keys():
        if key in indep_POS.keys():
            print(key, ' (в абсолютных числах):', 'в этой гос.новости ', rus_POS[key], ',', 'в независимой новости ',
                  indep_POS[key])
            print(key, ' (по доли употребления, т.е. в зависимости от объёмов текста):', 'в этой гос.новости ',
                  rus_POS[key] / words_number(rus_POS), ',', 'в этой независимых новости ',
                  indep_POS[key] / words_number(indep_POS))
