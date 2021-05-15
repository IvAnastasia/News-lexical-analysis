for n in range(1, 17):
    with open('D:\\project\\rusnew' + str(n) + '.txt', 'r', encoding='utf-8') as file1:
        text = file1.read()
        with open('D:\\project\\rusnews.txt', 'a', encoding='utf-8') as file2:
            file2.write(text)

for n in range(1, 17):
    with open('D:\\project\\indepnew' + str(n) + '.txt', 'r', encoding='utf-8') as file1:
        text = file1.read()
        with open('D:\\project\\indepnews.txt', 'a', encoding='utf-8') as file2:
            file2.write(text)
