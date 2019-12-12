#-*- coding:utf-8 -*-

import requests,os
from  bs4  import BeautifulSoup
from urllib.parse import urlencode
from requests import codes
from hashlib import md5
from multiprocessing.pool import Pool

session=requests.session()
header1={
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
}
def get_img_url(header,page):

    bas_url = 'https://www.mzitu.com'
    #妹子网的URL实现了翻页
    url=bas_url+'/'+'page/'+str(page)
    # print(url)
    html=requests.get(url,headers=header1).text

    url_str=BeautifulSoup(html,'lxml').find('ul',id='pins')
    if url_str:
        for li in url_str.find_all('li'):
            yield {
                #图片详情的URl
                'page_url':li.find('a')['href'],
                #图片简介的标题
                'alt':li.find('img')['alt']
            }
def save_img(imgs):

    url = imgs['page_url'] #因为yield是生成器类型，和列表类型类似取出URL
    num=url.split("/",-1)[3] #取出后面的数字列表
    html=session.get(url,headers=header1).text #得到图片详情页的HTML
    bs=BeautifulSoup(html,'lxml')

    if bs.find('div',class_='pagenavi'):
        # 获取页码
        count=bs.find('div',class_='pagenavi').find_all('span')[-2].text
        for index in range(1,int(count)+1):
            #网页防爬机制，网页详情页，headers中需要referer
            header2 = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
                'referer': 'https://www.mzitu.com/' + str(num) +'/'+str(index)
            }
            #获得每一张图片的URL页面的URL
            url_src=url+'/'+str(index)
            html_img = session.get(url_src, headers=header2).text
            bs = BeautifulSoup(html_img, 'lxml')
            if bs.find('p'):
                #获取每一张.jpg的图片
                url_img = bs.find('p').select('img')[0]['src']
                img_path = 'img' + os.path.sep + imgs['alt']
                if not os.path.exists(img_path):
                    os.makedirs(img_path)
                try:
                    img = session.get(url_img, headers=header2)
                    if codes.ok == img.status_code:
                        file_path = img_path + os.path.sep + '{file_name}.{file_suffix}'.format(
                            file_name=md5(img.content).hexdigest(),
                            file_suffix='jpg')
                        if not os.path.exists(file_path):
                            with open(file_path, 'wb') as f:
                                f.write(img.content)
                            # print('Downloaded image path is %s' % file_path)
                            print('下载完成')
                        else:
                            print('目标图片已经存在')
                except requests.ConnectionError:
                    print('图片保存失败 %s' %img )

def main(page):
    for i in get_img_url(header1,page):
        save_img(i)



if __name__=='__main__':
    for page in range(0,100):
        main(page)




