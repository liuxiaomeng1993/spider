import requests

from day03.ydm import ydm_api

session = requests.session()

def get_code():
    url = 'https://so.gushiwen.org/RandCode.ashx'

    resp = session.get(url)


    with open('code.png', 'wb') as f:
        f.write(resp.content)

    code = ydm_api('code.png')
    print(code)

    return code

def login():
    url = 'https://so.gushiwen.org/user/login.aspx'

    data = {
        'email': '673469226@qq.com',
        'pwd': 'l19930417',
        'code': get_code()
    }

    resp = session.post(url, data)


    with open('gsw_logined.html', 'w', encoding='utf-8') as f:
        f.write(resp.text)

if __name__ == '__main__':
    login()