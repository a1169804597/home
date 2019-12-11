from requests import Session
from  Weixin.weixin.config import *
from  Weixin.weixin.db import RedisQueue
from  Weixin.weixin.mysql import MySQL
from  Weixin.weixin.request import WeixinRequest
from urllib.parse import urlencode
import requests
from pyquery import PyQuery as pq
from requests import ReadTimeout, ConnectionError


class Spider():
    base_url = 'http://weixin.sogou.com/weixin'
    keyword = 'NBA'
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,ja;q=0.4,zh-TW;q=0.2,mt;q=0.2',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': 'CXID=3AE459955704DC40B7A9C4BF803AC9DC; SUID=A971AF734C238B0A5CE29DDC000E397A; IPLOC=CN4201; SUV=00972E4D73BE82EC5D65475498F2E322; wuid=AAHzkzyKKQAAAAqLK0bDdgsAGwY=; ABTEST=2|1570891290|v1; PHPSESSID=mii9hd0cmguo7al53fic3ep611; seccodeErrorCount=1|Sat, 12 Oct 2019 14:46:08 GMT; SNUID=AD3AA0457376E7C4D13C31DE74061038; seccodeRight=success; successCount=1|Sat, 12 Oct 2019 14:46:16 GMT; JSESSIONID=aaayviy4LNl9FaWWaer1w; weixinIndexVisited=1; ppinf=5|1570891332|1572100932|dHJ1c3Q6MToxfGNsaWVudGlkOjQ6MjAxN3x1bmlxbmFtZTo2OiVDMiVBMHxjcnQ6MTA6MTU3MDg5MTMzMnxyZWZuaWNrOjY6JUMyJUEwfHVzZXJpZDo0NDpvOXQybHVJMlFXaEdRb3hocmJsZmpUb1YxanNnQHdlaXhpbi5zb2h1LmNvbXw; pprdig=oG1wtfyOaf0h27Yy4eEUq1GakbVdWX9zGE12K42J9wCABTzqS09m7fhOF_pD4IGOQXMX1x9ELM_sqGgJrKMUF7cEl9sRJzIR7F6NzcB2GDB5fs3SEbLXBi3kUKmAmS8Hni9tAogYSE0vnL1Sx54QpzTc5osA9VsJwP7-2_vCswA; sgid=09-39487285-AV2h5kTAuXYdnsmFEtrSyRY; ppmdig=1570891332000000f62188001e3ecbb7610fd7cf9be07668',
        'Host': 'weixin.sogou.com',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
    }
    session = Session()
    queue = RedisQueue()
    mysql = MySQL()
    
    def get_proxy(self):
        """
        从代理池获取代理
        :return:
        """
        try:
            response = requests.get(PROXY_POOL_URL)
            if response.status_code == 200:
                print('Get Proxy', response.text)
                return response.text
            return None
        except requests.ConnectionError:
            return None
    
    def start(self):
        """
        初始化工作
        """
        # 全局更新Headers
        self.session.headers.update(self.headers)
        start_url = self.base_url + '?' + urlencode({'query': self.keyword, 'type': 2})
        weixin_request = WeixinRequest(url=start_url, callback=self.parse_index, need_proxy=True)
        # 调度第一个请求
        self.queue.add(weixin_request)
    
    def parse_index(self, response):
        """
        解析索引页
        :param response: 响应
        :return: 新的响应
        """
        doc = pq(response.text)
        items = doc('.news-box .news-list li .txt-box h3 a').items()
        for item in items:
            url = item.attr('href')
            weixin_request = WeixinRequest(url=url, callback=self.parse_detail)
            yield weixin_request
        next = doc('#sogou_next').attr('href')
        if next:
            url = self.base_url + str(next)
            weixin_request = WeixinRequest(url=url, callback=self.parse_index, need_proxy=True)
            yield weixin_request
    
    def parse_detail(self, response):
        """
        解析详情页
        :param response: 响应
        :return: 微信公众号文章
        """
        doc = pq(response.text)
        data = {
            'title': doc('.rich_media_title').text(),
            'content': doc('.rich_media_content').text(),
            'date': doc('#post-date').text(),
            'nickname': doc('#js_profile_qrcode > div > strong').text(),
            'wechat': doc('#js_profile_qrcode > div > p:nth-child(3) > span').text()
        }
        yield data
    
    def request(self, weixin_request):
        """
        执行请求
        :param weixin_request: 请求
        :return: 响应
        """
        try:
            if weixin_request.need_proxy:
                proxy = self.get_proxy()
                if proxy:
                    proxies = {
                        'http': 'http://' + proxy,
                        'https': 'https://' + proxy
                    }
                    return self.session.send(weixin_request.prepare(),
                                             timeout=weixin_request.timeout, allow_redirects=False, proxies=proxies)
            return self.session.send(weixin_request.prepare(), timeout=weixin_request.timeout, allow_redirects=False)
        except (ConnectionError, ReadTimeout) as e:
            print(e.args)
            return False
    
    def error(self, weixin_request):
        """
        错误处理
        :param weixin_request: 请求
        :return:
        """
        weixin_request.fail_time = weixin_request.fail_time + 1
        print('Request Failed', weixin_request.fail_time, 'Times', weixin_request.url)
        if weixin_request.fail_time < MAX_FAILED_TIME:
            self.queue.add(weixin_request)
    
    def schedule(self):
        """
        调度请求
        :return:
        """
        while not self.queue.empty():
            weixin_request = self.queue.pop()
            callback = weixin_request.callback
            print('Schedule', weixin_request.url)
            response = self.request(weixin_request)
            if response and response.status_code in VALID_STATUSES:
                results = list(callback(response))
                if results:
                    for result in results:
                        print('New Result', type(result))
                        if isinstance(result, WeixinRequest):
                            self.queue.add(result)
                        if isinstance(result, dict):
                            self.mysql.insert('articles', result)
                else:
                    self.error(weixin_request)
            else:
                self.error(weixin_request)
    
    def run(self):
        """
        入口
        :return:
        """
        self.start()
        self.schedule()


if __name__ == '__main__':
    spider = Spider()
    spider.run()
