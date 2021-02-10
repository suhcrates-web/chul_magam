import re
art_title = '코스피, 3.46p(0.11%) 오른 3088.13, 원/달러 환율 5.1원 내린 1111.0원 출발 - 머니투데이'


tit =  re.sub(r'.*원/달러','',art_title)
print(tit)
#내린, 오른 을 기점으로 좌 우 구분.
if bool(re.search('내린|오른', tit)):
    front = re.sub(r'[내린|오른].+','',tit)
    back = re.sub(r'.+[내린|오른]','',tit)
    point = re.findall(r'\d+\.?\d*?원',front)[0].replace('원','')
    num = re.findall(r'\d+\.?\d*?원', back)[0].replace('원','')
    plma_ment = re.findall('내린|오른',tit)[0]
    cnul_ma = re.findall('출발|마감',tit)[0]


    print(plma_ment)

