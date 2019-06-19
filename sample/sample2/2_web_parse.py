# coding: utf-8
from bs4 import BeautifulSoup


with open('E:/python/project/week1/sample/sample2/web/new_index.html', 'r') as web_data:
    Soup = BeautifulSoup(web_data, 'lxml')
    print(Soup)
