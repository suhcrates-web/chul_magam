###집배신에 올리기 ####
import requests, json
from datetime import datetime



def do_temp(op=None, title = '제목없음', article = '내용없음', info = '내용없음'):
    info = json.dumps({"rcept_no":"", "bogoNm":"", "url":"", "url0":""})
    with open('C:/stamp/port.txt', 'r') as f:
        port = f.read().split(',')#노트북 5232, 데스크탑 5231
        port = port[1]  # http://172.30.1.53:5232/bot_v3/

    today = datetime.today().strftime("%Y-%m-%d")
    url= port + str(today) +'/'
    data = {
        'title':title,
        'article':article,
        'repl':'',
        'desk':'',
        'info': info
    }
    requests.post(
        url,
        data = data,)
