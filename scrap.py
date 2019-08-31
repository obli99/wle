# This wepscraper will show 
# item_name
# item_price
# item_link

import requests
from bs4 import BeautifulSoup


URL = 'https://www.amazon.in/s?k=keyword&ref=nb_sb_noss'
url = 'https://www.amazon.in'
headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}

keyword = str(input("What do you want to search on amazon: "))
keyword = keyword.strip().replace(" ", "+")
URL = URL.replace("keyword", keyword)

text = requests.get(URL, headers=headers)
soup = BeautifulSoup(text.content, 'html.parser')


item_href_names_container = soup.findAll('a', {"class": "a-link-normal a-text-normal"})
item_price_container = soup.findAll("span", {"class": "a-offscreen"})


num = 1
for item_links in item_href_names_container:
    print("Item No: {}".format(num))
    item_name = item_links.span
    print("Item Name: {}".format(item_name.text))
    print("Price: {}".format(item_price_container[num].text))
    item_link = url+item_links.get('href')
    print("Item Link: {}".format(item_link))
    print("-------------------------------------------------------------------------------")
    num += 1

