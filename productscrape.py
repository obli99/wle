# This wepscraper will show 
# item_name
# item_price
# item_link

import requests
from bs4 import BeautifulSoup as soup

# search any item from your browser in amazon.in and paste it
URL = str(input("Paste your product url here:\n"))


headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}

text = requests.get(URL, headers=headers)
page = soup(text.content, 'html.parser')

item_name = page.find(id = 'productTitle').get_text()

item_price = page.find(id = 'priceblock_ourprice').get_text()
integer_item_price = int(item_price.replace('₹\xa0', '').split('.')[0].replace(',', ''))

item_link = URL.split('/ref')[0]

item_rating = page.find('span', {'class': 'a-icon-alt'}).get_text()

print(item_name.strip())
print(item_price)
print(item_rating)



