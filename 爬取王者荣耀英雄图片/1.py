
# !E:\python\env\python37
# -*- coding:utf-8 -*-
# @time :2019/5/23
# @Auther :zbwu103
# @name:爬取王者荣耀英雄皮肤方法一

import os, re
import requests
from requests import codes
from hashlib import md5

url = 'https://pvp.qq.com/web201605/js/herolist.json'
headers = {
    'referer': 'https://pvp.qq.com/web201605/herolist.shtml',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest'
}
html = requests.get(url, headers=headers)
html = html.json()
# print(html)
heroname = list(map(lambda x: x['cname'], html))
heronumber = list(map(lambda x: x['ename'], html))


# print(heroname)
# print(heronumber)

def main():
    li = 0
    for v in heronumber:
        img_path = 'img' + os.path.sep + heroname[li]
        # print(img_path )
        if not os.path.exists(img_path):
            os.makedirs(img_path)
        li += 1
        for u in range(1, 12):
            hero_links = 'http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/' + str(v) + '/' + str(
                v) + '-bigskin-' + str(u) + '.jpg'
            # print(hero_links)
            im = requests.get(hero_links)
            if im.status_code == 200:
                file_path = img_path + os.path.sep + str(u) + '.jpg'

                if not os.path.exists(file_path):
                    with open(file_path, 'wb') as f:
                        f.write(im.content)
                        print('下载完成')
                else:
                    print('图片已经存在')


if __name__ == "__main__":
    main()
