# Дана строка, содержащая латинские буквы и круглые скобки. Если скобки
# расставлены правильно (то есть каждой открывающей соответствует одна
# закрывающая), то вывести число 0. В противном случае вывести или номер позиции,
# в которой расположена первая ошибочная закрывающая скобка, или, если
# закрывающих скобок не хватает, число —1.

st = input('Введите строку: ') #создание строки, ввод данных
lst_1 = [] #создание 1 пустого списка
lst_2 = [] #создание 2 пустого списка
for i in st: #цикл, в котором i проходит через всю строку и перебирает все значения
    if i == ')': #если i равняется )
        lst_1.append(i) #
    elif i == '(': #также если i равняется (
        lst_2.append(i) #

if len(lst_1) == len(lst_2): #если список_1 равен список_2
    print(0) #выводим 0
elif len(lst_1) <len(lst_2): #если список_1 меньше, чем список_2
    print(1) #выводим 1
else: #Иначе
    n = 0
    number = 0
    while n < len(st): #повторение цикла 
        if st[n] == '(':
            number += 1
        elif st[n] == ')':
            number += 1
            if number % 2 != 0:
                print(n)
                break
        n += 1