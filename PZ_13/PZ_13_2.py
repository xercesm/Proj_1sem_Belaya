#В матрице найти сумму отрицательных элементов в первой трети матрицы
import random

def generate_matrix(number):
  matr = [[random.randint(-10, 10) for k in range(number)] for j in range(number)]
  return matr

def print_matrix(matrix):
  print('Сама матрица:')
  for k in matrix:
    print(k)

def chet_martix(matrix, size):
  size_tog = size // 3
  sum_otr = 0
  for k in matrix[:size_tog]:
    for j in k:
      if j < 0: sum_otr += j
  yield sum_otr


size_matrix = random.randint(2, 8)
matrix = generate_matrix(size_matrix)
print_matrix(matrix)
print(f'Сумма отрицательных значений в первой трети матрицы: {list(chet_martix(matrix, size_matrix))}')

