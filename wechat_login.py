import requests
import itchat
from itchat.content import *

KEY='2fe09c6fc01949dbb2204fb9ab059d93'

def get_response(msg):
    apiurl = 'http://www.tuling123.com/openapi/api'
    data = {'key':KEY,
            'info':msg,
            'userid':'robot-lijian'}
    try:
        r = requests.post(apiurl,data=data).json()
        return r.get('text')
    except:
        return None

@itchat.msg_register([TEXT,MAP,CARD,NOTE,SHARING])
def text_reply(msg):
    print (msg['Type'],msg['Text'])
    #itchat.send(msg['Text'], msg['FromUserName'])
    tuling_replay = get_response(msg['Text'])
    if tuling_replay:
        itchat.send(tuling_replay, msg['FromUserName'])
    else:
        itchat.send(msg['Text'], msg['FromUserName'])

@itchat.msg_register([PICTURE,RECORDING,ATTACHMENT,VIDEO])
def download_files(msg):
    msg['Text'](msg['FileName'])
    return '%s%s' %({'Picture':'img','video':'vid'}.get(msg['Type'],'fil'),msg['FileName'])

@itchat.msg_register(FRIENDS)
def add_friend(msg):
    itchat.add_friend(**msg['Text'])
    itchat.send_msg('Nice to meet you',msg['RecommendInfo']['UserName'])

@itchat.msg_register(TEXT,isGroupChat=True)
def text_reply(msg):
    print msg
    if msg['isAt']:
        tuling_replay = get_response(msg['Text'])
        if tuling_replay:
            itchat.send(tuling_replay, msg['FromUserName'])
        else:
            itchat.send_msg(u'@%s\u2005I received:%s' %(msg['ActualNickName'],msg['Content']),msg['FromUserName'])

itchat.auto_login(hotReload=True)
itchat.run()

#itchat.send('test','filehelper')