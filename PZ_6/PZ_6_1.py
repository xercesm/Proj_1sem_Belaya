#Сформировать и вывести целочисленный список размера 10, содержащий степени
#двойки от первой до 10-й: 2, 4, 8,16, ... .


n = 10 #переменная n ссылается на 10
print('n = ', n) #выводим число n

a1 = [] #создание пустого списка
p = 1 #счетчик с изн.знач 1
for i in range(n): #цикл, в котором i проходится по каждому эл. n в диапазоне до 10
    p *= 2 #умножение счетчика на 2
    a1.append(p) #в пустой список добав. значение p
print(a1) #выводим а1

