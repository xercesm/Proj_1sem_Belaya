try:
    a = int(input()) #вводим целочисленные значения А

    if a < 50000: #проверяем условия
        print('4%')
    elif 50000 < a < 100000:
        print('5%')
    elif 10000 < a < 150000:
        print('6%')
    elif 150000 < a < 200000:
        print('7%')
except ValueError:
    print('Введите число!')