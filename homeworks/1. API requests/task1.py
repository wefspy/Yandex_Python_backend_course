import json
import requests
from requests import Response
from main import BASE_URL

# Вывести продукты, цена которых <20
response: Response = requests.get(f'{BASE_URL}/products')

with open('responses/task1.json', 'w') as file:
    if response.status_code == 200:
        products: list[dict] = response.json()
        products_price_less_20: list[dict] = [product for product in products if product.get('price', 0) < 20]
        file.write(json.dumps(products_price_less_20, indent = 4))
    else:
        file.write(json.dumps(response.reason, indent = 4))
