from flask import Flask, jsonify

app = Flask(__name__)

# Маршрут API для генерации ссылки на подключение
@app.route('put your link', methods=['POST'])
def generate_link():
    # Получение параметров запроса (адрес сервера, порт, протокол)

    server_ip = ''
    server_port = ''
    server_protocol = ''

    # Генерация ссылки на подключение
    connection_link = f"{server_protocol}://{server_ip}:{server_port}"

    # Возвращение ссылки как ответа на запрос
    return jsonify({'connectionLink': connection_link})

if __name__ == '__main__':
    app.run(debug=True)

from pyxui import xui

