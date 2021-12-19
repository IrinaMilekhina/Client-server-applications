'''
Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.
'''

words = ['attribute', 'класс', 'функция', 'type']
for word in words:
    try:
        word_b = bytes(word, encoding='ascii')
        print(type(word_b), word_b)
    except UnicodeEncodeError:
        word_b = bytes(word, encoding='utf-8')
        print(type(word_b), word_b)
        print(word_b.decode('utf-8'))
    print('\n')

'''
Вывод:
В python 3 литералы Bytes создают экземпляр типа bytes вместо типа str. Они могут содержать только ASCII символы, 
однако можно перевестит строку в байтивый формат при указании соответствующей кодировки. 
Вывести байтивую строку в читаемом человеку формате в этом случае нельзя, но работать с ней можно.
'''
