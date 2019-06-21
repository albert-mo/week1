# coding: utf-8
from bs4 import BeautifulSoup
import requests
import time

url_links = 'https://bj.xiaozhu.com/'
url = 'https://xm.xiaozhu.com/fangzi/93319887403.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36',
}
page_link = [] # <- 每个详情页的链接都存在这里，解析详情的时候就遍历这个列表然后访问就好啦~


def judge_gender(class_name):
    if class_name == 'member_ico':
        return '男'
    elif class_name == 'member_ico1':
        return '女'
    else:
        return '未知结果'


def get_page_link(page_number):
    for each_number in range(1, page_number): # 每页24个链接,这里输入的是页码
        full_url = 'http://bj.xiaozhu.com/search-duanzufang-p{}-0/'.format(each_number)
        wb_data = requests.get(full_url)
        soup = BeautifulSoup(wb_data.text, 'lxml')
        for link in soup.select('a.resule_img_a'): # 找到这个 class 样为resule_img_a 的 a 标签即可
            page_link.append(link.get('href'))


def get_data(url, data=None):
    web_data = requests.get(url, headers=headers)
    time.sleep(3)
    soup = BeautifulSoup(web_data.text, 'lxml')
    title = soup.select_one('div.pho_info > h4 > em')
    address = soup.select_one('div.pho_info > p > span')
    daily_price = soup.select_one('div.day_l > span')
    img_house = soup.select_one('#curBigImage')
    img_landlord = soup.select_one('#floatRightBox > div.js_box.clearfix > div.member_pic > a > img')
    name = soup.select_one('#floatRightBox > div.js_box.clearfix > div.w_240 > h6 > a')
    gender = soup.select_one('#floatRightBox > div.js_box.clearfix > div.member_pic > div')
    data = {
        'title': title.get_text(),
        'address': address.get_text(),
        'daily_price': daily_price.get_text(),
        'img_house': img_house.get_text(),
        'img_landlord': img_landlord.get_text(),
        'name': name.get_text(),
        'gender': judge_gender(gender.get('class')[0])
    }
    print(data)


# get_data(url)
get_page_link(11)
for i in range(1, len(page_link)):
    get_data(page_link[i])
