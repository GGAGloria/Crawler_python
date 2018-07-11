# -*- coding: utf-8 -*-
""" Created on Mon Aug 7 21:05:03 2017 @author: Administrator """

import urllib.request
from bs4 import BeautifulSoup

no = input("Plz input the no:")
''' 目标:获取酒店名称和酒店星级 '''
url = 'http://hotels.ctrip.com/hotel/'
url1 = url + str(no) + ".html"

html1 = urllib.request.urlopen(url1).read().decode('utf-8')
#print(html1)
#1.获取酒店名称信息
soup1 = BeautifulSoup(html1,"html.parser")
#print(soup1)
result1 = soup1.find_all(class_="cn_n")
#print(result1)
hotelName = result1[0].string
print("酒店名称为:{}".format(hotelName))

#2.获取酒店星级信息
soup12 = BeautifulSoup(html1,'html.parser')

result12 = soup12.find_all(attrs={"class":"grade"})

#print(result1)
result12 =str(result12)

soup13 = BeautifulSoup(result12,'html.parser')

result13 = soup13.find_all('span')
hotelStar = result13[0]['title']
print("酒店星级为:{}".format(hotelStar))



''' 目标:获取酒店卫生评分、环境评分、服务评分、设施评分、用户推荐比、用户评分、评价内容 '''
url_3 = 'http://m.ctrip.com/html5/hotel/HotelDetail/dianping/'
url3 = url_3 + str(no) + '.html'


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

print("用户推荐为:{}".format(userRecommendRate))
print("卫生评分为:{}分".format(hRating))
print("环境评分为:{}分".format(eRating))
print("服务评分为:{}分".format(sRating))
print("设施评分为:{}分".format(iRating))

#提取用户评论数据
result34 = soup3.find_all(attrs={"class":"dn hotel-t-b-border"})
result34 = str(result34[1])
soup33 = BeautifulSoup(result34,'html.parser')
result35 = soup33.find_all('p')

for i in range(0,10):
    #userName = result35[i].get_text()
    result36 = soup3.find_all(attrs={"class":"dn-checkin"})
    datePublished = result36[i].string
    print("评论发表于:{}".format(datePublished))

    result37 = soup3.find_all(attrs={"class":"g-ve"})
    userRating = result37[i].string
    print("评分为:{}".format(userRating))

    result38 = soup3.find_all(attrs={"class":"tree-ellips-line6"})
    commentText = result38[i].get_text()
    print("评论内容为:{}".format(commentText))


    