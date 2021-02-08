from datetime import datetime
import article
from make_dict import make_dict, magam_check
import post
import time
from telebot import bot

def chulbal(test=True):
    chul_ma = False
    test = test
    while not chul_ma:
        now= datetime.today().strftime(format='%H:%M')
        today = datetime.today().strftime("%Y%m%d")

        dict_made = make_dict()['jisu_dict_s']
        chul_ma = True

        #코스피
        art = article.kos_pi_daq(jisu_dict_s=dict_made, pi_daq='kospi', chul_ma=chul_ma)
        post.do_temp(title=art['title'], article=art['article'])
        post.do_mbot(title=art['title'], article=art['article'], rcept_no = str(today) +'11', rm="출발") # c:
        # 출발 ,
        # a: 순서
        print(art['title'])
        #코스닥
        art = article.kos_pi_daq(jisu_dict_s=dict_made, pi_daq='kosdaq', chul_ma=chul_ma)
        post.do_temp(title=art['title'], article=art['article'])
        post.do_mbot(title=art['title'], article=art['article'], rcept_no = str(today) +'12', rm="출발")

        #환율
        art = article.dol_won(jisu_dict_s=dict_made, chul_ma=chul_ma)
        post.do_temp(title=art['title'], article=art['article'])
        post.do_mbot(title=art['title'], article=art['article'], rcept_no = str(today) +'13', rm="출발")

        #2보
        art = article.second_bo(jisu_dict_s=dict_made, chul_ma=chul_ma)
        post.do_temp(title=art['title'], article=art['article'])
        post.do_mbot(title=art['title'], article=art['article'], rcept_no = str(today) +'14', rm="출발")

        bot('c' ,"출발 기사 올렸습니다!\n"+"http://testbot.ddns.net:5231/bot_v3")
        print('출발')


def magam(test=True, be_0=None):
    chul_ma = True
    test = test
    while chul_ma:
        now= datetime.today().strftime(format='%H:%M')
        today = datetime.today().strftime("%Y%m%d")
        dict_made = make_dict(be_0=be_0)['jisu_dict_s']
        chul_ma = False

        #코스피
        art = article.kos_pi_daq(jisu_dict_s=dict_made, pi_daq='kospi', chul_ma=chul_ma)
        post.do_temp(title=art['title'], article=art['article'])
        post.do_mbot(title=art['title'], article=art['article'], rcept_no = str(today) +'21', rm="마감")
        print(art['title'])
        #코스닥
        art = article.kos_pi_daq(jisu_dict_s=dict_made, pi_daq='kosdaq', chul_ma=chul_ma)
        post.do_temp(title=art['title'], article=art['article'])
        post.do_mbot(title=art['title'], article=art['article'], rcept_no = str(today) +'22', rm="마감")

        #환율
        art = article.dol_won(jisu_dict_s=dict_made, chul_ma=chul_ma)
        post.do_temp(title=art['title'], article=art['article'])
        post.do_mbot(title=art['title'], article=art['article'], rcept_no = str(today) +'23', rm="마감")

        #2보
        art = article.second_bo(jisu_dict_s=dict_made, chul_ma=chul_ma)
        post.do_temp(title=art['title'], article=art['article'])
        post.do_mbot(title=art['title'], article=art['article'], rcept_no = str(today) +'24', rm="마감")

        bot('c' ,"마감 기사 올렸습니다!\n"+"http://testbot.ddns.net:5231/bot_v3")
        print('마감')

def magam_test():
    print("fuck")
    magam(test=True)


i=0
while True:
    now= datetime.today().strftime(format='%H:%M')
    print('here')
    #출발
    if (now >= "09:00") and (now<="09:05"):
        chulbal_done = False
        while not chulbal_done:
            try:
                chulbal()
                chulbal_done = True

            except:
                time.sleep(3)

        time.sleep(600)
    print('here2')
    #마감

    if (now >= "15:30") and (now<="20:50"):
        magam_done = False


        while not magam_done:
            #체크한 뒤 html 내놓음.
            be_0 = magam_check()['be_0']
            magam(be_0= be_0)
            magam_done = True
            time.sleep(1000)

    print('here3')
    i= i+1
    time.sleep(1)
    print(str(now)+' '+str(i))
