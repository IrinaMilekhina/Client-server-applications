"""Функции клиента:

сформировать presence-сообщение;
отправить сообщение серверу;
получить ответ сервера;
разобрать сообщение сервера;
параметры командной строки скрипта client.py []:

addr — ip-адрес сервера;
port — tcp-порт на сервере, по умолчанию 7777.
"""
import json
import sys
import time
from socket import socket, AF_INET, SOCK_STREAM

from common.configs import DEFAULT_CLIENT_IP_ADDRESS, DEFAULT_PORT, ACTION, PRESENCE, TIME, USER, ACCOUNT_NAME, \
    RESPONSE, ERROR
from common.utils import send_message, get_message


def process_ans(message):
    '''
    Функция разбирает ответ сервера
    :param message:
    :return:
    '''
    if RESPONSE in message:
        if message[RESPONSE] == 200:
            return '200 : OK'
        return f'400 : {message[ERROR]}'
    raise ValueError


def create_presence(account_name='Guest'):
    '''
    Функция генерирует запрос о присутствии клиента
    :param account_name:
    :return: словарь для JIM протокола
    '''
    out = {
        ACTION: PRESENCE,
        TIME: time.time(),
        USER: {
            ACCOUNT_NAME: account_name
        }
    }
    return out


def get_serv_address():
    try:
        server_address = sys.argv[sys.argv.index('addr') + 1]
    except IndexError:
        print(
            'После параметра \'addr\'- необходимо указать адрес сервера.')
        sys.exit(1)
    return server_address


def get_serv_port():
    try:
        server_port = int(sys.argv[sys.argv.index('-p') + 1])
        if 1024 < server_port > 65535:
            raise ValueError
    except IndexError:
        print('После параметра \'port\' необходимо указать номер порта.')
        sys.exit(1)
    except ValueError:
        print(
            'В качастве порта может быть указано только число в диапазоне от 1024 до 65535.')
        sys.exit(1)
    return server_port


def prepare_client():
    server_address = DEFAULT_CLIENT_IP_ADDRESS
    if 'addr' in sys.argv:
        server_address = get_serv_address()
    server_port = DEFAULT_PORT
    if 'port' in sys.argv:
        server_port = get_serv_port()
    transport = socket(AF_INET, SOCK_STREAM)
    transport.connect((server_address, server_port))
    return transport


if __name__ == '__main__':
    client_socket = prepare_client()

    message_to_server = create_presence()
    send_message(client_socket, message_to_server)
    try:
        answer = process_ans(get_message(client_socket))
        print(answer)
    except (ValueError, json.JSONDecodeError):
        print('Не удалось декодировать сообщение сервера.')