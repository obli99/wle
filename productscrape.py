# This webscraper will show
# item_name
# item_price
# item_link

import requests
from bs4 import BeautifulSoup as soup
import updater


def main():
    debug = True

    # search any item from your browser in amazon.in and paste it
    url = str(input("Paste your product url here:\n"))


    post_amazon_domain = url.split('amazon.')[1].split('/')[0]

    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/76.0.3809.132 Safari/537.36'}

    res = requests.get(url, headers=headers)

    page = soup(res.text, 'lxml')

    item_name = page.find(id='productTitle').get_text()
    item_name = item_name.strip()
    print('\n')
    if debug:
        print("item_name:", item_name, "\n")

    item_link = url.split('/ref')[0]
    if debug:
        print("item_link:", item_link, "\n")

    item_rating = page.find('span', {'class': 'a-icon-alt'}).get_text()
    if debug:
        print("item_link:", item_rating, "\n")

    if post_amazon_domain == 'com':
        item_price = page.find('span', id='priceblock_ourprice').get_text()
        integer_item_price = float(item_price.lstrip('$'))
        price_flag = True
    elif post_amazon_domain == 'in':
        item_price = page.find(id='priceblock_ourprice').get_text()
        integer_item_price = int(item_price.replace('₹\xa0', '').split('.')[0].replace(',', ''))
        price_flag = True
    elif post_amazon_domain == 'de':
        item_price = page.find('span', id='priceblock_ourprice').get_text()
        integer_item_price = float(item_price.replace('\xa0€', '').replace(',', '.'))
        price_flag = True
    elif post_amazon_domain == 'fr':
        item_price = page.find('span', id='priceblock_ourprice').get_text()
        integer_item_price = float(item_price.replace('\xa0€', '').replace(',', '.'))
        price_flag = True
    else:
        print('Undefined domain')
        price_flag = False

    if price_flag:
        updater.update(item_name, integer_item_price, item_rating, item_link)


if __name__ == '__main__':
    main()

else:
    pass
