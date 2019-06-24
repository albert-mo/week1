# coding: utf-8
from bs4 import BeautifulSoup
import requests
import time


def get_url(page):
    base_url = 'https://bj.58.com/pbdn/0/pn{}/'
    return base_url.format(str(page))


print(get_url(2))
