import requests
from bs4 import BeautifulSoup as soup


def scraping(url):

    # search any item from your browser in amazon.in and paste it
    #url = "https://www.amazon.in/Apple-MacBook-Air-13-3-inch-MQD32HN/dp/B073Q5R6VR/"

    product = {}

    post_amazon_domain = url.split('amazon.')[1].split('/')[0]

    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/76.0.3809.132 Safari/537.36'}

    res = requests.get(url, headers=headers)

    page = soup(res.text, 'lxml')

    item_name = page.find(id='productTitle').get_text()
    item_name = item_name.strip()
    product['item_name'] = item_name

    item_link = url.split('/ref')[0]
    product['item_link'] = item_link

    try:
        item_rating = page.find('span', {'class': 'a-icon-alt'}).get_text()
        product['item_rating'] = item_rating
    except AttributeError:
        product['item_rating'] = None

    if post_amazon_domain == 'com':
        try:
            item_price = page.find('span', id='priceblock_ourprice', attrs={"class": "a-size-medium a-color-price priceBlockBuyingPriceString"}).get_text()
            integer_item_price = float(item_price.lstrip('$'))
            product['item_price'] = item_price
        except AttributeError:
            product['item_price'] = None

    elif post_amazon_domain == 'in':
        try:
            item_price = page.find('span', id='priceblock_ourprice', attrs={"class": "a-size-medium a-color-price priceBlockBuyingPriceString"}).get_text()
            integer_item_price = int(item_price.replace('₹\xa0', '').split('.')[0].replace(',', ''))
            product['item_price'] = integer_item_price
        except AttributeError:
            product['item_price'] = None

    elif post_amazon_domain == 'de':
        try:
            item_price = page.find('span', id='priceblock_ourprice', attrs={"class": "a-size-medium a-color-price priceBlockBuyingPriceString"}).get_text()
            integer_item_price = float(item_price.replace('\xa0€', '').replace(',', '.'))
            product['item_price'] = integer_item_price
        except AttributeError:
            product['item_price'] = None

    elif post_amazon_domain == 'fr':
        try:
            item_price = page.find('span', id='priceblock_ourprice', attrs={"class": "a-size-medium a-color-price priceBlockBuyingPriceString"}).get_text()
            integer_item_price = float(item_price.replace('\xa0€', '').replace(',', '.'))
            product['item_price'] = integer_item_price
        except AttributeError:
            product['item_price'] = None

    else:
        product['item_price'] = None

    return product