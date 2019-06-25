# coding: utf-8
import time

from bs4 import BeautifulSoup
import requests

detail_url = 'https://bj.58.com/pingbandiannao/38574077861893x.shtml?link_abtest=&psid=145025750204651111695161274&entinfo=38574077861893_p&slot=-1'
url1 = 'https://jst1.58.com/counter?infoid=33705648867640&userid=&uname=&sid=0&lid=0&px=0&cfpath='


headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.36',
    'Referer': 'https://bj.58.com/pingbandiannao/26062681492781x.shtml?adtype=1&entinfo=26062681492781_q&adact=3&psid=121770456204659668829687360&iuType=q_2&link_abtest=&ClickID=3&PGTID=0d300000-0000-0f11-a812-aac18c5d4b8a&slot=1000019'}


def get_count_url(detail_url):
    base_url = 'https://jst1.58.com/counter?infoid={}&userid=&uname=&sid=0&lid=0&px=0&cfpath='
    count_url = base_url.format(detail_url.split('/')[4].split('x')[0])
    return count_url


def get_count(detail_url):
    web_data = requests.get(get_count_url(detail_url), headers=headers)
    time.sleep(1)
    soup = BeautifulSoup(web_data.text, 'lxml')
    body = soup.select_one('body').get_text()
    total = body.split('=')[2]
    return total

