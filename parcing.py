#$ sudo pip3 install bs4
# !/usr/bin/python3

pip install beautifulsoup4

pip install requests

import re
from bs4 import BeautifulSoup

def parce(link):
    if 'https://meduza' in link:
        return meduza(link)
    if 'novayagazeta.ru' in link:
        return novaya(link)
    if 'https://tvrain' in link:
        return rain(link)
    if 'www.rbc' in link:
        return rbc(link)
    if 'tsargrad.tv' in link:
        return tsar(link)
    if 'https://ria.' in link:
        return ria(link)
    if 'russian.rt' in link:
        return rt(link)
    if 'rg.ru' in link:
        return rg(link)


def meduza(link):
    with open(link, "r") as f:
        contents = f.read()
        soup = BeautifulSoup(contents, 'lxml')
        newstext = soup.h2.text
    return newstext

def novaya(link):
    with open(link, "r") as f:
        contents = f.read()
        soup = BeautifulSoup(contents, 'lxml')
        newstext = soup.h2.text
    return newstext

def rain(link):
    with open(link, "r") as f:
        contents = f.read()
        soup = BeautifulSoup(contents, 'lxml')
        text = soup.'script type="application/ld+json"'.text
        newstext = re.findall(r"\"headline\": \"(.+)\"", text).group(1)
        newstext = newstext + re.findall(r"\"description\": \"(.+)\"", text).group(1)
        newstext = newstext + re.findall(r"\"articleBody\": \"(.+)\"", text).group(1)
    return newstext

def rbc(link):
    with open(link, "r") as f:
        contents = f.read()
        soup = BeautifulSoup(contents, 'lxml')
        text = soup.p.text
       # newstext = re.findall(r"\"headline\": \"(.+)\"", text).group(1)
        #newstext = newstext + re.findall(r"\"description\": \"(.+)\"", text).group(1)
        #newstext = newstext + re.findall(r"\"articleBody\": \"(.+)\"", text).group(1)
    return newstext

def tsar(link):
    with open(link, "r") as f:
        contents = f.read()
        soup = BeautifulSoup(contents, 'lxml')
        text = soup.'div class="article__content"'.text
       # newstext = re.findall(r"\"headline\": \"(.+)\"", text).group(1)
        #newstext = newstext + re.findall(r"\"description\": \"(.+)\"", text).group(1)
        #newstext = newstext + re.findall(r"\"articleBody\": \"(.+)\"", text).group(1)
    return newstext

def ria(link):
    with open(link, "r") as f:
        contents = f.read()
        soup = BeautifulSoup(contents, 'lxml')
        newstext = soup.'div itemprop="articleBody"'.text
    return newstext

def rt(link):
    with open(link, "r") as f:
        contents = f.read()
        soup = BeautifulSoup(contents, 'lxml')
        newstext = soup.'div itemprop="articleBody"'.text
    return newstext

def rg(link):
    with open(link, "r") as f:
        contents = f.read()
        soup = BeautifulSoup(contents, 'lxml')
        newstext = soup.p.text
    return newstext


rus_links = [[1a, 1b, 1c], [2a, 2b, 3c, 2d]]
indep_links = []
n = 1
for li in rus_links:
    newstext = parse(link)
    with open('rusnew' + str(n) + '.txt', 'a') as file:
        for link in li:
            newstext = parse(link)
            file.write(newstext)
    with open('rusnew' + str(n) + '.txt', 'r') as file1:
        text = file1.read()
        with open('rusnews.txt', 'a') as file2:
            file2.write(text)
    for li in indep_links:
        newstext = parse(link)
        with open('indepnew' + str(n) + '.txt', 'a') as file:
            for link in li:
                newstext = parse(link)
                file.write(newstext)
        with open('indepnew' + str(n) + '.txt', 'r') as file1:
            text = file1.read()
            with open('indepnews.txt', 'a') as file2:
                file2.write(text)
