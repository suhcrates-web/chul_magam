from bs4 import BeautifulSoup
import os, glob, json, requests
import time, re

def get_dict():
   url = 'https://news.mt.co.kr/newsflash/newsflash.html?sec=invest&pDepth=1&page=1&listType=left'
   # url ="https://search.mt.co.kr?kwd"
   req = requests.get(url)
   be_0 = BeautifulSoup(req.text, 'html.parser')
   # print(be_0)
   be_0 = be_0.find('div', {'id':'articleList'})

   be_0 =be_0.find_all('li')
   ar_dict = {}
   n=0
   for i in be_0:
      ar_dict[n]={}
      ar_dict[n]['title'] =i.a.text

      inhref = i.a['href']
      id = re.findall(r'\d\d\d\d\d\d+',inhref)[0]
      day = id[:8]
      ar_dict[n]['id']= id
      ar_dict[n]['day']= day
      ar_dict[n]['time'] = i.span.text

      n+=1

   return ar_dict



ar_dict = get_dict()
hwan_up = False
for i in [*ar_dict][:10]:
   title = ar_dict[i]['title']
   if bool(re.search('원/달러', title)):
      id =ar_dict[i]['id']
      hwan_up = True
      break
print(id)
#2021021009020234079
if hwan_up:
   art_url = 'https://news.mt.co.kr/mtview.php?no=' +id
   art_req = requests.get(art_url)
   art_be = BeautifulSoup(art_req.text, 'html.parser')
   art_title = art_be.title.text
   #코스피, 3.46p(0.11%) 오른 3088.13, 원/달러 환율 5.6원 내린 1111.0원 출발 - 머니투데이

   print(art_title)




