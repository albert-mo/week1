# coding: utf-8
import urllib
from bs4 import BeautifulSoup
import requests
import time


url_list = []
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.36'
}
path = 'E:/python/project/downloads/'
proxies = {"http": "http://121.69.29.162:8118"}


def get_url(page):
    url = 'https://weheartit.com/inspirations/taylorswift?page='
    return url + str(page)


def get_data(page, data=None):
    url = get_url(page)
    web_data = requests.get(url, proxies=proxies)
    time.sleep(2)
    soup = BeautifulSoup(web_data.text, 'lxml')
    # imgs_figure = soup.select('figure > img')
    # for img in imgs_figure:
    #     data = {
    #         'img': img.get('src')
    #     }
    # imgs = soup.select('img[height="250"]')
    imgs = soup.select('img.entry-thumbnail')
    for img in imgs:
        data = {
            'img': img.get('src')
        }
        url_list.append(img.get('src'))
    # print(url_list)
    return url_list


def dl_image(url):
    para = path + url.split('/')[-2] + url.split('/')[-1].split('?')[0]
    # para = 'E:/python/project/downloads/316635662superthumb.jpg'
    print(para)
    urllib.request.urlretrieve(url, para)
    print('Done')


for i in range(1, 3):
    get_data(i)
print(len(get_data(i)), 'pictures will be downloaded!')


for l in url_list:
    dl_image(l)
