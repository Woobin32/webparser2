
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE","webparser.settings")

import django
django.setup()

from data.models import WebData

def parse_web():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    url = 'https://www.koreaherald.com//'
    req = requests.get(url)
# url 에 접속해라. 요청해라.

    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    titles = soup.select(
        'dd > a'
    )


    data = {}
# print(titles)

    for title in titles:
        data[title.text] = url + title.get('href')
        # print(title.text)
        # print(title.get('href'))
    return data

if __name__ == '__main__':
    web_data_dict = parse_web()
    for t, l in web_data_dict.items():
        WebData(title=t, link=url+l).save()