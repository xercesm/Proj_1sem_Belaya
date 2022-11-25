# Дана строка, содержащая латинские буквы и круглые скобки. Если скобки
# расставлены правильно (то есть каждой открывающей соответствует одна
# закрывающая), то вывести число 0. В противном случае вывести или номер позиции,
# в которой расположена первая ошибочная закрывающая скобка, или, если
# закрывающих скобок не хватает, число —1.
a = list(input())
b = a.count('(')
c = a.count(')')
#print(b, c)
if c < b:
    print(-1)
elif c > b:
    while b != 0:
        a.remove(')')
        b -= 1
    print(a)
    print(a.index(')'))
else:
    print(0)


# s=input("Введите строку: ")
# v = 0
# list_1 = []
# list_2 = []
# while True:
#     while v < len(s):
#         if s[v] == ")":
#             print(v)
#             break
#         elif v == len(s):
#             break
#         v += 1
#         break
#     for i in s:
#         if (i=="("):
#             list_1.append(i)
#         elif (i == ")"):
#             list_2.append(i)
#     for n in s:
#        if (n==")"):
#         list_2.append(n)
#
#         if len(list_1) == len(list_2):
#             print(0)
#             break
#        else:
#            print(1)
#        break
#     break
#
#
#     # else:
#     #     if (i==")"):
#     #         v=v-1
#     #         for i in s[s.index(")"):]:
#     #             if (i=="("):
#     #                 v=v+1
#
#
# # print(v)
