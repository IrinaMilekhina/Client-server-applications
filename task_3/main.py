"""
3. Задание на закрепление знаний по модулю yaml.
 Написать скрипт, автоматизирующий сохранение данных
 в файле YAML-формата.
Для этого:

Подготовить данные для записи в виде словаря, в котором
первому ключу соответствует список, второму — целое число,
третьему — вложенный словарь, где значение каждого ключа —
это целое число с юникод-символом, отсутствующим в кодировке
ASCII(например, €);

Реализовать сохранение данных в файл формата YAML — например,
в файл file.yaml. При этом обеспечить стилизацию файла с помощью
параметра default_flow_style, а также установить возможность работы
с юникодом: allow_unicode = True;

Реализовать считывание данных из созданного файла и проверить,
совпадают ли они с исходными.
"""
import os
import pathlib

import yaml
from random import randint
from pprint import pprint

root_dir = pathlib.Path(os.path.dirname(os.path.realpath(__file__)))
yaml_file = root_dir.joinpath('file.yaml')

DATA_WRITE = {
    'first': [f'value_{item:02d}' for item in range(1, 11)],
    'second': randint(1, 100),
    'third': {
        key: randint(1, 100) for key in
        (f'{item}-{chr(item)}' for item in range(1040, 1051))
    },
}


with open(yaml_file, 'w', encoding='UTF-8') as file:
    yaml.dump(DATA_WRITE, file, default_flow_style=False, allow_unicode=True)

with open(yaml_file, encoding='UTF-8') as file:
    DATA_READ = yaml.load(file, yaml.Loader)

print('Словарь для записи в yaml-файл:')
pprint(DATA_WRITE)

print('\nСловарь, выгруженный из yaml-файла:')
pprint(DATA_READ)

print('\nСовпадают ли словари:', DATA_WRITE == DATA_READ)


