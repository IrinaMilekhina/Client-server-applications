"""
Функции сервера:

принимает сообщение клиента;
формирует ответ клиенту;
отправляет ответ клиенту;
имеет параметры командной строки:

-p — TCP-порт для работы (по умолчанию использует 7777);
-a — IP-адрес для прослушивания (по умолчанию слушает все доступные адреса).
"""
import json
import sys
from socket import socket, AF_INET, SOCK_STREAM

from common.configs import DEFAULT_PORT, MAX_CONNECTIONS, ACTION, PRESENCE, TIME, USER, ACCOUNT_NAME, RESPONSE, ERROR
from common.utils import get_message, send_message


def process_client_message(message):
    '''
    Обработчик сообщений от клиентов, принимает словарь -
    сообщение от клинта, проверяет корректность,
    возвращает словарь-ответ для клиента

    :param message:
    :return:
    '''
    if ACTION in message and message[ACTION] == PRESENCE and TIME in message \
            and USER in message and message[USER][ACCOUNT_NAME] == 'Guest':
        return {RESPONSE: 200}
    return {
        RESPONSE: 400,
        ERROR: 'Bad Request'
    }


def get_port():
    try:
        listen_port = int(sys.argv[sys.argv.index('-p') + 1])
        if 1024 < listen_port > 65535:
            raise ValueError
    except IndexError:
        print('После параметра -\'p\' необходимо указать номер порта.')
        sys.exit(1)
    except ValueError:
        print(
            'В качастве порта может быть указано только число в диапазоне от 1024 до 65535.')
        sys.exit(1)
    return listen_port


def get_address():
    try:
        listen_address = sys.argv[sys.argv.index('-a') + 1]
    except IndexError:
        print(
            'После параметра \'a\'- необходимо указать адрес, который будет слушать сервер.')
        sys.exit(1)
    return listen_address


def prepare_server():
    listen_port = DEFAULT_PORT
    if '-p' in sys.argv:
        listen_port = get_port()
    listen_address = ''
    if '-a' in sys.argv:
        listen_address = get_address()
    transport = socket(AF_INET, SOCK_STREAM)
    transport.bind((listen_address, listen_port))
    transport.listen(MAX_CONNECTIONS)
    return transport


if __name__ == '__main__':
    serv_socket = prepare_server()

    while True:
        client, client_address = serv_socket.accept()
        try:
            message_from_client = get_message(client)
            response = process_client_message(message_from_client)
            send_message(client, response)
            client.close()
        except (ValueError, json.JSONDecodeError):
            print('Принято некорретное сообщение от клиента.')
            client.close()


