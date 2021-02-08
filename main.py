import requests
import os
from pprint import pprint
import random

# token = os.environ['token']
token = '1646026624:AAFl-4-09PT5AM5T1RewNdGSo52jnLMLNv4'
# 1258594598
# AgACAgQAAxkBAAMOYCC-dNtXi3ZzJ8xHlMVXSVycWOsAAuyqMRtxmGxQW71jzwkrdqeImgABI10AAwEAAwIAA20AAz-IAAIeBA

def getUpdates():
    url = f'https://api.telegram.org/bot{token}/getUpdates'
    r = requests.get(url)
    data = r.json()['result'][-1]['message']

    return data

def sendPhoto(ids):
    url_rasm = 'https://random.dog/doggos'
    r1 = requests.get(url_rasm)
    choise = r1.json()
    # pprint(choise)
    url = f'https://api.telegram.org/bot{token}/sendPhoto'
    payload = {
        'chat_id': ids,
        'photo': f"https://random.dog/{random.choice(choise)}"
    }
    respons = requests.get(url=url, params=payload)
    pprint(respons.json())


# sendPhoto(1258594598)
def sendKeyboard(idx=1258594598):
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    payload = {
        'chat_id': idx,
        'text':'dog',
        'reply_markup': {
            'keyboard': [
                [{'text': 'dog'}]
            ],
            'resize_keyboard': True
        }
    }
    r = requests.post(url=url, json=payload)
    pprint(r.json())

m0 = getUpdates()['message_id']
while True:
    data = getUpdates()
    m1 = data['message_id']
    msg_text = data['text']
    user_id = data['from']['id']
    if m0 != m1:
        if msg_text == 'dog':
            sendPhoto(user_id)
        sendKeyboard(user_id)
        # if msg_text == 'dog':
        m0 = m1
