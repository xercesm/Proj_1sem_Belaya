#Создайте класс «Студент», который имеет атрибуты имя, фамилия и оценки.
#Добавьте методы для вычисления среднего балла и определения, является ли студент
#отличником.

class Student:
    def __init__(self, name, surname, num: list):
        self.__name = name
        self.__surname = surname
        self.__num = num

    def vichet(self):
        self.ocenki = sum(self.__num) / len(self.__num)
        return self.ocenki

    def otl(self):
        return "Отличник" if self.ocenki == 5 else "не отличник"


obj = Student("Ольга", "Оранская", [5, 5, 5, 5, 5])
obj2 = Student('Николай', 'Сидин', [3, 4, 5, 4, 3])
obj3 = Student('Вова', 'Скляров', [5, 5, 5, 5, 5])
print(obj.vichet())
print(obj.otl())
print(obj2.vichet())
print(obj2.otl())
print(obj3.vichet())
print(obj3.otl())