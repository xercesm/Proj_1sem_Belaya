#Из текстового файла (writer.txt) выбрать фамилии писателей и годы жизни.Посчитать общее количество произведений в
#данном файле.

import re

with open('writer.txt', 'r', encoding='utf-8') as file:
    data: str = file.read()

a: list = [i[:-5] for i in re.findall("[А-Я][а-я]+\s[А-Я]\.[А-Я]\.", data)]
date_life: list = re.findall("\(\d{4}\-\d{4}\)", data)
books: list = re.findall("«.+?»", data)

for author, date in zip(a, date_life):
    print(f'{author} {date}')

print(f'Количество произведений: {len(books)}')