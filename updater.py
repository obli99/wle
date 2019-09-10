import json
import productscrape as ps

data = {}
data['amazon'] = []
data['amazon'].append({
    'Item Name': ps.item_name,
    'Item Price': ps.item_price,
    'Item Rating': ps.item_rating,
    'Item Link': ps.item_link,
})

with open('data.txt', 'w') as json_file:
    json.dump(data, json_file)