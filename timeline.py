from datetime import datetime
import article
from make_dict import make_dict
import post
import schedule
import time
from telebot import bot

def chulbal(test=False):
    chul_ma = False
    test = test
    while not chul_ma:
        now= datetime.today().strftime(format='%H:%M')
        if (now > '9:00' and now < '9:05') | test==True :
            dict_made = make_dict()
            chul_ma = True

            #코스피
            art = article.kos_pi_daq(jisu_dict_s=dict_made, pi_daq='kospi', chul_ma=chul_ma)
            post.do_temp(title=art['title'], article=art['article'])
            print(art['title'])
            #코스닥
            art = article.kos_pi_daq(jisu_dict_s=dict_made, pi_daq='kosdaq', chul_ma=chul_ma)
            post.do_temp(title=art['title'], article=art['article'])

            #환율
            art = article.dol_won(jisu_dict_s=dict_made, chul_ma=chul_ma)
            post.do_temp(title=art['title'], article=art['article'])

            #2보
            art = article.second_bo(jisu_dict_s=dict_made, chul_ma=chul_ma)
            post.do_temp(title=art['title'], article=art['article'])
            
            bot('c' ,"출발 기사 올렸습니다!\n"+"http://testbot.ddns.net:5231/bot_v3")
        time.sleep(1)

def magam(test=False):
    chul_ma = True
    test = test
    while chul_ma:
        now= datetime.today().strftime(format='%H:%M')
        if (now > '15:30' and now < '15:35') | test==True :
            dict_made = make_dict()
            chul_ma = False

            #코스피
            art = article.kos_pi_daq(jisu_dict_s=dict_made, pi_daq='kospi', chul_ma=chul_ma)
            post.do_temp(title=art['title'], article=art['article'])
            print(art['title'])
            #코스닥
            art = article.kos_pi_daq(jisu_dict_s=dict_made, pi_daq='kosdaq', chul_ma=chul_ma)
            post.do_temp(title=art['title'], article=art['article'])

            #환율
            art = article.dol_won(jisu_dict_s=dict_made, chul_ma=chul_ma)
            post.do_temp(title=art['title'], article=art['article'])

            #2보
            art = article.second_bo(jisu_dict_s=dict_made, chul_ma=chul_ma)
            post.do_temp(title=art['title'], article=art['article'])

            bot('c' ,"마감 기사 올렸습니다!\n"+"http://testbot.ddns.net:5231/bot_v3")
        time.sleep(1)

def magam_test():
    print("fuck")
    magam(test=True)


schedule.every().day.at("09:00").do(chulbal)
schedule.every().day.at("15:30").do(magam)
schedule.every().day.at("19:49").do(magam_test)
i=1
while True:
   i= i+1
   schedule.run_pending()
   time.sleep(1)
   print(i)
