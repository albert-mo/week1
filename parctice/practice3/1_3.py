# coding: utf-8
from bs4 import BeautifulSoup
import requests
import time

url = 'http://bj.xiaozhu.com/fangzi/104562426301.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36',
    'cookie': 'TY_SESSION_ID=e7591ae0-c199-45f2-b1dc-afa2a7d44f03; _uab_collina=156101126407549894604606; abtest_ABTest4SearchDate=b; Hm_lvt_92e8bc890f374994dd570aa15afc99e1=1561009318; gr_user_id=5ef62cd2-599d-4a4e-867e-df13dc782c2e; 59a81cc7d8c04307ba183d331c373ef6_gr_session_id=ce527012-3f77-4940-bebd-751c203ddd5f; 59a81cc7d8c04307ba183d331c373ef6_gr_last_sent_sid_with_cs1=ce527012-3f77-4940-bebd-751c203ddd5f; 59a81cc7d8c04307ba183d331c373ef6_gr_last_sent_cs1=N%2FA; 59a81cc7d8c04307ba183d331c373ef6_gr_session_id_ce527012-3f77-4940-bebd-751c203ddd5f=true; grwng_uid=93770626-935b-45a5-845a-eb8dc1a8b13f; Hm_lpvt_92e8bc890f374994dd570aa15afc99e1=1561011264; rule_math=l7i37gdrq7h'
}

def get_data(url, data=None):
    web_data = requests.get(url, headers=headers)
    time.sleep(0)
    soup = BeautifulSoup(web_data.text, 'lxml')
    title = soup.select('body > div.wrap.clearfix.con_bg > div.con_l > div.pho_info > h4')
    address = soup.select('body > div.wrap.clearfix.con_bg > div.con_l > div.pho_info > p > span')
    daily_price = soup.select('#pricePart > div.day_l > span')
    img_house = soup.select('#curBigImage')
    img_landlord = soup.select('#floatRightBox > div.js_box.clearfix > div.member_pic > a > img')
    name = soup.select('#floatRightBox > div.js_box.clearfix > div.w_240 > h6 > a')
    gender = soup.select('#floatRightBox > div.js_box.clearfix > div.member_pic > div')
    # data = {
    #     'title': title.get_text(),
    #     'address': address.get_text(),
    #     'daily_price': daily_price.get_text(),
    #     'img_house': img_house.get_text(),
    #     'img_landlord': img_landlord.get_text(),
    #     'name': name.get_text(),
    #     'gender': gender.get_text(),
    # }
    print(soup)


get_data(url)
