#coding=utf-8
###자료수집 ####

from datetime import date, timedelta

from bs4 import BeautifulSoup
import os, glob, json, requests
import time, re



# def magam_check(): 이건 안됨. '종료' 플래그가 너무 늦게 뜸
#     url = 'https://www.kiwoom.com/nkw.HeroFrontJisu3.do'
#     req = requests.post(url)
#     be_0 = BeautifulSoup(req.text, 'html.parser')
#     day = be_0.find('span').text.replace(' ','')
#     magam_ready =False
#     if bool(re.search('종료', day)):
#         magam_ready = True
#     return {"magam_ready" : magam_ready, 'be_0':be_0}

def magam_check():

    def get_bs():
        url = 'https://www.kiwoom.com/nkw.HeroFrontJisu3.do'
        req = requests.post(url)
        be_0 = BeautifulSoup(req.text, 'html.parser')
        be = be_0.find_all('li')
        list = []
        for i in be[:4]:
            list.append(i.text.replace(' ',''))
        return {'list':list, 'be_0':be_0}

    same = False
    old_list = [0,0,0,0]
    while same ==False:
        bs = get_bs()
        new_list= bs['list']
        for i in range(0,4):
            if old_list[i] != new_list[i]:
                old_list = new_list
                time.sleep(30)
                break
            else:
                same = True
    return {"magam_ready" : True, 'be_0': bs['be_0']}



if __name__ == '__main__':
    print(magam_check())


def make_dict(be_0 = 'None'):
    if be_0 =='None':
        url = 'https://www.kiwoom.com/nkw.HeroFrontJisu3.do'
        req = requests.post(url)
        be_0 = BeautifulSoup(req.text, 'html.parser')
        # print(be_0)

    be = be_0.find_all('li')
    jisu_dict_s= {}
    for i in be:
        plma = None
        jisu_dict = {}
        jisu = i.get_text(separator='|').split('|')

        #이름 구간
        name = jisu[0].replace(' ','')
        jisu_dict['name'] = name

        #지수구간
        num_0 = jisu[1]
        if bool(re.search('▲',num_0)):
            plma = True
            plma_ment ='오른'
            num= num_0.replace(',','').replace('▲','').replace(' ','')

        elif bool(re.search('▼', num_0)):
            plma = False
            plma_ment = '내린'
            num= num_0.replace(',','').replace('▼','').replace(' ','')
        jisu_dict['num'] = num
        jisu_dict['plma'] = plma
        jisu_dict['plma_ment'] = plma_ment

        #포인트 구간
        point = jisu[2].replace(' ','')
        jisu_dict['point'] = point


        #증감율 구간
        rate = jisu[3].replace('%','').replace(' ','')
        jisu_dict['rate'] = rate


        jisu_dict_s[name] =jisu_dict
    return {'jisu_dict_s':jisu_dict_s}

def yon_data():
    url ='https://www.yna.co.kr/economy/all/1'

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
            time.sleep(10)
            n +=1
            print('연합 아직 안뜸. 대기중 '+str(n))

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


# """
# {'KOSPI': {'name': 'KOSPI', 'num': '3096.81', 'plma': True, 'plma_ment': '오른', 'point': '40.28', 'rate': '1.32'}, 'KOSPI200': {'name': 'KOSPI200', 'num': '421.03', 'plma': True, 'plma_ment': '오른', 'point': '5.58', 'rate': '1.34'}, 'KOSDAQ': {'name': 'KOSDAQ', 'num': '963.81', 'plma': True, 'plma_ment': '오른', 'point': '6.89', 'rate': '0.72'}, 'KOSDAQ150': {'name': 'KOSDAQ150', 'num': '1488.69', 'plma': True, 'plma_ment': '오른', 'point': '0.15', 'rate': '0.01'}, '선물(F202103)': {'name': '선물(F202103)', 'num': '422.10', 'plma': True, 'plma_ment': '오른', 'point': '6.80', 'rate': '1.64'}, '다우': {'name': '다우', 'num': '422.10', 'plma': None, 'plma_ment': '오른', 'point': '30,211.91▲', 'rate': '229.29'}, '나스닥': {'name': '나스닥', 'num': '422.10', 'plma': None, 'plma_ment': '오른', 'point': '13,403.39▲', 'rate': '332.69'}, 'S&P500': {'name': 'S&P500', 'num': '422.10', 'plma': None, 'plma_ment': '오른', 'point': '3,773.86▲', 'rate': '59.62'}, '상해종합': {'name': '상해종합', 'num': '422.10', 'plma': None, 'plma_ment': '오른', 'point': '3,533.69▲', 'rate': '28.40'}, '유로스톡': {'name': '유로스톡', 'num': '422.10', 'plma': None, 'plma_ment': '오른', 'point': '3,530.85▲', 'rate': '49.41'}, '니케이225': {'name': '니케이225', 'num': '422.10', 'plma': None, 'plma_ment': '오른', 'point': '28,362.17▲', 'rate': '271.12'}, '홍콩항셍': {'name': '홍콩항셍', 'num': '422.10', 'plma': None, 'plma_ment': '오른', 'point': '29,217.10▲', 'rate': '324.24'}, '국고채3년': {'name': '국고채3년', 'num': '0.98', 'plma': False, 'plma_ment': '내린', 'point': '0.01', 'rate': '1.01'}, '회사채3년': {'name': '회사채3년', 'num': '2.06', 'plma': False, 'plma_ment': '내린', 'point': '0.02', 'rate': '0.96'}, 'CD(91일)': {'name': 'CD(91일)', 'num': '0.73', 'plma': True, 'plma_ment': '오른', 'point': '0.03', 'rate': '4.29'}, '원/달러': {'name': '원/달러', 'num': '1117.70', 'plma': True, 'plma_ment': '오른', 'point': '1.20', 'rate': '0.11'}, '엔/달러': {'name': '엔/달러', 'num': '104.97', 'plma': True, 'plma_ment': '오른', 'point': '0.29', 'rate': '0.28'}, '유가(WTI)근월': {'name': '유가(WTI)근월', 'num': '53.55', 'plma': True, 'plma_ment': '오른', 'point': '1.35', 'rate': '2.59'}, '고객예탁금': {'name': '고객예탁금', 'num': '680172', 'plma': False, 'plma_ment': '내린', 'point': '3,118', 'rate': '0.46'}, '선물예수금': {'name': '선물예수금', 'num': '129372', 'plma': False, 'plma_ment': '내린', 'point': '641', 'rate': '0.49'}, '미수금잔고': {'name': '미수금잔고', 'num': '3899', 'plma': False, 'plma_ment': '내린', 'point': '59', 'rate': '1.48'}, '신용잔고': {'name': '신용잔고', 'num': '210139', 'plma': False, 'plma_ment': '내린', 'point': '2,306', 'rate': '1.09'}}
#
#
# """