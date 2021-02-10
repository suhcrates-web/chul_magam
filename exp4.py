import requests, re, time
from bs4 import BeautifulSoup


def yon_data():
    url ='https://www.yna.co.kr/economy/all/3'

    req = requests.get(url)
    be_0 = BeautifulSoup(req.text, 'html.parser')
    li_list = be_0.find('div', {'class':'section01'}).find_all('li')

    yon_up = False
    n=0
    while yon_up == False:
        for i in li_list:
            try:
                tit_0 = i.strong.text
                if bool(re.search('\[외환\]',tit_0)) and bool(re.search('원/달러',tit_0)) :
                    tit = tit_0.replace(',','')
                    yon_up = True
                    break  #for

            except : ##중간에 광고 li 도 있어서.
                pass

        if yon_up:
            break #while
        else:
            time.sleep(5)
            n +=1
            print('연합 대기중 '+str(n))

    if bool(re.search('내린|오른', tit)):
        front = re.sub(r'[내린|오른].+','',tit)
        back = re.sub(r'.+[내린|오른]','',tit)
        point = re.findall(r'\d+\.?\d*?원',front)[0].replace('원','')
        num = re.findall(r'\d+\.?\d*?원', back)[0].replace('원','')
        plma_ment = re.findall('내린|오른',tit)[0]
        if plma_ment == '오른':
            plma = True
        elif plma_ment == '내린':
            plma = False

    return {'name': '원/달러', 'num': num, 'plma': plma, 'plma_ment': plma_ment, 'point': point, 'rate': '0'}