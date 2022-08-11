# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 11:25:05 2022

@author: LENOVO
"""

import requests

url = "https://www.newegg.com/global/in-en/samsung-galaxy-z-flip-3-5g-6-7-black/p/N82E16875168090?Item=N82E16875168090"

page = requests.get(url)

from bs4 import BeautifulSoup

soup = BeautifulSoup(page.content,"html.parser")

price = soup.find_all('div', attrs={"class":"price-current"})[0].get_text()

