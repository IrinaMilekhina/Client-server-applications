"""
1. Задание на закрепление знаний по модулю CSV. Написать скрипт,
осуществляющий выборку определенных данных из файлов info_1.txt, info_2.txt,
info_3.txt и формирующий новый «отчетный» файл в формате CSV.

Для этого:

Создать функцию get_data(), в которой в цикле осуществляется перебор файлов
с данными, их открытие и считывание данных. В этой функции из считанных данных
необходимо с помощью регулярных выражений или другого инструмента извлечь значения параметров
«Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
Значения каждого параметра поместить в соответствующий список. Должно
получиться четыре списка — например, os_prod_list, os_name_list,
os_code_list, os_type_list. В этой же функции создать главный список
для хранения данных отчета — например, main_data — и поместить в него
названия столбцов отчета в виде списка: «Изготовитель системы»,
«Название ОС», «Код продукта», «Тип системы». Значения для этих
столбцов также оформить в виде списка и поместить в файл main_data
(также для каждого файла);

Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл.
В этой функции реализовать получение данных через вызов функции get_data(),
а также сохранение подготовленных данных в соответствующий CSV-файл;

Пример того, что должно получиться:

Изготовитель системы,Название ОС,Код продукта,Тип системы

1,LENOVO,Windows 7,00971-OEM-1982661-00231,x64-based

2,ACER,Windows 10,00971-OEM-1982661-00231,x64-based

3,DELL,Windows 8.1,00971-OEM-1982661-00231,x86-based

Обязательно проверьте, что у вас получается примерно то же самое.

ПРОШУ ВАС НЕ УДАЛЯТЬ СЛУЖЕБНЫЕ ФАЙЛЫ TXT И ИТОГОВЫЙ ФАЙЛ CSV!!!
"""
import os
import pathlib
import re

import chardet
import pandas as pd

root_dir = pathlib.Path(os.path.dirname(os.path.realpath(__file__)))

def get_encoding(filename: str) -> str:
    """
    Функция для определения кодировки файла
    :param filename: путь к файлу в виде строки
    :return: кодировка в виде строки
    """
    with open(filename, 'br') as file:
        detector = chardet.UniversalDetector()
        for line in file:
            detector.feed(line)
            if detector.done:
                break
        detector.close()
    return detector.result.get('encoding')


def get_filenames_in_dir(task_dir=root_dir):
    """
    Функция рекурсивно проходит по рабочей папке и собирает все txt файлы из нее. В т.ч. во вложенных структурах
    :return: список абсолютных путей до файлов
    """
    filenames = []
    for root, dirs, files in os.walk(task_dir):
        for file in files:
            if file.endswith('txt'):
                filenames.append(f'{root}/{file}')
    return filenames


def pattern_math(line, headers):
    """
    Функция сопоставляет данные из строки с набором заголовков
    :param line: строка
    :param headers: перечень заголовков
    :return: boolean
    """
    patterns = [re.compile(param) for param in headers]
    for pattern in patterns:
        if re.match(pattern, line):
            return True
    return False


def get_data():
    """
    Функция парсит файлы с информацией и собирает DataFrame с данными по указанным заголовкам
    :return: DataFrame
    """

    headers = ['Название ОС', 'Изготовитель системы', 'Код продукта', 'Тип системы']
    data_df = pd.DataFrame(columns=headers)
    data_files = get_filenames_in_dir()
    for file in data_files:
        encoding = get_encoding(file)
        with open(file, 'r', encoding=encoding) as f:
            lines = []
            for line in f.readlines():
                if pattern_math(line, headers):
                    lines.append(re.sub(r':\s+', ':', line.strip()).split(':'))
            dict_of_info_file = {line[0]: line[1] for line in lines}
            data_df = data_df.append(dict_of_info_file, ignore_index=True)
    return data_df


def write_to_csv(csv_file_path):
    """
    Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл.
    В этой функции реализовать получение данных через вызов функции get_data(),
    а также сохранение подготовленных данных в соответствующий CSV-файл;

    Пример того, что должно получиться:

    Изготовитель системы,Название ОС,Код продукта,Тип системы

    1,LENOVO,Windows 7,00971-OEM-1982661-00231,x64-based

    2,ACER,Windows 10,00971-OEM-1982661-00231,x64-based

    3,DELL,Windows 8.1,00971-OEM-1982661-00231,x86-based

    Обязательно проверьте, что у вас получается примерно то же самое.
    :param csv_file_path: путь к файлу для записи
    """
    result_df = get_data()
    with open(csv_file_path, 'w', encoding='utf-8') as f:
        result_df.index += 1
        result_df.to_csv(f)


if __name__ == '__main__':

    csv_file_path = root_dir.joinpath('result_csv.csv')
    write_to_csv(csv_file_path)
