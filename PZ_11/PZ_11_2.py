#Из предложенного текстового файла (text18-2.txt) вывести на экран его содержимое,
#количество знаков препинания. Сформировать новый файл, в который поместить текст в
#стихотворной форме выведя строки в обратном порядке.

t = 0
d = 0
q = 1
L = []
D = []
for i in open('text18-2.txt', encoding='UTF-8'):
    print(i, end='')
    t += 1
    for j in i:
        if j in ",.!?;:—….....":
            d += 1
print(end='\n')
print('Количество строк: ', t, end='\n')
print('Количество знаков препинаний : ', d, end='\n')

f1 = open('text18-2.txt', encoding="UTF-8")
for x in f1:
    L.append(x)
f2 = open('text18-3.txt', 'w', encoding="UTF-8")
for x in L:
    D.append(L[-q])
    q -=1

for x in D:
    f2.writelines(x)
f1.close()
f2.close()

