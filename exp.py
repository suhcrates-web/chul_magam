#coding=utf-8
# from make_dict import make_dict
import json, math
from datetime import date, timedelta
import datetime

# jisu_dict_s =  make_dict()

jisu_dict_s = """{'KOSPI': {'name': 'KOSPI', 'num': '3096.81', 'plma': True, 'plma_ment': '오른', 'point': '40.28', 
'rate': '1.32'}, 'KOSPI200': {'name': 'KOSPI200', 'num': '421.03', 'plma': True, 'plma_ment': '오른', 'point': '5.58', 'rate': '1.34'}, 'KOSDAQ': {'name': 'KOSDAQ', 'num': '963.81', 'plma': True, 'plma_ment': '오른', 'point': '6.89', 'rate': '0.72'}, 'KOSDAQ150': {'name': 'KOSDAQ150', 'num': '1488.69', 'plma': True, 'plma_ment': '오른', 'point': '0.15', 'rate': '0.01'}, '선물(F202103)': {'name': '선물(F202103)', 'num': '422.10', 'plma': True, 'plma_ment': '오른', 'point': '6.80', 'rate': '1.64'}, '다우': {'name': '다우', 'num': '422.10', 'plma': None, 'plma_ment': '오른', 'point': '30,211.91▲', 'rate': '229.29'}, '나스닥': {'name': '나스닥', 'num': '422.10', 'plma': None, 'plma_ment': '오른', 'point': '13,403.39▲', 'rate': '332.69'}, 'S&P500': {'name': 'S&P500', 'num': '422.10', 'plma': None, 'plma_ment': '오른', 'point': '3,773.86▲', 'rate': '59.62'}, '상해종합': {'name': '상해종합', 'num': '422.10', 'plma': None, 'plma_ment': '오른', 'point': '3,533.69▲', 'rate': '28.40'}, '유로스톡': {'name': '유로스톡', 'num': '422.10', 'plma': None, 'plma_ment': '오른', 'point': '3,530.85▲', 'rate': '49.41'}, '니케이225': {'name': '니케이225', 'num': '422.10', 'plma': None, 'plma_ment': '오른', 'point': '28,362.17▲', 'rate': '271.12'}, '홍콩항셍': {'name': '홍콩항셍', 'num': '422.10', 'plma': None, 'plma_ment': '오른', 'point': '29,217.10▲', 'rate': '324.24'}, '국고채3년': {'name': '국고채3년', 'num': '0.98', 'plma': False, 'plma_ment': '내린', 'point': '0.01', 'rate': '1.01'}, '회사채3년': {'name': '회사채3년', 'num': '2.06', 'plma': False, 'plma_ment': '내린', 'point': '0.02', 'rate': '0.96'}, 'CD(91일)': {'name': 'CD(91일)', 'num': '0.73', 'plma': True, 'plma_ment': '오른', 'point': '0.03', 'rate': '4.29'}, '원/달러': {'name': '원/달러', 'num': '1117.70', 'plma': True, 'plma_ment': '오른', 'point': '1.20', 'rate': '0.11'}, '엔/달러': {'name': '엔/달러', 'num': '104.97', 'plma': True, 'plma_ment': '오른', 'point': '0.29', 'rate': '0.28'}, '유가(WTI)근월': {'name': '유가(WTI)근월', 'num': '53.55', 'plma': True, 'plma_ment': '오른', 'point': '1.35', 'rate': '2.59'}, '고객예탁금': {'name': '고객예탁금', 'num': '680172', 'plma': False, 'plma_ment': '내린', 'point': '3,118', 'rate': '0.46'}, '선물예수금': {'name': '선물예수금', 'num': '129372', 'plma': False, 'plma_ment': '내린', 'point': '641', 'rate': '0.49'}, '미수금잔고': {'name': '미수금잔고', 'num': '3899', 'plma': False, 'plma_ment': '내린', 'point': '59', 'rate': '1.48'}, '신용잔고': {'name': '신용잔고', 'num': '210139', 'plma': False, 'plma_ment': '내린', 'point': '2,306', 'rate': '1.09'}}"""



jisu_dict_s = jisu_dict_s.replace('\'','\"').replace('True','"True"').replace('False','"False"').replace('None','"None"')
# jisu_dict_s = jisu_dict_s.replace('\'','\"').replace('True','true').replace('False','false').replace('None','')
jisu_dict_s = json.loads(jisu_dict_s)
# print(jisu_dict_s)

chul_ma = True

