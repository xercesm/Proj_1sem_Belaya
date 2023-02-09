#В матрице найти минимальный и максимальные элементы.

from random import randint

def random_number():
  n, m = 3, 3
  a = [[randint(1, 10) for j in range(m)] for i in range(n)]
  yield a

lst = []
def min_max(i):
  iter_object = iter(i[0])
  while True:
    try:
      next_i = next(iter_object)
      for k in next_i:
        lst.append(k)
    except StopIteration:
      print("Итерация закончилась")
      break
  print(f"Минимальное значение в матрице: {min(lst)}")
  print(f"Максимальное значение в матрице: {max(lst)}")

  iter_object_2 = iter(i[0])
  print("\nСама матрица:")
  while True:
    try:
      c = next(iter_object_2)
      print(*c)
    except StopIteration:
      print("\nВсе!")
      break


b = list(random_number())
min_max(b)
