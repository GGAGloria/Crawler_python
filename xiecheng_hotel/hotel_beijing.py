#coding: utf-8

import urllib
from urllib import request, parse
from bs4 import BeautifulSoup


def getReviews(index):
    url = 'http://hotels.ctrip.com/hotel/'
    url1 = url + str(index) + ".html"
    html1 = urllib.request.urlopen(url1).read().decode('utf-8')
    #print(html1)
    #1.获取酒店名称信息
    soup1 = BeautifulSoup(html1,"html.parser")
    #print(soup1)
    result1 = soup1.find_all(class_="cn_n")
    #print(result1)
    hotelName = result1[0].string
    f.write("酒店名称为:{}".format(hotelName)+"\n")

    #2.获取酒店星级信息
    soup12 = BeautifulSoup(html1,'html.parser')

    result12 = soup12.find_all(attrs={"class":"grade"})

    #print(result1)
    result12 =str(result12)

    soup13 = BeautifulSoup(result12,'html.parser')



    ''' 目标:获取酒店卫生评分、环境评分、服务评分、设施评分、用户推荐比、用户评分、评价内容 '''
    url_3 = 'http://m.ctrip.com/html5/hotel/HotelDetail/dianping/'
    url3 = url_3 + str(index) + '.html'


    html3 = urllib.request.urlopen(url3).read().decode('utf-8')

    soup3 = BeautifulSoup(html3,'lxml')

    #获取酒店各项评分数据
    result32 = soup3.find_all(attrs={"class":"ve-txt"})
    result32 = str(result32)
    soup32 = BeautifulSoup(result32,'lxml')

    result33 = soup32.find_all('em')
    userRecommendRate = result33[0].string
    hRating = result33[1].string
    eRating = result33[2].string
    sRating = result33[3].string
    iRating = result33[4].string

    f.write("用户推荐为:{}".format(userRecommendRate)+"\n")
    f.write("卫生评分为:{}分".format(hRating)+"\n")
    f.write("环境评分为:{}分".format(eRating)+"\n")
    f.write("服务评分为:{}分".format(sRating)+"\n")
    f.write("设施评分为:{}分".format(iRating)+"\n")

    #提取用户评论数据
    result34 = soup3.find_all(attrs={"class":"dn hotel-t-b-border"})
    result34 = str(result34[1])
    soup33 = BeautifulSoup(result34,'html.parser')
    result35 = soup33.find_all('p')

    for i in range(0,10):
        #userName = result35[i].get_text()
        result36 = soup3.find_all(attrs={"class":"dn-checkin"})
        datePublished = result36[i].string
        f.write("评论发表于:{}".format(datePublished)+"\n")

        result37 = soup3.find_all(attrs={"class":"g-ve"})
        userRating = result37[i].string
        f.write("评分为:{}".format(userRating)+"\n")

        result38 = soup3.find_all(attrs={"class":"tree-ellips-line6"})
        commentText = result38[i].get_text()
        f.write("评论内容为:{}".format(commentText)+"\n")

def findIndex(url):
    global count
    print(url)
    html = request.urlopen(url).read().decode('utf-8', 'ignore')
    soup = BeautifulSoup(html, 'html.parser')
    for i in soup.find_all(attrs={"class":"hotel_new_list"}):
        index = i.get("id")
        getReviews(index)
        count=count+1
        print(count)

count=0
f = open('hotel_beijing.txt', 'a+', encoding='utf-8')
for i in range(1,100):
    findIndex('http://hotels.ctrip.com/hotel/beijing1/p'+str(i))
print(count)
