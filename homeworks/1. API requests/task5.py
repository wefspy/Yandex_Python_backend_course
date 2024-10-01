import json
import requests
from requests import Response
from main import BASE_URL

user: json = {
    'username': 'johnd',
}

# Добавить пользователя со своим именем.
response: Response = requests.post(f'{BASE_URL}/users', user)

with open('responses/task5.json', 'w') as file:
    if response.status_code == 200:
        file.write(json.dumps(response.json(), indent = 4))
    else:
        file.write(json.dumps(response.reason, indent = 4))