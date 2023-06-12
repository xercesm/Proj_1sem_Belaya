#Из предложенного текстового файла (text18-2.txt) вывести на экран его содержимое,
#количество знаков препинания. Сформировать новый файл, в который поместить текст в
#стихотворной форме выведя строки в обратном порядке.

import string

file = open('text18-2.txt', 'r', encoding='UTF-8')

data = file.read()
print(data)
print(f'Знаки препинания: {[i for i in data if i in string.punctuation]}')

file.close()

file = open('text18-2.txt', 'r', encoding='UTF-8')

lines = file.readlines()

file.close()
file = open('text-naoborot.txt', 'w', encoding='UTF-8')

file.writelines(lines[::-1])

file.close()