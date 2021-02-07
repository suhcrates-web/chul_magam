#coding=utf-8
###자료수집 ####

from datetime import date, timedelta

from bs4 import BeautifulSoup
import os, glob, json, requests
import time, re

def make_dict():
    url = 'https://www.kiwoom.com/nkw.HeroFrontJisu3.do'
    req = requests.post(url)
    be_0 = BeautifulSoup(req.text, 'html.parser')
    day = be_0.find('span').text.replace(' ','')
    magam_ready =False
    if bool(re.search('종료', day)):
        magam_ready = True
    print(day+str(magam_ready))


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
    return {'jisu_dict_s':jisu_dict_s, 'magam_ready':magam_ready}

print(make_dict())

# """
# {'KOSPI': {'name': 'KOSPI', 'num': '3096.81', 'plma': True, 'plma_ment': '오른', 'point': '40.28', 'rate': '1.32'}, 'KOSPI200': {'name': 'KOSPI200', 'num': '421.03', 'plma': True, 'plma_ment': '오른', 'point': '5.58', 'rate': '1.34'}, 'KOSDAQ': {'name': 'KOSDAQ', 'num': '963.81', 'plma': True, 'plma_ment': '오른', 'point': '6.89', 'rate': '0.72'}, 'KOSDAQ150': {'name': 'KOSDAQ150', 'num': '1488.69', 'plma': True, 'plma_ment': '오른', 'point': '0.15', 'rate': '0.01'}, '선물(F202103)': {'name': '선물(F202103)', 'num': '422.10', 'plma': True, 'plma_ment': '오른', 'point': '6.80', 'rate': '1.64'}, '다우': {'name': '다우', 'num': '422.10', 'plma': None, 'plma_ment': '오른', 'point': '30,211.91▲', 'rate': '229.29'}, '나스닥': {'name': '나스닥', 'num': '422.10', 'plma': None, 'plma_ment': '오른', 'point': '13,403.39▲', 'rate': '332.69'}, 'S&P500': {'name': 'S&P500', 'num': '422.10', 'plma': None, 'plma_ment': '오른', 'point': '3,773.86▲', 'rate': '59.62'}, '상해종합': {'name': '상해종합', 'num': '422.10', 'plma': None, 'plma_ment': '오른', 'point': '3,533.69▲', 'rate': '28.40'}, '유로스톡': {'name': '유로스톡', 'num': '422.10', 'plma': None, 'plma_ment': '오른', 'point': '3,530.85▲', 'rate': '49.41'}, '니케이225': {'name': '니케이225', 'num': '422.10', 'plma': None, 'plma_ment': '오른', 'point': '28,362.17▲', 'rate': '271.12'}, '홍콩항셍': {'name': '홍콩항셍', 'num': '422.10', 'plma': None, 'plma_ment': '오른', 'point': '29,217.10▲', 'rate': '324.24'}, '국고채3년': {'name': '국고채3년', 'num': '0.98', 'plma': False, 'plma_ment': '내린', 'point': '0.01', 'rate': '1.01'}, '회사채3년': {'name': '회사채3년', 'num': '2.06', 'plma': False, 'plma_ment': '내린', 'point': '0.02', 'rate': '0.96'}, 'CD(91일)': {'name': 'CD(91일)', 'num': '0.73', 'plma': True, 'plma_ment': '오른', 'point': '0.03', 'rate': '4.29'}, '원/달러': {'name': '원/달러', 'num': '1117.70', 'plma': True, 'plma_ment': '오른', 'point': '1.20', 'rate': '0.11'}, '엔/달러': {'name': '엔/달러', 'num': '104.97', 'plma': True, 'plma_ment': '오른', 'point': '0.29', 'rate': '0.28'}, '유가(WTI)근월': {'name': '유가(WTI)근월', 'num': '53.55', 'plma': True, 'plma_ment': '오른', 'point': '1.35', 'rate': '2.59'}, '고객예탁금': {'name': '고객예탁금', 'num': '680172', 'plma': False, 'plma_ment': '내린', 'point': '3,118', 'rate': '0.46'}, '선물예수금': {'name': '선물예수금', 'num': '129372', 'plma': False, 'plma_ment': '내린', 'point': '641', 'rate': '0.49'}, '미수금잔고': {'name': '미수금잔고', 'num': '3899', 'plma': False, 'plma_ment': '내린', 'point': '59', 'rate': '1.48'}, '신용잔고': {'name': '신용잔고', 'num': '210139', 'plma': False, 'plma_ment': '내린', 'point': '2,306', 'rate': '1.09'}}
#
#
# """