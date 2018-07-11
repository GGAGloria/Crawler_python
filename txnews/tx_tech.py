import requests
from bs4 import BeautifulSoup
import re
import pandas as pd


headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
}
url = "http://tech.qq.com"
subject = "tech"
result=requests.get(url,headers=headers,timeout=2)
print (result.status_code)
content=result.content
soup=BeautifulSoup(content,fromEncoding=result.encoding)
def has_no_string(tag):
    return tag.name=='a' and tag.string!=None

samples=soup.find('div','list first').find_all(has_no_string,target='_blank',href=re.compile('tech\.qq\.com'))

news_titles = []
news_urls = []

for sample in samples:
    title=sample.text.strip()
    url=sample['href']

    news_titles.append(title)
    news_urls.append(url)

news_dic={'title':news_titles,'url':news_urls}
news_df=pd.DataFrame(news_dic)
news_df.to_excel(subject+'.xlsx', sheet_name = 'testing', index = False)
print ("finished")

def getHTMLText(url):
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status()
        #r.encoding = 'utf-8'
        return r.text
    except:
        return ""

def getContent(url, i):
    html = getHTMLText(url)
    # print(html)
    soup = BeautifulSoup(html, "html.parser")
    title = soup.select("div.hd > h1")
    print(title[0].get_text())
    time = soup.select("div.a_Info > span.a_time")
    print(time[0].string)
    author = soup.select("div.qq_articleFt > div.qq_toolWrap > div.qq_editor")
    print(author[0].get_text())
    paras = soup.select("div.Cnt-Main-Article-QQ > p.text")
    for para in paras:
        if len(para) > 0:
            print(para.get_text())
            print()
    fo = open("txnews/"+str(i)+".txt", "w+")
    fo.writelines(title[0].get_text() + "\n")
    fo.writelines(time[0].get_text() + "\n")
    for para in paras:
        if len(para) > 0:
            fo.writelines(para.get_text() + "\n\n")
    fo.writelines(author[0].get_text() + '\n')
    fo.close()
    fo = open("txnews/"+str(i)+".txt", "w+")
    fo.writelines(title[0].get_text() + "\n")
    fo.writelines(time[0].get_text() + "\n")
    for para in paras:
        if len(para) > 0:
            fo.writelines(para.get_text() + "\n\n")
    fo.writelines(author[0].get_text() + '\n')
    fo.close()

i=int(input("index: "))

for url in news_df['url']:
    getContent(url, i)
    i = i+1


