#功能;抓取uid的微博的信息，把点赞、评论、转发的数量和正文的内容保存到mongdb数据库中，
# 要抓取谁的微博只需要修改VALUE和CON（containerid)值就可以。
from urllib.parse import urlencode
import requests
from pyquery import PyQuery as pq
from pymongo import MongoClient

max_page = 10
VALUE=2145291155
CON=1076032145291155
client = MongoClient(host='localhost', port=27017,password='foobared')
db = client['weibo']
collection = db['weibo']  #这个为什么不能放在main函数里面呢？

base_url = 'https://m.weibo.cn/api/container/getIndex?'

headers={
     'Host': 'm.weibo.cn',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}
def get_page(page):
    params={
         'type': 'uid',
        'value': VALUE,
        'containerid': CON,
        'page': page
    }
    url=base_url+urlencode(params)
    try:
        response=requests.get(url,headers=headers)
        if response.status_code==200:
            return response.json(),page #将得到的response转化成字典的格式
    except requests.ConnectionError as e:
        print('Error',e.args)
def parse_page(json,page:int):
    if json:
        items=json.get('data').get('cards')
        for index, item in enumerate(items):    #生成器类型不能使用for item in items
            if page == 1 and index == 1:
                continue
            else:
                item = item.get('mblog',{})
                weibo={}
                weibo['id']=item.get('id')
                weibo['text']=pq(item.get('text')).text() #text中还含有其他的格式，所以筛选之后加入pq解析器中，用text方提取出文本
                weibo['attitudes']=item.get('attitudes_count')
                weibo['comments']=item.get('comments_count')
                weibo['reposts']=item.get('reposts_count')
                yield weibo
def save_to_mongo(result):
    if collection.insert(result):
        print('Saved to Mongo')
def main():
    for page in range(1, max_page + 1):
        json = get_page(page)
        results = parse_page(*json)
        for result in results:
            print(result)
            save_to_mongo(result)
if __name__=='__main__':
    main()
