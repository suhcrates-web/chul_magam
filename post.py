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

def do_mbot(op='set_disc', title = '((((테스트2)))', article = '내용없음2', rcept_no = None, stock_code='111', corp_cls =
"None", ori_url = "None", article_content_type= "8", category_ids = "211", corp_name = None, rm =" "):

    with open('C:/stamp/port.txt', 'r') as f:
        port = f.read().split(',')#노트북 5232, 데스크탑 5231
        port = port[1]  # http://172.30.1.53:5232/bot_v3/
    if port ==5232:
        return "집배신엔 안보냄"

    url = 'http://alpha.news1.kr/ajax/article_api.php'
    today = datetime.today().strftime("%Y%m%d")
    if op=='set_disc':
        data = {
            "access_token" : '7ECEB18CF30C48038076225884432F0D',
            "cmd" : "disc",
            "op" : "set_disc",
            "rcept_no" : rcept_no,
            "report_nm": title,
            "kind" : "1",
            "corp_code": stock_code,
            "corp_name": corp_name,
            "corp_cls" : corp_cls,
            "stock_code" : stock_code,
            "flr_nm" : "테스트",
            "rcept_dt" : today,
            "rm" : rm,
            "ori_url" : ori_url,
            "content" : article,
            "article_content_type" : article_content_type,
            "category_ids" : category_ids
        }
        requests.post(
            url,
            data = data,)

if __name__ == "__main__":
    today = datetime.today().strftime("%Y%m%d")

    do_mbot(rcept_no=str(today) +'32')

def do_mbot2(op='제목없음', title = '제목없음', article = '내용없음', rcept_no = None, stock_code='111', corp_cls =
"None", ori_url = "None", article_cotent_type= "8", category_id = "83", corp_name = None):
    url = 'http://talpha.news1.kr/ajax/article_api.php'
    today = datetime.today().strftime("%Y%m%d")

    data = {
        "access_token":"7ECEB18CF30C48038076225884432F0D",
        "cmd" : "article",
        "op" : "moneybot_article",
        "title" : "test",
        "content" : "test",
        "department_id" : "118",
        "category_id": "83",


    }
    requests.post(
        url,
        data = data,)




def do(op='new_article', title = '제목없음', article = '내용없음', rcept_no = None):
    #세션열기
    session_requests = requests.session()
    #로그인정보
    payload = {
        'cmd' : 'member',
        'op' : 'alpha_login',
        'uid' : 'suhcrates' ,
        'pwd' : 'sbtmdnjs1'
    }
    #로그인, 기사 보내는 ajax url.
    login_url ='http://alpha.news1.kr/ajax/ajax.php'

    if op=='new_article':
        data = {
            'cmd' : 'article',
            'op' : 'new_article',
            'autosave': '',
            'articles_num' : '',
            'article_status' : '9',
            'article_org_status': '0',
            'regist_status': '' ,
            'result_category_selected' : '83',
            'result_byline_selected':'1128',
            'result_keyword_selected': '',
            'result_keyword_str': '',
            'result_article_relation_value':'9' ,
            'article_foreign_photo_id_arr':'',
            'article_photo_id_arr':'',
            'article_movie_id_arr':'',
            'result_hotissue_selected':'',
            'user_job_title' : '5',
            'article_title' : title,
            'subSubjectChk' : '1',
            'subSubject[]' : '(테스트)',
            'article_byline_area' : '(세종=뉴스1)',
            'article_byline_selected' : '1128',
            'contentArea' : article,
            'article_editor_email' : 'suhcrates@news1.kr',
            'article_embargo_hour' : '',
            'article_embargo_min' : '',
            'department_id':'5',
            'source_id' : '10',
            'article_category_id' : '83',
            'article_category_selected' : '83',
            'article_kindof' : '1',
            'article_cotent_type[]' : '7',
            'keyword':'',
            'www_only' : '0',
            'exclude_images' : '0',
            'article_bundle_id' : '24',
            'article_bundle_selected' : '24',
            'is_edit_title':'1',
            'bundle_edited_title':'',
            'breaking' : '2',
            'article_relation_value' :'1',
            'id': '4139089',
            'code' : '1000',
            'mode' : '',
            'user_id' :'1128',
            'msg': 'OK',
            'status' : '1',

        }
    elif op=='edit_article':
        data = {
            'cmd' : 'article',
            'op' : 'edit_article',
            'autosave': '', #이거 넣으면 작동 안함. 그냥 공란으로 비워두길.
            'articles_num' : '4140779',
            'article_status' : '91',  #1  #수정완료 버튼을 누르면 91에서 11로 바꾸도록 함
            # 근데 11을 넣으면 '예약요청'이 되고 91을 넣으면 '수정완료'가 됨
            'article_org_status': '91', # 수정버튼 누르면 91 -> 11 하도록 함. 근데 막상 열어서 보면 1임
            'regist_status': '11' , #공란
            'result_category_selected' : '83',
            'result_byline_selected':'1128',
            'result_keyword_selected': '',
            'result_keyword_str': '',
            'result_article_relation_value':'' ,
            'article_foreign_photo_id_arr':'',
            'article_photo_id_arr':'',
            'article_movie_id_arr':'',
            'result_hotissue_selected':'',
            'user_job_title' : '5',
            'article_title' : title,
            'subSubjectChk' : '1',
            'subSubject[]' : '(테스트)',
            'article_byline_area' : '(세종=뉴스1)',
            'article_byline_selected' : '1128',
            'contentArea' : article,
            'article_editor_email' : 'suhcrates@news1.kr',
            'article_embargo_hour' : '',
            'article_embargo_min' : '',
            'department_id':'5',
            'source_id' : '10',
            'article_category_id' : '83',  #카테고리 설정. 5번은 '청와대' . 산업일반 83
            'article_category_selected' : '83',
            'article_kindof' : '1',
            'article_cotent_type[]' : '7',#article_cotent_type[] / content가 아니라 cotent임 / 7번이 발생
            'keyword':'',
            'www_only' : '0',
            'exclude_images' : '0',
            'article_bundle_id' : '24',
            'article_bundle_selected' : '24',
            'is_edit_title':'1',
            'bundle_edited_title':'',
            'breaking' : '2',
            'article_relation_value' :'1',
            'id': '4140779',
            'code' : '03',
            'tp' : 'edit',
            'mode' : '',
            'user_id' :'1128',
            'msg': 'OK',
            'status' : '1',
        }



    # data0['contentArea'] = content_n1
    session_requests.post(
        login_url,
        data = payload,
    )
    session_requests.post(
        login_url,
        data = data,)


