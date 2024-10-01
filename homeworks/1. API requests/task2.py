import json
import requests
from requests import Response
from main import BASE_URL

# Вывести все категории
response: Response = requests.get(f'{BASE_URL}/products/categories')

with open('responses/task2.json', 'w') as file:
    if response.status_code == 200:
        categories: list[dict] = response.json()
        file.write(json.dumps(categories, indent = 4))
    else:
        file.write(json.dumps(response.reason, indent = 4))
