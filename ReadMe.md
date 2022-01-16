# Курс клиент-серверные приложения
19.12.2021

python 3.8.10

ДЗ 1:
---
1. Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и проверить тип и 
содержание соответствующих переменных. Затем с помощью онлайн-конвертера преобразовать строковые представление 
в формат Unicode и также проверить тип и содержимое переменных.
2. Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в последовательность кодов 
(не используя методы encode и decode) и определить тип, содержимое и длину соответствующих переменных.
3. Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.
4. Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления в байтовое 
и выполнить обратное преобразование (используя методы encode и decode).
5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из байтовового в строковый тип на кириллице.
6. Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет», «декоратор». 
Проверить кодировку файла по умолчанию. Принудительно открыть файл в формате Unicode и вывести его содержимое.


ДЗ 2:
---
###1. Задание на закрепление знаний по модулю CSV. 

Написать скрипт, осуществляющий выборку определенных данных из файлов info_1.txt, info_2.txt, info_3.txt
и формирующий новый «отчетный» файл в формате CSV. 

Для этого:

Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными, их открытие и считывание данных.

В этой функции из считанных данных необходимо с помощью регулярных выражений извлечь значения параметров 
«Изготовитель системы», «Название ОС», «Код продукта», «Тип системы». 

Значения каждого параметра поместить в соответствующий список. 
Должно получиться четыре списка — например, os_prod_list, os_name_list, os_code_list, os_type_list. 

В этой же функции создать главный список для хранения данных отчета — например, main_data — 
и поместить в него названия столбцов отчета в виде списка: «Изготовитель системы», «Название ОС», 
«Код продукта», «Тип системы». 

Значения для этих столбцов также оформить в виде списка и поместить в файл main_data 
(также для каждого файла);

Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл. 

В этой функции реализовать получение данных через вызов функции get_data(), 
а также сохранение подготовленных данных в соответствующий CSV-файл;

Проверить работу программы через вызов функции write_to_csv(). 

### 2. Задание на закрепление знаний по модулю json. 

Есть файл orders в формате JSON с информацией о заказах. 
Написать скрипт, автоматизирующий его заполнение данными. 

Для этого:

Создать функцию write_order_to_json(), в которую передается 5 параметров — товар (item), 
количество (quantity), цена (price), покупатель (buyer), дата (date). 

Функция должна предусматривать запись данных в виде словаря в файл orders.json. 

При записи данных указать величину отступа в 4 пробельных символа;

Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого параметра. 

### 3. Задание на закрепление знаний по модулю yaml. 

Написать скрипт, автоматизирующий сохранение данных в файле YAML-формата. 

Для этого:

Подготовить данные для записи в виде словаря, в котором первому ключу соответствует список, 
второму — целое число, третьему — вложенный словарь, где значение каждого ключа — это целое число 
с юникод-символом, отсутствующим в кодировке ASCII (например, €);

Реализовать сохранение данных в файл формата YAML — например, в файл file.yaml. 

При этом обеспечить стилизацию файла с помощью параметра default_flow_style, 
а также установить возможность работы с юникодом: allow_unicode = True;

Реализовать считывание данных из созданного файла и проверить, совпадают ли они с исходными.

ДЗ 3:
---
###1. Реализовать простое клиент-серверное взаимодействие по протоколу JIM (JSON instant messaging):
клиент отправляет запрос серверу;

сервер отвечает соответствующим кодом результата. 

Клиент и сервер должны быть реализованы в виде отдельных скриптов, содержащих соответствующие функции. 

Функции клиента:
- сформировать presence-сообщение;
- отправить сообщение серверу;
- получить ответ сервера; 
- разобрать сообщение сервера; 

параметры командной строки скрипта client.py <addr> [<port>]: 
- addr — ip-адрес сервера;
- port — tcp-порт на сервере, по умолчанию 7777. 

Функции сервера: 
- принимает сообщение клиента; 
- формирует ответ клиенту; 
- отправляет ответ клиенту; 

имеет параметры командной строки: 
- -p <port> — TCP-порт для работы (по умолчанию использует 7777); 
- -a <addr> — IP-адрес для прослушивания (по умолчанию слушает все доступные адреса).