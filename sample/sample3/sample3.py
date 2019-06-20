# coding: utf-8
from bs4 import BeautifulSoup
import requests
import time


url = 'https://www.tripadvisor.cn/Attractions-g60763-Activities-New_York_City_New_York.html'
url_mb = 'https://www.tripadvisor.cn/Attractions-g60763-Activities-c47-New_York_City_New_York.html'
urls = ['https://www.tripadvisor.cn/Attractions-g60763-Activities-c47-oa{}-New_York_City_New_York.html#FILTERED_LIST'.format(str(i)) for i in range(30, 510, 30)]
url_saves = 'https://www.tripadvisor.cn/Recent'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'
# }
headers = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
    'Cookie': 'ServerPool=C; TART=%1%enc%3A5Tnkpnb1R6%2BhRjsNgA8yg03Bcbw3HQWjwnuqCb%2F4FkuXZ7PgJr70XCdPkc5tnkUZAFc3phsIA7c%3D; TAUnique=%1%enc%3A3gMp0ouSF2n%2FiHg4rerGlmtzBvHQ%2BhFp0P9DwlBL8YR9i1%2B2aew%2BBQ%3D%3D; TASSK=enc%3AAOcYcEXnKGaY1ldRReTNVfmT2n5d58bfS4ztSOK1GEV1bu%2F4QoaNn%2B7ZBCUccy1egC0wYWXOZ5Z5co7gDdPSXhwtHSh%2BdaHOGBu4DTn8YFBnLj58AK%2F54puE4D%2B5DyspGw%3D%3D; TAPD=tripadvisor.cn; _smt_uid=5d0ae878.d900ec0; TAAuth3=3%3A9e43aaf23f01d11498e0630885390950%3AANib7TPRptjWq7fu1mYqXx4KY%2BqdrHaHQGvqYHcw%2Fh6jnlRLwOiF2VOWC37rPPxjSm5dgjeEBR1EXREa9F%2Foi8u0oaD5Frhk8WZv8vJyZyJ9WUZNwqZQA2Jp7mO38uRz%2FJwMG4fP%2FCnu14UIdyc3toJHdn4zP1tREBa%2FRsFTetRqEaqU9p817c1TCWnSrFttGA%3D%3D; CM=%1%PremiumMobSess%2C%2C-1%7Ct4b-pc%2C%2C-1%7CRestAds%2FRPers%2C%2C-1%7CRCPers%2C%2C-1%7CWShadeSeen%2C%2C-1%7CTheForkMCCPers%2C%2C-1%7CHomeASess%2C1%2C-1%7CPremiumSURPers%2C%2C-1%7CPremiumMCSess%2C%2C-1%7CUVOwnersSess%2C%2C-1%7CRestPremRSess%2C%2C-1%7CCCSess%2C%2C-1%7CCYLSess%2C%2C-1%7CViatorMCPers%2C%2C-1%7Csesssticker%2C%2C-1%7C%24%2C%2C-1%7CPremiumORSess%2C%2C-1%7Ct4b-sc%2C%2C-1%7CRestAdsPers%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS2%2C%2C-1%7Cb2bmcpers%2C%2C-1%7CPremMCBtmSess%2C%2C-1%7CPremiumSURSess%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS%2C%2C-1%7CLaFourchette+Banners%2C%2C-1%7Csess_rev%2C%2C-1%7Csessamex%2C%2C-1%7CPremiumRRSess%2C%2C-1%7CTADORSess%2C%2C-1%7CTARSWBPers%2C%2C-1%7CSPMCSess%2C%2C-1%7CTheForkORSess%2C%2C-1%7CTheForkRRSess%2C%2C-1%7Cpers_rev%2C%2C-1%7Cmds%2C%2C-1%7CSPMCWBPers%2C%2C-1%7CRBAPers%2C%2C-1%7CRestAds%2FRSess%2C%2C-1%7CHomeAPers%2C%2C-1%7CPremiumMobPers%2C%2C-1%7CRCSess%2C%2C-1%7CLaFourchette+MC+Banners%2C%2C-1%7CRestAdsCCSess%2C%2C-1%7CRestPremRPers%2C%2C-1%7CUVOwnersPers%2C%2C-1%7Csh%2C%2C-1%7Cpssamex%2C%2C-1%7CTheForkMCCSess%2C%2C-1%7CCYLPers%2C%2C-1%7CCCPers%2C%2C-1%7Cb2bmcsess%2C%2C-1%7CSPMCPers%2C%2C-1%7CViatorMCSess%2C%2C-1%7CPremiumMCPers%2C%2C-1%7CPremiumRRPers%2C%2C-1%7CRestAdsCCPers%2C%2C-1%7CTADORPers%2C%2C-1%7CTheForkORPers%2C%2C-1%7CPremMCBtmPers%2C%2C-1%7CTheForkRRPers%2C%2C-1%7CTARSWBSess%2C%2C-1%7CPremiumORPers%2C%2C-1%7CRestAdsSess%2C%2C-1%7CRBASess%2C%2C-1%7CSPORPers%2C%2C-1%7Cperssticker%2C%2C-1%7CSPMCWBSess%2C%2C-1%7C; __gads=ID=3a5fdf50a218aa45:T=1560995963:RT=1561000938:S=ALNI_May66QqQS5DE8QQRtfAn_BGXYg6kw; interstitialCounter=-1; MobileLastViewedList=%1%%2FAttractions-g60763-Activities-c47-New_York_City_New_York.html; TATravelInfo=V2*A.2*MG.-1*HP.2*FL.3; TAReturnTo=%1%%2FProfile; roybatty=TNI1625!ALeGa654sBnhYsfkdlapZ7PCGSt7CSIzVsXwJ9UkHoDTgq%2FduAeQ68cgomUE%2FYJ36CMJyR0two8uUyJ0z%2B8YHFAisNBnQv9dnCVr1lwuAOObCVSZc9%2FH7aN%2FStNhhKj6NN%2FxYLnbM1r%2BLpnH0PfSVARZGwqTMrRAQBEMwNU6uuRv%2C1; SRT=%1%enc%3A5Tnkpnb1R6%2BhRjsNgA8yg03Bcbw3HQWjwnuqCb%2F4FkuXZ7PgJr70XCdPkc5tnkUZAFc3phsIA7c%3D; TASession=%1%V2ID.B36F65F1800731713A68FBFD9D41FB20*SQ.130*LP.%2FLangRedirect%3Fauto%3D3%26origin%3Dzh%26pool%3DC%26returnTo%3D%252F*LS.DemandLoadAjax*GR.68*TCPAR.13*TBR.73*EXEX.99*ABTR.40*PHTB.24*FS.0*CPU.28*HS.recommended*ES.popularity*AS.popularity*DS.5*SAS.popularity*FPS.oldFirst*TS.C4E2D1190455728FE0821AD243233509*LF.zhCN*FA.1*DF.0*IR.3*OD.zh*FLO.60763*TRA.false*LD.60763; TAUD=LA-1560995954916-1*RDD-1-2019_06_19*LG-5662783-2.0.F.*LD-5662784-.....'
}


def get_attractions(url, data = None):
    web_data = requests.get(url)
    time.sleep(2)
    soup = BeautifulSoup(web_data.text, 'lxml')
    titles = soup.select('div.listing_title > a[target="_blank"]')
    images = soup.select('img[width = "180"]')
    for title, image in zip(titles, images):
        data = {
            'title': title.get_text(),
            'image': image.get('src')
        }
        print(data)


def get_mb_attractions(url, data = None):
    web_data = requests.get(url, headers=headers)
    time.sleep(2)
    soup = BeautifulSoup(web_data.text, 'lxml')
    titles = soup.select('div.location')
    images = soup.select('img[width = "54"]')
    for title, image in zip(titles, images):
        data = {
            'title': title.get_text(),
            'image': image.get('src')
        }
        print(data)


# get_mb_attractions(url_mb)
# for single_url in urls:
#     get_attractions(single_url)


# web_data = requests.get(url_saves, headers=headers)
# soup = BeautifulSoup(web_data.text, 'lxml')
# titles = soup.select('div.location_summary > a[target="_blank"]')
# print(soup, titles)
