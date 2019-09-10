import json


def update(item_name, item_price, item_rating, item_link):
    data = {'amazon': []}
    data['amazon'].append({
        'Item Name': item_name,
        'Item Price': item_price,
        'Item Rating': item_rating,
        'Item Link': item_link,
    })

    with open('data.json', 'w') as json_file:
        json.dump(data, json_file)
        
