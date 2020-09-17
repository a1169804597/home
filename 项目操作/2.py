import requests
import itchat

KEY = 'd364bd41d25c4c1a9dfcecccf8ed8494'

def get_response(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
    'key' : KEY,
    'info' : msg,
    'userid' : 'wechat-robot',
    }
    try:
        r = requests.post(apiUrl, data=data).json()
        return r.get('text')
    except Exception as e:
        print(e)

@itchat.msg_register(['Map', 'Card', 'Note', 'Sharing', 'Picture','Text'])
def tuling_reply(msg):
    defaultReply = 'I received: ' + msg['Text']
    reply = get_response(msg['Text'])
    return reply or defaultReply

itchat.auto_login(hotReload=True)
itchat.run()