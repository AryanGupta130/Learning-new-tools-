# I am creating this file bcs I think that using an API for this project wont be the best wau to go abt implementing it
## This will go threough a youtube video and see how they pull in the data through that

import pandas as pd
import datetime
import requests
from requests.exceptions import ConnectionError
from bs4 import BeautifulSoup


def web_content_div(web_content, class_path):
    web_content_div = web_content.find_all('div', {'class' : class_path})
    try:
        spans = web_content_div[0].find_all('span')
        texts = [spans.get_text() for span in spans]
    except IndexError:
        texts = []
    return texts

def real_time_price(stock_code):
    url = 'https://finance.yahoo.com/quote/' + stock_code +'?.tsrc=fin-srch'
    try:
        r = requests.get(url)
        web_content = BeautifulSoup(r.text, "lxml")
        texts = web_content_div(web_content, 'bottom svelte-okyrr7')
        if texts != []:
            price, change = texts[0], texts[1]
        else:
            price, change = [], []
            print("ewww")
    except ConnectionError:
        print("connection error")
    return price, change

Stock = ['BRK-B ']
print(real_time_price('BRK-B '))

