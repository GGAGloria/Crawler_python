#coding: utf-8

import urllib
from urllib import request, parse
from bs4 import BeautifulSoup
import time
import re


def getNews(url):
    global count
    html = request.urlopen(url).read().decode('utf-8', 'ignore')
    #解析
    soup = BeautifulSoup(html, 'html.parser')
    title  = soup.title.name
    main_content = soup.find('div', {'class': 'article'})
    content = ''
    
    for p in main_content.select('p'):
        content = content + p.get_text()

    if (title and content):
        count=count+1
        today = time.strftime("%F")
        f=open('xinlang_news_'+ today + '_' + str(count) + '.txt', 'a+', encoding='utf-8')
        f.write("Topic: "+ title +'\t'+ content +'\n\n')
        #print(count)


def findURL(url):
    global count
    html = request.urlopen(url).read().decode('utf-8', 'ignore')
    soup = BeautifulSoup(html, 'html.parser')
    f.write(str(soup))
    for links in soup.find_all(attrs={"class":"c_tit"}):
        for link in links.find_all('a'):
            url = link.get('href')
            getNews(url)
            
f = open("soup.txt", "a+", encoding='utf-8')
count=int(input("index: "))
findURL('http://api.roll.news.sina.com.cn')
