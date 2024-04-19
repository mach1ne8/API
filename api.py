import requests

# URL страницы, где лежит файл с данными
login_url = 'put your site'

# флаг - на вход будет получен файл только json формата
headers = {
    'Content-Type': 'application/json'
}

# Получаем список всех входящих соединений
response_inbounds = requests.get(login_url, headers=headers)

# проверка на соответствие порта
if response_inbounds.status_code == 80:
    # Обработка полученных данных
    inbounds = response_inbounds.json()
    print(inbounds)
else:
    print('Ошибка при получении inbounds:', response_inbounds.status_code, response_inbounds.text)

