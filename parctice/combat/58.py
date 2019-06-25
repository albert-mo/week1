# coding: utf-8
from bs4 import BeautifulSoup
import requests
import time


headers = {
    'user-agent': 'Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1',
    'cookie': 'f=n; commontopbar_new_city_info=1%7C%E5%8C%97%E4%BA%AC%7Cbj; f=n; commontopbar_new_city_info=1%7C%E5%8C%97%E4%BA%AC%7Cbj; f=n; commontopbar_new_city_info=1%7C%E5%8C%97%E4%BA%AC%7Cbj; userid360_xml=DFC3578475B773D978187477C5F6F73D; time_create=1563939159227; id58=e87rZl0QRBKw2bbdAxmkAg==; f=n; city=bj; 58home=bj; commontopbar_new_city_info=1%7C%E5%8C%97%E4%BA%AC%7Cbj; 58tj_uuid=415b707b-fc05-4fe4-b9ae-942a5e6e1636; commontopbar_ipcity=wh%7C%E6%AD%A6%E6%B1%89%7C0; als=0; xxzl_deviceid=BzLf%2FmIlB5YG%2BHrinaMuH2QtbWDGaKexfa5BoSyAmSIL13nz0xvNadpvhednG%2BWv; sessionid=ea0e3319-8e20-415c-90e9-0380ae468f4f; gr_user_id=404c308f-3383-46e1-80f7-5eafa276f0b9; wmda_uuid=68b301614674e69f83bcf87b6552d608; wmda_new_uuid=1; wmda_visited_projects=%3B1409632296065; Hm_lvt_3bb04d7a4ca3846dcc66a99c3e861511=1561347158; Hm_lvt_e15962162366a86a6229038443847be7=1561347159; Hm_lpvt_3bb04d7a4ca3846dcc66a99c3e861511=1561353352; Hm_lpvt_e15962162366a86a6229038443847be7=1561353352; xzfzqtoken=zq8mFcF0d5ipTbv%2F1sOXPRsigbuTQgzdxt5MOBY%2BR90Tl3YjMf%2BWA9cQpGGV6Lcpin35brBb%2F%2FeSODvMgkQULA%3D%3D; wmda_session_id_1409632296065=1561357420549-c607d6d6-4673-ebe0; gr_session_id_98e5a48d736e5e14=c99067df-42f2-4125-b1df-96662c1daf45; gr_session_id_98e5a48d736e5e14_c99067df-42f2-4125-b1df-96662c1daf45=true; new_session=1; new_uv=3; utm_source=; spm=; init_refer=https%253A%252F%252Fcallback.58.com%252Ffirewall%252Fverifycode%253FserialId%253D6317b6990d975b90c3b969dbcc75f9b4_c81c137f65904797abe0e701883e8a50%2526code%253D22%2526sign%253D6675643442a9c99f0dda41d1c440a22c%2526namespace%253Dhuangyelistpc%2526url%253Dhttps%25253A%25252F%25252Finfo5.58.com%25252Fbj%25252Fpbdn%25252F0%25252Fpn1%25252F%25253FPGTID%25253D0d300000-0000-02ae-cc16-24d8537fb2f1%252526ClickID%25253D1'
}
goods_list = []
goods_detail = []


def get_url(page):
    base_url = 'https://bj.58.com/pbdn/0/pn{}/'
    return base_url.format(str(page))


def get_list(url):
    # print(url)
    web_data = requests.get(url, headers=headers)
    time.sleep(2)
    soup = BeautifulSoup(web_data.text, 'lxml')
    # print(soup)
    titles = soup.select('td.t > a')
    tags = soup.select('td.t > a > span')
    # print(titles)
    for title, tag in zip(titles, tags):
        # print(title.get_text(), len(list(tag.stripped_strings)))
        data = {
            'title': title.get_text(),
            'url': title.get('href')
        }
        goods_list.append(data)
    return goods_list


def get_detail(url):
    web_data = requests.get(url, headers=headers)
    time.sleep(2)
    soup = BeautifulSoup(web_data.text, 'lxml')
    category = soup.select_one('body > div.nav > a:nth-child(3)')
    title = soup.select_one('div.detail-title > h1')
    posting_time = soup.select_one('div.detail-title > div.detail-title__info > div:nth-child(1)')
    price = soup.select_one('div.infocard__container__item__main > span')
    address = soup.select_one('div.infocard__container.haveswitch > div:nth-child(2) > div.infocard__container__item__main')
    detail = {
        'category': category.get_text(),
        'title': title.get_text(),
        'posting_time': posting_time.get_text(),
        'price': price.get_text(),
        'address': address.get_text(),
    }
    return detail


for i in range(1, 2):
    # detail_url = get_list(get_url(i))[0]['url']
    # detail_url = 'https://bj.58.com/pingbandiannao/38574077861893x.shtml?link_abtest=&psid=145025750204651111695161274&entinfo=38574077861893_p&slot=-1'
    # print(get_detail(detail_url))
    detail_urls = get_list(get_url(i))
    print('There are {} goods info to pull'.format(len(detail_urls)))
    # print(detail_urls)
    for detail_url in detail_urls:
        print('Get info from {}'.format(detail_url))
        good_detail = get_detail(detail_url['url'])
        goods_detail.append(good_detail)
print(goods_detail)
