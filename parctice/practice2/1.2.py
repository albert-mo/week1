# coding: utf-8
from bs4 import BeautifulSoup


info = []
with open('E:/python/project/week1/parctice/practice2/1_2_homework_required/index.html', 'r') as web_data:
    Soup = BeautifulSoup(web_data, 'lxml')
    images = Soup.select('body > div:nth-child(2) > div > div.col-md-9 > div:nth-child(2) > div > div > img')
    titles = Soup.select('body > div:nth-child(2) > div > div.col-md-9 > div:nth-child(2) > div > div > div.caption > h4:nth-child(2) > a')
    prices = Soup.select('body > div:nth-child(2) > div > div.col-md-9 > div:nth-child(2) > div > div > div.caption > h4.pull-right')
    scoring_amounts = Soup.select('body > div:nth-child(2) > div > div.col-md-9 > div:nth-child(2) > div > div > div.ratings > p.pull-right')
    scoring_stars = Soup.select('body > div:nth-child(2) > div > div.col-md-9 > div:nth-child(2) > div > div > div.ratings > p:nth-child(2)')
    # print(scoring_stars)


for title, price, scoring_amount, scoring_star, image in zip(titles, prices, scoring_amounts, scoring_stars, images):
    data = {
        'title': title.get_text(),
        'price': price.get_text(),
        'scoring_amount': scoring_amount.get_text(),
        'scoring_star': scoring_star.find_all("span", class_='glyphicon glyphicon-star'),
        'image': image.get('src')
    }
    info.append(data)
    print(data)


for i in info:
    if len(i['scoring_star']) == 5:
        print(i['title'])
'''
body > div:nth-child(2) > div > div.col-md-9 > div:nth-child(2) > div:nth-child(3) > div > img
body > div:nth-child(2) > div > div.col-md-9 > div:nth-child(2) > div:nth-child(3) > div > div.caption > h4:nth-child(2) > a
body > div:nth-child(2) > div > div.col-md-9 > div:nth-child(2) > div:nth-child(3) > div > div.caption > h4.pull-right
body > div:nth-child(2) > div > div.col-md-9 > div:nth-child(2) > div:nth-child(3) > div > div.ratings > p.pull-right
body > div:nth-child(2) > div > div.col-md-9 > div:nth-child(2) > div:nth-child(3) > div > div.ratings > p:nth-child(2)
'''