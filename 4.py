'''
Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления в байтовое
и выполнить обратное преобразование (используя методы encode и decode).
'''

words = ['разработка', 'администрирование', 'protocol', 'standard']

for word in words:
    b_word = bytes(word, encoding='utf-8')
    s_word = b_word.decode('utf-8')
    print(b_word, s_word)
