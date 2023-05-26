# Создайте класс "Человек", который содержит информацию о имени, возрасте и поле.
# Создайте классы "Мужчина" и "Женщина", которые наследуются от класса
# "Человек". Каждый класс должен иметь метод, который выводит информацию о
# поле объекта

class Chelovek:
    def __init__(self, name, surname, pol):
        self.__name = name
        self.__surname = surname
        self.__pol = pol

    def pols(self):
        return 'Мужчина' if self.__pol == 1 else 'Женщина'

class Man:
    def __init__(self, pol=1):
        self.__pol = pol
    def pols(self):
        return 'Мужчина' if self.__pol == 1 else 'Женщина'

class Woman:
    def __init__(self, pol=2):
        self.__pol = pol

    def pols(self):
        return 'Мужчина' if self.__pol == 1 else 'Женщина'



obj = Chelovek("Ольга", "Оранская", 2)
obj2 = Chelovek('Николай', 'Сидин', 1)
obj3 = Chelovek('Вова', 'Скляров', 1)

print(obj.pols())
print(obj2.pols())
print(obj3.pols())