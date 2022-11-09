#Дан список размера N. Найти номера тех элементов списка, которые больше своего
#левого соседа, и количество таких элементов. Найденные номера выводить в
#порядке их убывания.

import random

n = random.randrange(2,11)
print('n = ', n)

a = [random.randrange(1,11) for i in range(n)]
print(a)


c = 0
for i in range(len(a)-1,0,-1):
    if a[i] > a[i-1]:
        c += 1
        print(i,end='; ')
print()
print('Count:',c)