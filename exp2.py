from bs4 import BeautifulSoup
import re

be = """
<div class="index-jisoo-box">
<div class="jisoo-top first">
<h3><img alt="국내지수" src="/kwa/images/hero/title_hero03.png"/></h3>
<div class="jisoo-top-date">
<a href="#none" onclick="javascript:goJisu();setTimeout(function() {try {goMainJisu();} catch(e) {}	},500);"><img alt="새로고침" src="/kwa/images/hero/btn_refresh.png"/></a>
<span>02월 02일 </span>
</div>
</div>
<div class="jisoo-list">
<ul>
<li class="red"><em>KOSPI</em><span class="first">3,096.81 ▲ </span><span class="second">40.28</span><span class="third">1.32%</span></li>
<li class="red"><em>KOSPI200</em><span class="first">421.03 ▲ </span><span class="second">5.58</span><span class="third">1.34%</span></li>
<li class="red"><em>KOSDAQ</em><span class="first">963.81 ▲ </span><span class="second">6.89</span><span class="third">0.72%</span></li>
<li class="red"><em>KOSDAQ150</em><span class="first">1,488.69 ▲ </span><span class="second">0.15</span><span class="third">0.01%</span></li>
<li class="red"><em>선물(F 202103)</em><span class="first">421.75 ▲ </span><span class="second">6.45</span><span class="third">1.55%</span></li>
</ul>
</div>
</div>
<div class="index-jisoo-box jisoo-index1">
<div class="jisoo-top">
<h3><img alt="해외지수" src="/kwa/images/hero/title_hero04.png"/></h3>
</div>
<div class="jisoo-list">
<ul>
<li class="red"><em>다우<u style="font-size: 11px; float: right; margin-right:10px; display: inline; font-style: normal; letter-spacing: -.1em;">02/01</u></em><span class="first">30,211.91 ▲ </span><span class="second">229.29</span><span class="third">0.76%</span></li>
<li class="red"><em>나스닥<u style="font-size: 11px; float: right; margin-right:10px; display: inline; font-style: normal; letter-spacing: -.1em;">02/01</u></em><span class="first">13,403.39 ▲ </span><span class="second">332.69</span><span class="third">2.55%</span></li>
<li class="red"><em>S&amp;P500<u style="font-size: 11px; float: right; margin-right:10px; display: inline; font-style: normal; letter-spacing: -.1em;">02/01</u></em><span class="first">3,773.86 ▲ </span><span class="second">59.62</span><span class="third">1.61%</span></li>
<li class="red"><em>상해종합<u style="font-size: 11px; float: right; margin-right:10px; display: inline; font-style: normal; letter-spacing: -.1em;">02/02</u></em><span class="first">3,532.10 ▲ </span><span class="second">26.81</span><span class="third">0.76%</span></li>
<li class="red"><em>유로스톡<u style="font-size: 11px; float: right; margin-right:10px; display: inline; font-style: normal; letter-spacing: -.1em;">02/01</u></em><span class="first">3,530.85 ▲ </span><span class="second">49.41</span><span class="third">1.42%</span></li>
<li class="red"><em>니케이225<u style="font-size: 11px; float: right; margin-right:10px; display: inline; font-style: normal; letter-spacing: -.1em;">02/02</u></em><span class="first">28,362.17 ▲ </span><span class="second">271.12</span><span class="third">0.97%</span></li>
<li class="red"><em>홍콩항셍<u style="font-size: 11px; float: right; margin-right:10px; display: inline; font-style: normal; letter-spacing: -.1em;">02/02</u></em><span class="first">29,337.79 ▲ </span><span class="second">444.93</span><span class="third">1.54%</span></li>
</ul>
</div>
</div>
<div class="index-jisoo-box jisoo-index2">
<div class="jisoo-top">
<h3><img alt="금리환율" src="/kwa/images/hero/title_hero05.png"/></h3>
</div>
<div class="jisoo-list">
<ul>
<li class="red"><em>국고채3년</em><span class="first">0.99 ▲ </span><span class="second">0.02</span><span class="third">2.06%</span></li>
<li &nbsp;=""><em>회사채3년</em><span class="first">2.09   </span><span class="second">0.00</span><span class="third">0.00%</span></li>
<li &nbsp;=""><em>CD(91일)</em><span class="first">0.70   </span><span class="second">0.00</span><span class="third">0.00%</span></li>
<li class="red"><em>원/달러</em><span class="first">1,117.70 ▲ </span><span class="second">1.20</span><span class="third">0.11%</span></li>
<li class="red"><em>엔/달러</em><span class="first">104.97 ▲ </span><span class="second">0.29</span><span class="third">0.28%</span></li>
<li class="red"><em>유가(WTI) 근월</em><span class="first">53.55 ▲ </span><span class="second">1.35</span><span class="third">2.59%</span></li>
</ul>
</div>
</div>
<div class="index-jisoo-box">
<div class="jisoo-top">
<h3><img alt="증시주변자금" src="/kwa/images/hero/title_hero06.png"/></h3>
<div>(단위:억원)</div>
</div>
<div class="jisoo-list">
<ul>
<li class="blue"><em>고객예탁금</em><span class="first">680,172 ▼ </span><span class="second">3,118</span><span class="third">0.46%</span></li>
<li class="blue"><em>선물예수금</em><span class="first">129,372 ▼ </span><span class="second">641</span><span class="third">0.49%</span></li>
<li class="blue"><em>미수금잔고</em><span class="first">3,899 ▼ </span><span class="second">59</span><span class="third">1.48%</span></li>
<li class="blue"><em>신용잔고</em><span class="first">210,139 ▼ </span><span class="second">2,306</span><span class="third">1.09%</span></li>
</ul>
</div>
</div>

"""

be = BeautifulSoup(be, 'html.parser')
be = be.find_all('li')
jisu_dict_s= {}
for i in be:
    plma = None
    jisu_dict = {}
    jisu = i.get_text(separator='|')
    print(jisu)
#
#     #이름 구간
#     name = jisu[0].replace(' ','')
#     jisu_dict['name'] = name
#
#     #지수구간
#     num_0 = jisu[1]
#     if bool(re.search('▲',num_0)):
#         plma = True
#         plma_ment ='오른'
#         num= num_0.replace(',','').replace('▲','').replace(' ','')
#
#     elif bool(re.search('▼', num_0)):
#         plma = False
#         plma_ment = '내린'
#         num= num_0.replace(',','').replace('▼','').replace(' ','')
#     jisu_dict['num'] = num
#
#     #포인트 구간
#     point = jisu[2].replace(' ','')
#     jisu_dict['point'] = point
#
#
#     #증감율 구간
#     rate = jisu[3].replace('%','').replace(' ','')
#     jisu_dict['rate'] = rate
#
#
#     jisu_dict_s[name] =jisu_dict
#
#
# print(jisu_dict_s)
#
#
