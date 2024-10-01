import json
import requests
from requests import Response
from main import BASE_URL

# Вывести всех пользователей
response: Response = requests.get(f'{BASE_URL}/users')

with open('responses/task4.json', 'w') as file:
    if response.status_code == 200:
        users: list[dict] = response.json()
        file.write(json.dumps(users, indent = 4))
    else:
        file.write(json.dumps(response.reason, indent = 4))
