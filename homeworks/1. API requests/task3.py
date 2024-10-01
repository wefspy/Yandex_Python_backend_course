import json
import requests
from requests import Response
from main import BASE_URL

# Вывести все продукты с категорией  "jewelery"
response: Response = requests.get(f'{BASE_URL}/products/category/jewelery')

with open('responses/task3.json', 'w') as file:
    if response.status_code == 200:
        jewelery_products: list[dict] = response.json()
        file.write(json.dumps(jewelery_products, indent = 4))
    else:
        file.write(json.dumps(response.reason, indent = 4))
