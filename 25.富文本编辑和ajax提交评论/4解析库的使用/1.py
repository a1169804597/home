#coding:utf-8
from pyquery import PyQuery as pq
import requests

url='https://www.zhihu.com/explore'

headers = {
'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
}
html=requests.get(url,headers=headers).text
doc=pq(html)
items=doc('.explore-feed.feed-item').items()
for item in items:
    quetion=item.find('h2 a').text()
    author=item.find('a.author-link').text()
    answer=pq(item.find('.content').html()).text()
    with open('explore.txt','a',encoding='utf-8') as f:
        f.write('\n' .join([quetion,author,answer]))
        f.write('\n'+ '='*50 + '\n')




