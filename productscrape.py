# This webscraper will show
# item_name
# item_price
# item_link

import requests
from bs4 import BeautifulSoup as soup
import updater


def main():
    debug = False

    # search any item from your browser in amazon.in and paste it
    url = str(input("Paste your product url here:\n"))
    # test URL's
    # url = 'https://www.amazon.com/dp/B014RWWURC'
    # url = 'https://www.amazon.com/dp/1449325866'
    # url = 'https://www.amazon.in/dp/B01J0XWYKQ/'
    # url = 'https://www.amazon.de/dp/B01MYQ4HJD'
    # url = 'https://www.amazon.fr/dp/B01MQE8CJW/'
    if debug:
        print("URL:", url, "\n")
    post_amazon_domain = url.split('amazon.')[1].split('/')[0]
    if debug:
        print("post_amazon_domain:", post_amazon_domain, "\n")

    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/76.0.3809.132 Safari/537.36'}

    # res is an object of <class 'requests.models.Response'>
    res = requests.get(url, headers=headers)
    if debug:
        print("res:", res, "\n")
    # page is an object of <class 'bs4.BeautifulSoup'>
    page = soup(res.text, 'lxml')

    item_name = page.find(id='productTitle').get_text()
    item_name = item_name.strip()
    if debug:
        print("item_name:", item_name, "\n")

    item_link = url.split('/ref')[0]
    if debug:
        print("item_link:", item_link, "\n")

    item_rating = page.find('span', {'class': 'a-icon-alt'}).get_text()
    if debug:
        print("item_link:", item_rating, "\n")

    if post_amazon_domain == 'com':
        print(".com\n")
        try:
            item_price = page.find('span', id='newBuyBoxPrice').get_text()
            integer_item_price = int(item_price.replace('₹\xa0', '').split('.')[0].replace(',', '').lstrip('$'))
            price_flag = True
        except AttributeError:
            try:
                item_price = str(page.find(id='mediaNoAccordion'))
                item_price = item_price.split('<span class="a-size-medium a-color-price header-price">')[1]
                item_price = item_price.split('</span>')[0].strip()
                integer_item_price = int(item_price.replace('₹\xa0', '').split('.')[0].replace(',', '').lstrip('$'))
                price_flag = True
            except AttributeError:
                print('Unable to find price.')
                price_flag = False
    elif post_amazon_domain == 'in':
        print(".in\n")
        item_price = page.find(id='priceblock_ourprice').get_text()
        integer_item_price = int(item_price.replace('₹\xa0', '').split('.')[0].replace(',', ''))
        price_flag = True
    elif post_amazon_domain == 'de':
        print(".de\n")
        item_price = page.find('span', id='newBuyBoxPrice').get_text()
        integer_item_price = int(item_price.replace('₹\xa0', '').split(',')[0].lstrip('EUR '))
        price_flag = True
    elif post_amazon_domain == 'fr':
        print(".fr\n")
        item_price = page.find('span', id='newBuyBoxPrice').get_text()
        integer_item_price = int(item_price.replace('₹\xa0', '').split(',')[0].lstrip('EUR '))
        price_flag = True
    else:
        print('Undefined domain')
        price_flag = False

    if price_flag:
        updater.update(item_name, item_price, item_rating, item_link)
        if debug:
            print("item_price:", item_price, "\n")
            print("integer_item_price:", integer_item_price, "\n")
            print("Data has been written to the data.json file.\n")


if __name__ == '__main__':
    main()

else:
    pass
