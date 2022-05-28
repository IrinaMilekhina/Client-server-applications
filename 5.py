'''
Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из
байтовового в строковый тип на кириллице.
'''
import subprocess
import chardet

sites = ['yandex.ru', 'youtube.com']
max_lines = 5

for site in sites:
    ping_result = subprocess.Popen(['ping', site], stdout=subprocess.PIPE)
    line_num = 1
    for line in ping_result.stdout:
        if line_num <= max_lines:
            decode_name = chardet.detect(line)['encoding']
            line = line.decode(decode_name).encode('utf-8')

            print(line.decode('utf-8').replace('\n', ''))
        else:
            break
        line_num += 1
