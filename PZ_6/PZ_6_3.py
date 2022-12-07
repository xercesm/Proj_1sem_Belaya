#Дан список размера N. Обнулить элементы списка, расположенные между его
#минимальным и максимальным элементами (не включая минимальный и
#максимальный элементы)

import random
N = int(input('Введите число N: '))
a = [random.randint(1, N) for i in range(N)]
print(a)
max_val = max(a)
max_idx = a.index(max_val)
min_val = min(a)
min_idx = a.index(min_val)
if min_idx < max_idx :
    start_idx = min_idx
    end_idx = max_idx
else :
    start_idx = max_idx
    end_idx = min_idx
i = start_idx + 1
while i < end_idx :
    a[i] = 0
    i += 1
print(a)