# Дана строка «Петров Иван ПОКС-29 5 4 3 2 5 4 4 5 4». Преобразовать
# информацию из строки в словарь, найти среднее арифметическое оценок,
# результаты вывести на экран.

str1 = 'Петров Иван ПОКС-29 5 4 3 2 5 4 4 5 4' #дана строка
student = {} #создание словаря
a = str1.split() #переменная которая делит элементы в строке
student["Фамилия"] = a[0] #ключом является "Фамилия", это первый элемент
student['Имя'] = a[1] #ключом является "Имя", это второй элемент
student['Группа'] = a[2] #ключом является "Группа", это третий элемент
student['Оценки'] = a[3::] #ключом является "Оценки", он берет элементы от 3 до конца списка
n = 0 #счетчик
for i in a[3::]: #цикл где i проходит по каждому элементу списка от 3 до конца списка
    n+= int(i) #к n прибавляется каждое последующее число в int формате
student['Среднее арифметическое'] = n / len(a[3::]) #ключом является "Среднее арифметическое",
# сумма n-элементов делится на кол-во элементов строки от 3 до конца
for n in student.items():
    print(n)
