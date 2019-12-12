import requests
from bs4 import BeautifulSoup
from 简易的代理池.db import save_to_redis



def get_daili():
    # for page in range(1,1):
    #     url='https://www.xicidaili.com/nn'+'/'+str(page)


    url = 'https://www.xicidaili.com/nn'
    headers = {
        'Referer': 'https://www.xicidaili.com/nn',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
    }
    resp=requests.get(url,headers=headers)
    print(resp.status_code)
    html = resp.text
    soup = BeautifulSoup(html,'lxml')
    all = soup.find_all('tr',class_='odd')
    j=1
    for i in all:

        t=i.find_all('td')
        ip =t[1].text+':'+ t[2].text
        save_to_redis(j,ip)
        print(ip)
        j+=1

def main():
    get_daili()

if __name__=='__main__':
    main()
