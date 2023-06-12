#Средствами языка Python сформировать текстовый файл (.txt), содержащий
#последовательность из целых положительных и отрицательных чисел. Сформировать
#новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
#обработку элементов:
#Исходные данные:
#Количество элементов:
#Максимальный элемент:
#Произведение элементов меньших 0 в первой половине:


import random

file = open('file.txt', 'w', encoding='UTF-8')

file.write(' '.join([str(random.randint(-20, 20)) for _ in range(20)]))

file.close()

file = open('file.txt', 'r', encoding='UTF-8')

raw_data = file.read().split(' ')
data = [int(i) for i in raw_data]

composion = 1

for num in data[:int(len(data)/2)]:
    if num < 0:
        composion *= num

file.close()

file = open('file.txt', 'w', encoding='UTF-8')

file.write(f'Исходные данные:  {raw_data}\n')
file.write(f'Количество элементов: {len(raw_data)}\n')
file.write(f'Максимальный элемент: {max(data)}\n')
file.write(f'Произведение элементов, меньших 0 в первой половине: {composion}')

file.close()