def second_bo(jisu_dict_s=None, chul_ma = None):

    today = date.today().day
    yesterday = (date.today() - timedelta(days=1)).day
    now_0 = str(datetime.datetime.now().hour) +'시' + str(datetime.datetime.now().minute) +'분'
    g = {} #글로벌
    ##
    n = {
        'kp':'KOSPI',
        'kd':'KOSDAQ',
        'ex':'원/달러'
    }
    for i in ['kp','kd','ex']:
        ind = n[i]
        temp = jisu_dict_s[ind]['point'] # 코스피 변동폭
        g[i+'_point'] = str(float(temp))
        temp = float(jisu_dict_s[ind]['num']) #코스피 얼마
        g[i+'_sun'] = math.floor(temp/10)*10
        g[i+'_num'] = str(temp)
        g[i+'_plma'] = jisu_dict_s[ind]['plma'] #증감여부

        g[i+'_plma_ment'] = jisu_dict_s[ind]['plma_ment']
        g[i+'_rate'] = float(jisu_dict_s[ind]['rate']) #변동폭
        #
        if g[i+'_rate'] < 0.5 :
            g[i+'_how'] = '소폭 '
            g[i+'_how2'] = ''
        elif g[i+'_rate'] <2:
            g[i+'_how'] = ''
            g[i+'_how2'] = ''
        elif g[i+'_rate'] >2:
            g[i+'_how'] = '대폭 '
            g[i+'_how2'] = '급격히 '
        #
        if g[i+'_plma']:
            g[i+'_ment_sang'] = '상승'
            g[i+'_ment_se'] = '오름세'
            g[i+'_ment_jin'] = '높아진'
            g[i+'_arr'] = '↑'
        elif not g[i+'_plma']:
            g[i+'_ment_sang'] = '하락'
            g[i+'_ment_se'] = '내림세'
            g[i+'_ment_jin'] = '떨어진'
            g[i+'_arr'] = '↓'

    ks_kd = '는' #코스피 코스닥 같으면 '도'
    if g['kp_plma'] == g['kd_plma']:
        ks_kd = '도'
    if chul_ma: #출발

        title = f"""코스피, 장초반 {g['kp_how']}{g['kp_ment_sang']} {g['kp_sun']}선...코스닥 {g['kd_rate']}%{g['kd_arr']}(2보)"""
        article = f"""{today}일 장초반 코스피 지수는 {g['kp_how']}{g['kp_plma_ment']} {g['kp_sun']}선을 가리키고 있다. 코스닥{ks_kd}
{g['kd_ment_se']}다. <br><br>이날 오전 {now_0} 기준 코스피는 전날 종가와 비교해 {g['kp_point']}포인트(p)({g['kp_rate']}%) {g['kp_plma_ment']}
{g['kp_num']}를 기록 중이다.<br><br>코스닥은 전날보다 {g['kd_point']}p({g['kd_rate']}%) {g['kd_ment_jin']} {g['kd_num']}를 가리키고 있다.<br><br>서울외환시장에서 달러/원 환율은 전날 대비 {g['ex_point']}원 {g['ex_plma_ment']} {g['ex_num']}원으로 거래를 시작했다."""
    elif not chul_ma: #마감
        title = f"""코스피 {g['kp_rate']}% {g['kp_how']}{g['kp_ment_sang']} {g['kp_sun']}선...코스닥 {g['kd_rate']}%{g['kd_arr']}(2보)"""
        article = f"""{today}일 코스피 지수가 {g['kd_rate']}% {g['kp_how']}{g['kp_ment_sang']}해 {g['kp_sun']}선으로 마감했다. 코스닥
{ks_kd} {g['kd_ment_se']}였다. <br><br>이날 코스피 지수는 {g['kp_point']}포인트(p)({g['kp_rate']}%) {g['kp_plma_ment']} 
{g['kp_num']}로 거래를 마쳤다.<br><br>코스닥 지수는 {g['kd_point']}p({g['kd_rate']}%) {g['kd_plma_ment']}{g['kd_num']}로 
마감했다.<br><br>달러/원 환율은 {g['ex_point']}원 {g['ex_plma_ment']} {g['ex_num']}원을 기록했다."""
    return {'title':title, 'article':article}
        # title = f"""코스피 {}% {} {}선...코스닥 {}%{}"""
        # article = f""" """
fuck =second_bo(jisu_dict_s, False)
print(fuck['title'])
print(fuck['article'])

# def dol_won(jisu_dict_s=None, pi_daq = None, chul_ma = None):
#     today = date.today().day
#     name_h = '달러/원'  #한글이름
#     name = '원/달러'
#     point = jisu_dict_s[name]['point'] # 원
#     point = str(float(point))
#     num = jisu_dict_s[name]['num']
#     num = str(float(num))
#     plma_ment = jisu_dict_s[name]['plma_ment']
#     st_en = '마감'
#     title = f"""[{name_h}] 환율 {point}원 {plma_ment} {num}원 {st_en} """
#     article = f"""{today}일 {name_h}"""
#
#     return {'title':title, 'article':article}


# def kos_pi_daq(jisu_dict_s=None, pi_daq = None, chul_ma = None):
#     today = date.today().day
#     name_h = '코스피'  #한글이름
#     name = 'KOSPI'
#     point = jisu_dict_s[name]['point']
#     num = jisu_dict_s[name]['num']
#     rate = jisu_dict_s[name]['rate']
#     plma_ment = jisu_dict_s[name]['plma_ment']
#     st_en = '마감'
#     title = f"""[{name_h}] {point}p({rate}%) {plma_ment} {num} {st_en} """
#     article = f"""{today}일 {name_h} {st_en}"""
#
#     return {'title':title, 'article':article}
