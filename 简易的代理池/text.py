from 简易的代理池.db import get_to_redis
import requests
targeurl='https://www.baidu.com'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
}
def test_url():
    for i in range(100):
        if get_to_redis(i)==None:
          pass
        else:
            ip=get_to_redis(i)
            proxies={
                'http':'http://'+ip,
                'https':'https://'+ip,
            }
            try:
                response = requests.get(targeurl, proxies=proxies, headers=headers, timeout=5).status_code
                if response == 200:
                    print(ip)

            except:
                print("该IP不可用")

if __name__=='__main__':
    test_url()