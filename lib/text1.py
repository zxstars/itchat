# coding=utf-8
'''
图灵自动回复
'''

import requests
import itchat

KEY = "8edce3ce905a4c1dbb965e6b35c3834d"

def get_response(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    msg = str(msg)
    data = {
        'key': KEY,
        'info': msg,
        'userid': 'wechat-robot',
    }
    try:
        r = requests.post(apiUrl, data=data).json()
        return r.get("text")
    except:
        return


@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
    defaultReply = 'I received: ' + msg["Text"]
    reply = "本人在疯狂写bug，有事发红包。下面是图灵回复：\n\n"+get_response(msg["Text"])
    print("接受消息："+msg["Text"])
    print("发送消息:" + reply)

    return reply or defaultReply


itchat.auto_login(hotReload=True)
itchat.run()