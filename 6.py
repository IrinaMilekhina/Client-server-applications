'''
Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет», «декоратор».
Проверить кодировку файла по умолчанию. Принудительно открыть файл в формате Unicode и вывести его содержимое.
'''

from chardet.universaldetector import UniversalDetector

detector = UniversalDetector()
with open('test_file.txt', 'rb') as f:
    for line in f:
        detector.feed(line)
        if detector.done:
            break
    detector.close()
print(f'Кодировка файла - {detector.result["encoding"]}')

with open('test_file.txt', 'r', encoding='utf-8') as f:
    text = f.readlines()
for line in text:
    print(line.strip())
